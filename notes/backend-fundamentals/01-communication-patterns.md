---
title: Backend communication patterns
track: backend-fundamentals
status: structured
---

# Backend communication patterns

[Study roadmap](../../roadmaps/backend-fundamentals.md) · [Backend notes](README.md)

**Level:** Foundation. **Prerequisite:** Understand what a client and a server are.

## Concept

**Request-response** describes an exchange: a client asks for something and the server returns a response. HTTP is a familiar example. Opening a weather page might send a request for the latest temperature.

**Synchronous and asynchronous execution** describe how the caller handles waiting. A synchronous call waits before continuing that execution path. An asynchronous API gives the caller a way to receive the result later, such as a future or callback.

These are different dimensions. An asynchronous HTTP client still exchanges a request and a response. For example, Java's `HttpClient.send()` waits for a response, while `sendAsync()` returns a `CompletableFuture`.

**Push updates** let a server deliver new information over an established channel. With Server-Sent Events (SSE), a browser opens an event stream and receives subsequent server messages without a fresh request for every update. The initial connection still comes from the client.

## Why it matters

A weather lookup, a large report and a live scoreboard have different user expectations. Choosing how they communicate affects waiting time, failure handling and how much state the application must track.

Ask two questions first: does the user need the final answer now, and how will they learn about a later result or failure?

## Example

Imagine an application with three features. The following is an illustrative API design, not a runnable service or a benchmark.

| Feature | Possible design | What the user sees |
| --- | --- | --- |
| Weather lookup | Request the current weather and return the result | A temperature or a clear error |
| Report generation | Accept a job, return a job identifier and provide a status endpoint | Progress followed by a download or failure |
| Live scoreboard | Open an SSE stream for score updates | New scores arrive while the page remains connected |

A report request could receive this response:

```http
HTTP/1.1 202 Accepted
Content-Type: application/json
Location: /reports/job-42

{"jobId":"job-42","status":"queued"}
```

Here, the status endpoint and JSON fields are application design choices. HTTP `202` means the request was accepted for processing; it does not promise successful completion. The client needs a way to discover the eventual outcome.

**Try it:** List three report states and what the client should display for each. Then explain what happens if the client loses its connection after submitting the job.

## Trade-offs

| Choice | Benefit | Cost or limitation |
| --- | --- | --- |
| Wait for a final response | Straightforward interaction for a short operation | The caller depends on the operation finishing within its waiting budget |
| Track a background job | The caller can continue while work finishes | Requires job state, failure reporting and a way to retrieve the result |
| Poll a status endpoint | Simple client-driven checking | Repeated requests and a delay between completion and the next poll |
| Receive SSE updates | Server-to-client updates over an open stream | Requires connection handling and an application decision about missed events |

An asynchronous API alone does not make the server operation faster. Its immediate benefit is how the caller can use the waiting period.

## Common mistakes

- **Treating asynchronous HTTP as a different exchange pattern.** It can still be request-response; the caller's waiting behaviour changes.
- **Showing “completed” after a `202`.** Show acceptance or progress until the application confirms a final result.
- **Assuming push needs no client setup.** SSE begins with a client-created event stream.
- **Ignoring disconnects.** Specify how a client discovers the latest state or resumes updates after reconnecting.
- **Choosing a complex background workflow for every operation.** First explain why the operation needs it and how errors will be visible.

## Interview questions

1. **Can request-response be asynchronous?** Yes. The client can receive the response through a future or callback instead of waiting synchronously.
2. **Does `202 Accepted` mean the report was generated?** No. It means processing was accepted; the final result still needs to be discovered.
3. **When would you use polling instead of SSE?** Occasional updates and simple connection management may favour polling; discuss the extra requests and update delay.
4. **What would you ask before choosing a pattern?** Expected duration, update frequency, failure behaviour and how the client obtains the final outcome.

## References

- **IETF / RFC Editor:** Roy T. Fielding, Mark Nottingham and Julian Reschke (editors), *HTTP Semantics*, RFC 9110, 2022. [Official specification](https://www.rfc-editor.org/rfc/rfc9110.html), especially Section 15.3.3 for `202 Accepted`.
- **Oracle:** *Java SE 21 API — HttpClient*. [Official API documentation](https://docs.oracle.com/en/java/javase/21/docs/api/java.net.http/java/net/http/HttpClient.html). Supports the distinction between `send()` and `sendAsync()`.
- **WHATWG:** *HTML Living Standard — Server-sent events*. [Official specification](https://html.spec.whatwg.org/multipage/server-sent-events.html). Explains `EventSource`, event streams and reconnection behaviour.

Sources consulted on 2026-10-21. The application scenarios and comparison above are original teaching examples.
