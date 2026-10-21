---
title: What is a database?
track: database-foundations
status: structured
---

# Lesson 1: What is a database?

Lesson **1 of 10** · [Course home](README.md)

**Your goal:** explain why a course-registration application needs to remember data.

## Concept

Imagine that Amina registers for a course. She closes the application and opens it tomorrow. She expects to see the same registration.

The application needs to remember facts: who Amina is, which course she selected and when she registered. Recorded facts like these are **data**.

A **database** is an organised collection of related data. In this course, our database will hold the information needed by a small course-registration system.

Think of the database as the organised information the application remembers. The screen is one way to view that information; closing the screen does not mean we want to erase the registration.

## Why it matters

An application becomes useful when it can keep track of earlier actions. Otherwise, the learner would have to register again every time they opened it.

We first need to decide **what must be remembered**. Later lessons will explain how to organise and manage it.

## Example

Our course application needs to remember:

| Fact | Example |
| --- | --- |
| Student's name | Amina |
| Course title | Database Foundations |
| Registration date | 2026-10-01 |

These are invented examples. We are designing on paper; no database software is needed.

### Try it

Rafi registers for Backend Basics. Write three facts the application should remember about this registration.

<details>
<summary>Check your answer</summary>

Rafi's name, the title Backend Basics and the date of registration. Your example date may differ. The important point is that these facts belong to the registration we want to remember.

</details>

**Ready to move on when:** you can explain what a database is using this registration example.

<details>
<summary>Extra reading — open when you want more detail</summary>

## Trade-offs

Keeping data makes later retrieval possible, but we must decide which facts are useful and keep them accurate. Collecting more personal information is not automatically helpful.

## Common mistakes

- Thinking the application screen and the stored information are the same thing.
- Assuming all databases must use tables. We will use tables in this course; other models also exist.

## Interview questions

**What is a database?** An organised collection of related data. Explain which facts your example system stores and why.

## References

IBM, *What is a database?*, IBM Think, undated. [Official overview](https://www.ibm.com/think/topics/database). Supports the introductory database definition; checked 21 October 2026.

</details>

**[Next lesson: Why use a DBMS? →](02-why-use-a-dbms.md)**
