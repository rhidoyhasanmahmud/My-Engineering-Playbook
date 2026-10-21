#!/usr/bin/env python3
"""Check local documentation navigation and structured-note conventions.

Uses only the Python standard library. External URLs and lesson code are not
executed. Supports inline/reference Markdown links, HTML src/href attributes,
ATX headings, and backtick/tilde fenced blocks used by this repository.
"""

from __future__ import annotations

import html
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SECTIONS = [
    "Concept", "Why it matters", "Example", "Trade-offs",
    "Common mistakes", "Interview questions", "References",
]


def prose(text: str) -> tuple[str, bool]:
    """Remove front matter, comments and code, retaining line boundaries."""
    text = re.sub(r"\A---\n.*?\n---(?:\n|$)", "", text, count=1, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    output = []
    fence = None
    for line in text.splitlines():
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line)
        if match:
            marker, tail = match.groups()
            if fence is None:
                fence = marker
                continue
            if marker[0] == fence[0] and len(marker) >= len(fence) and not tail.strip():
                fence = None
                continue
        if fence is None:
            output.append(line)
    return "\n".join(output), fence is None


class HTMLLinks(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.targets: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.targets.extend(value for key, value in attrs if key in {"src", "href"} and value)


def destination(value: str) -> str:
    value = value.strip()
    if value.startswith("<"):
        return value[1:value.find(">")]
    # Optional link titles follow whitespace. New repository paths contain no spaces.
    return value.split(maxsplit=1)[0] if value else ""


def links(text: str) -> list[str]:
    # Inline code is an example, not a rendered link.
    text = re.sub(r"(`+)(.+?)\1", "", text)
    result = []
    for match in re.finditer(r"!?\[[^\]\n]*\]\(", text):
        start, cursor, depth = match.end(), match.end(), 1
        while cursor < len(text) and depth:
            char = text[cursor]
            if char == "\\":
                cursor += 2
                continue
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
            cursor += 1
        if depth == 0:
            result.append(destination(text[start:cursor - 1]))
    definitions = {
        key.casefold(): destination(value)
        for key, value in re.findall(r"^\s{0,3}\[([^\]]+)\]:\s*(.+)$", text, re.M)
    }
    for label, ref in re.findall(r"!?\[([^\]\n]+)\]\[([^\]\n]*)\]", text):
        result.append(definitions.get((ref or label).casefold(), ""))
    for label in re.findall(r"(?<!!)\[([^\]\n]+)\](?![\[(\]:])", text):
        if label.casefold() in definitions:
            result.append(definitions[label.casefold()])
    parser = HTMLLinks()
    parser.feed(text)
    return result + parser.targets


def anchors(text: str) -> set[str]:
    result = set()
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, re.M):
        heading = re.sub(r"!?\[([^\]]+)\]\([^)]*\)", r"\1", heading)
        heading = re.sub(r"<[^>]+>", "", heading)
        base = re.sub(r"[^\w\- ]", "", html.unescape(heading).lower()).replace(" ", "-")
        slug, suffix = base, 0
        while slug in result:
            suffix += 1
            slug = f"{base}-{suffix}"
        result.add(slug)
    result.update(re.findall(r'\b(?:id|name)=["\']([^"\']+)["\']', text))
    return result


def main() -> int:
    files = sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)
    bodies, errors, graph = {}, [], {}
    for path in files:
        text = path.read_text(encoding="utf-8")
        body, balanced = prose(text)
        bodies[path] = body
        if not balanced:
            errors.append(f"{path.relative_to(ROOT)}: unclosed fenced code block")
    heading_ids = {path: anchors(body) for path, body in bodies.items()}
    checked_links = 0
    for path, body in bodies.items():
        graph[path] = set()
        for target in links(body):
            parsed = urlsplit(html.unescape(target))
            if parsed.scheme or parsed.netloc:
                continue
            if not target:
                errors.append(f"{path.relative_to(ROOT)}: empty or undefined link")
                continue
            raw_path = unquote(parsed.path)
            resolved = ((ROOT / raw_path.lstrip("/")) if raw_path.startswith("/")
                        else (path.parent / raw_path) if raw_path else path).resolve()
            checked_links += 1
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing local target {target}")
                continue
            if resolved.is_dir() and (resolved / "README.md").exists():
                resolved /= "README.md"
            graph[path].add(resolved)
            fragment = unquote(parsed.fragment)
            if fragment and resolved in heading_ids and fragment not in heading_ids[resolved]:
                errors.append(f"{path.relative_to(ROOT)}: missing heading {target}")
    counts = {"draft": 0, "structured": 0}
    for path in files:
        if path.relative_to(ROOT).parts[0] != "notes" or path.name == "README.md":
            continue
        text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        metadata = dict(re.findall(r"^(\w+):\s*(.+)$", match[1], re.M)) if match else {}
        if any(not metadata.get(key) for key in ("title", "track", "status")):
            errors.append(f"{path.relative_to(ROOT)}: requires title, track and status metadata")
            continue
        status, track = metadata["status"], metadata["track"]
        if status not in counts:
            errors.append(f"{path.relative_to(ROOT)}: invalid status {status}")
            continue
        counts[status] += 1
        roadmap = ROOT / "roadmaps" / f"{track}.md"
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", track) or not roadmap.is_file():
            errors.append(f"{path.relative_to(ROOT)}: unknown roadmap {track}")
        elif path not in graph.get(roadmap, set()):
            errors.append(f"{path.relative_to(ROOT)}: not linked from its roadmap")
        if status == "structured":
            sections = re.findall(r"^## (.+)$", bodies[path], re.M)
            if sections != SECTIONS:
                errors.append(f"{path.relative_to(ROOT)}: requires the seven sections in template order")
            for heading, content in re.findall(r"^## (.+)\n(.*?)(?=^## |\Z)", bodies[path], re.M | re.S):
                if not content.strip():
                    errors.append(f"{path.relative_to(ROOT)}: empty section {heading}")
                if heading == "References" and not any(urlsplit(url).scheme in {"http", "https"} for url in links(content)):
                    errors.append(f"{path.relative_to(ROOT)}: References needs an external source link")
    visited, pending = set(), [ROOT / "README.md"]
    while pending:
        path = pending.pop()
        if path in visited:
            continue
        visited.add(path)
        pending.extend(graph.get(path, set()) - visited)
    for path in files:
        if path not in visited and ".github" not in path.parts:
            errors.append(f"{path.relative_to(ROOT)}: not reachable from the root README")
    if errors:
        print("Documentation checks failed:\n" + "\n".join(f"- {error}" for error in errors))
        return 1
    print(f"PASS: {len(files)} Markdown files; {checked_links} local links; all learning pages reachable.")
    print(f"Study notes: {counts['structured']} structured, {counts['draft']} draft.")
    print("External URLs, example execution and technical accuracy are outside this check.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
