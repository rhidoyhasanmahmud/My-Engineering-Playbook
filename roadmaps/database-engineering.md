# Database engineering roadmap

[All roadmaps](README.md) · [Database notes](../notes/database-engineering/README.md) · [SQL practice](../practice/sql/README.md)

**Goal:** Understand how databases preserve data and how storage, transactions and indexes affect application behaviour.

**Prerequisites:** Basic programming and familiarity with tables, rows and columns. If SQL is new to you, learn `SELECT`, filtering and joins before the internals and indexing steps; a complete introductory SQL lesson is still planned.

| Step | Topic | Study material | Status | Practical checkpoint |
| --- | --- | --- | --- | --- |
| 1 | Database foundations | [Database introduction](../notes/database-engineering/01-database-introduction.md) | Draft | Describe when an application needs a database and compare row-oriented and column-oriented storage |
| 2 | SQL foundations | [Query order notes](../practice/sql/query-order.md) and [five SQL exercises](../practice/sql/leetcode/README.md) | Draft; full introduction planned | Write a filter with `NULL` handling and explain the logical stages of a query |
| 3 | Transactions and consistency | [ACID](../notes/database-engineering/02-acid.md) | Draft | Explain what should happen if a money transfer fails halfway through |
| 4 | Storage internals | [Database internals](../notes/database-engineering/03-database-internals.md) | Draft | Sketch pages, rows and an index lookup; identify engine-specific assumptions |
| 5 | Tree indexes | [B-Tree and B+ Tree](../notes/database-engineering/05-b-tree-and-b-plus-tree.md) | Draft | Explain why ordered indexes help with range queries |
| 6 | Indexing and query planning | [Database indexing](../notes/database-engineering/04-database-indexing.md) | Draft | Compare a query plan before and after an index and discuss the write cost |
| 7 | SQL and schema practice | [Interview challenges](../practice/sql/interview-challenges.md) and [design scenarios](../practice/database-design/scenarios.md) | Draft | Design an enrolment schema with keys and constraints; solve a per-department salary query |
| 8 | Concurrency and operations | Notes to be written | Planned | Reproduce an isolation anomaly and explain a backup/restore approach |

The roadmap defines the reading order. Existing numeric filenames are identifiers and may differ from that order.

## Check your understanding

Use the preserved [database review questions](../practice/database-design/review-questions.md). Explain the answer for a named database engine where behaviour differs.

## Suggested application

Pick one [database design scenario](../practice/database-design/scenarios.md). Create the schema locally, insert a small dataset, write queries and inspect one execution plan. Record the database version and observations. A packaged database lab is not included yet.
