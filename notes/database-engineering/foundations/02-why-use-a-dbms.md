---
title: Why use a DBMS?
track: database-foundations
status: structured
---

# Lesson 2: Why use a DBMS?

Lesson **2 of 10** · [Previous](01-what-is-a-database.md) · [Course home](README.md)

**Your goal:** distinguish the stored data from the software that manages it.

## Concept

In Lesson 1, we decided which registration facts to remember. We could begin by writing them in a file or spreadsheet.

Now imagine several people updating registrations. Who coordinates their changes? Who decides whether a record is valid? Who controls access?

A **database management system**, or **DBMS**, is software that manages databases. It provides mechanisms to store, retrieve and change data, coordinate access and enforce configured rules.

Remember these three roles:

| Role | In our example |
| --- | --- |
| Application | Shows a registration screen and handles the user's request |
| DBMS | Manages the stored records and the rules we configure |
| Database | Contains the student, course and registration data |

PostgreSQL is one example of a DBMS. We will use the relational approach, which organises data in tables. A DBMS based on this approach is called an **RDBMS**. You do not need to choose or install a product yet.

## Why it matters

Saving a file is only part of the problem. A shared application also needs rules and coordinated changes. Knowing the roles helps us avoid expecting the screen alone to protect the stored data.

## Example

Two administrators download the same registration spreadsheet. One adds Amina. The other adds Rafi and uploads an older copy that does not contain Amina. One person's change can be lost.

A suitable DBMS gives the application ways to coordinate these changes. The application must still use those mechanisms correctly; the DBMS does not guess the intended business rules.

### Try it

Which would you choose for each situation, and why?

1. A temporary list that one person edits once.
2. A registration service that receives requests from many people.

<details>
<summary>Check your answer</summary>

A file or spreadsheet may be sufficient for the temporary list. A DBMS is attractive for the service because changes, rules and access need ongoing coordination. Explain the requirement rather than saying that one option is always better.

</details>

**Ready to move on when:** you can point to the application, DBMS and database as three different roles.

<details>
<summary>Extra reading — open when you want more detail</summary>

## Trade-offs

A DBMS adds useful management capabilities, but also introduces setup, maintenance and learning costs. A small task may not need all of them.

## Common mistakes

- Calling PostgreSQL the application's data: it is the managing software.
- Assuming installing a DBMS automatically prevents every application bug.
- Treating every spreadsheet workflow as unsuitable; the decision depends on the task.

## Interview questions

**How does a database differ from a DBMS?** The database is the organised collection; the DBMS is the software managing it.

## References

IBM, *What is a database?*, IBM Think, undated. [Official overview](https://www.ibm.com/think/topics/database). Explains databases and DBMS responsibilities; checked 21 October 2026.

</details>

[← Previous](01-what-is-a-database.md) · **[Next lesson: Tables, rows and columns →](03-tables-rows-and-columns.md)**
