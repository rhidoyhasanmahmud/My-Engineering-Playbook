# Backend fundamentals roadmap

[All roadmaps](README.md) · [Backend notes](../notes/backend-fundamentals/README.md)

**Goal:** Understand how backend services exchange information and make basic communication decisions.

**Prerequisites:** Basic programming, functions, and a general understanding of a client and a server. The first note introduces request-response, synchronous/asynchronous calls and push.

| Step | Topic | Study material | Status | Practical checkpoint |
| --- | --- | --- | --- | --- |
| 1 | Communication patterns | [Communication patterns](../notes/backend-fundamentals/01-communication-patterns.md) | Structured | Choose a pattern for weather lookup, report generation and live score updates; explain one trade-off for each |
| 2 | HTTP and request lifecycle | Note to be written | Planned | Trace a request through DNS, connection setup, HTTP processing and a response |
| 3 | API design and validation | Note to be written | Planned | Design endpoints with validation and error responses |
| 4 | Timeouts, retries and idempotency | Note to be written | Planned | Explain how a retry could duplicate an operation and propose a prevention strategy |
| 5 | Authentication and authorisation | Note to be written | Planned | Distinguish identity verification from permission checks |
| 6 | Caching and rate limiting | Note to be written | Planned | Choose a cache expiry strategy and explain stale data behaviour |

## Check your understanding

- Can you separate a communication pattern from the way a caller waits for a result?
- Can you explain why an accepted request might still fail later?
- Can you identify what a caller should do when a dependency is slow?

## Suggested application

Design a small order service. Explain which operations need an immediate answer, which can finish later, and how a client learns the result. This is a suggested exercise; a runnable implementation is not included yet.

For persistent state, continue with the [database engineering roadmap](database-engineering.md).
