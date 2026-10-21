# Contributing to My Engineering Playbook

[Home](README.md) · [Roadmaps](roadmaps/README.md) · [Templates](templates/README.md)

Help readers learn an idea, apply it and understand its limitations. Corrections to existing drafts are as useful as new topics.

## Add or improve a note

1. Pick a topic from an existing roadmap, or explain why a new track is useful.
2. Create a branch and copy [the study-note template](templates/study-note.md) into the relevant `notes/` subject folder.
3. Fill all seven sections using clear English, a concrete example and verified references. Set `track` to the matching roadmap filename without `.md`.
4. Add the note to the subject index and its roadmap row. Add practice material under `practice/` when it helps the learner apply the idea.
5. Run the documentation check below and open a pull request with the topic, learning outcome and validation performed.

## Structure and naming

| Location | Convention |
| --- | --- |
| `roadmaps/` | One file per track, linked from the roadmap index |
| `notes/` | Subject folders with their own `README.md` index |
| `practice/` | Exercises and solutions grouped by subject |
| `assets/` | Images with descriptive lowercase names and appropriate attribution |
| `templates/` | Reusable authoring formats and personal study tracker |

Use lowercase kebab-case for new filenames, for example `02-http-basics.md`. Use relative links for repository content, including images. Keep filenames stable once published; the roadmap is the authority for reading order.

Keep code fenced with a language name. Use tables for comparisons and diagrams only when they clarify an idea. Avoid large decorative sections that make the explanation harder to find.

## Content status

Study notes carry a small metadata block with `title`, `track` and `status`.

- `draft`: A note exists but may need structural, source or technical review.
- `structured`: All seven sections contain useful explanations and references. This is a format milestone, not an independent review certification.
- **Planned** is only a roadmap label. Do not create empty notes just to fill the roadmap.

Existing material was migrated as draft content. When improving it, review the technical claims and examples before changing the status. Exercise collections use the [practice template](templates/practice-exercise.md); they do not need concept-note metadata.

## Writing and references

- Explain the concept before introducing implementation detail.
- Name the database, runtime or framework when behaviour is implementation-specific.
- Distinguish illustration, expected output and an actually executed result.
- Cite primary documentation for technical claims. Keep source versions and dates clear for facts that change.
- Prefer original explanations and small original examples; attribute external exercises and images.
- Never add invented benchmarks, citations or claims about production experience.
- Use the [study tracker](templates/study-tracker.md) for personal progress; shared roadmaps describe content availability.

## Validate the documentation

From the repository root, with Python 3.10 or newer:

```bash
python3 scripts/check_docs.py
git diff --check
```

The checker validates local Markdown/HTML links, local image paths, linked Markdown headings, fenced-code balance, note metadata and the seven headings for structured notes. It also checks that each study note is linked from its track roadmap. It does not test external websites, execute lesson code or judge technical accuracy. Review those separately when the content changes.

The same documentation check runs on pull requests and pushes to `main`. For a new roadmap, begin with the [roadmap template](templates/roadmap.md) and add it to the directory.
