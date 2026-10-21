---
title: Finish your first design
track: database-foundations
status: structured
---

# Lesson 10: Finish your first design

Lesson **10 of 10** · [Previous](09-normalization.md) · [Course home](README.md)

**Your goal:** explain and check the small model you have built.

## Concept

A useful design tells another person what each record means, how records connect and which changes are valid. A diagram is part of that explanation; written rules and small examples complete it.

You already know the pieces. This final lesson asks you to use them together with the same Student–Course example.

## Why it matters

Explaining your own model shows where a rule is still unclear. Finding that uncertainty on paper is easier than discovering it after an application starts storing conflicting records.

## Example

Keep this situation in mind:

- Students S101 (Amina), S102 (Rafi) and S103 (Amina) are registered.
- Department D10 (Computing) offers C101 (Database Foundations) and C102 (Backend Basics).
- S101 takes C101 and C102. S102 takes C101. S103 has not enrolled yet.
- Each enrollment has a date and status. A student–course pair may appear only once; phone is optional.

### Try it

Without copying Lesson 8:

1. Draw the four tables. State what one row means and mark each primary key and foreign key.
2. Write the three existing enrollment pairs. Explain how S103 is represented.
3. Explain what changes when S103 enrolls in C102. Choose a date and allowed status.
4. Explain why a second S101–C101 enrollment is rejected.
5. Explain where to update the name of D10 without changing course identity.

<details>
<summary>Check your design</summary>

| Table | Identity | References |
| --- | --- | --- |
| Student | `student_id` | None in this model |
| Department | `department_id` | None in this model |
| Course | `course_id` | `department_id` refers to Department |
| Enrollment | `(student_id, course_id)` | Refers to Student and Course |

One row represents one student, department, course or student–course enrollment respectively. The three existing enrollment pairs are `(S101, C101)`, `(S101, C102)` and `(S102, C101)`.

S103 has a Student row and no Enrollment row yet. Add `(S103, C102)` with a date and, for example, `active` status when that student enrolls. Do not duplicate Student or Course.

A second S101–C101 row violates the unique enrollment pair. Rename D10 in Department; courses continue referring to the same D10 identifier.

</details>

### Ready to begin SQL?

You are ready to start when you can explain:

- What one row means in each table.
- How keys identify records and connect them.
- Why duplicate or invalid references are rejected.
- Why names belong with their student or department records.

If one answer is unclear, use [Lesson 3](03-tables-rows-and-columns.md), [Lesson 5](05-primary-keys.md), [Lesson 7](07-constraints.md) or [Lesson 9](09-normalization.md) to revisit that specific idea.

**SQL** is the language we will use to define these tables and read or change their records. The next stage is practical: choose a database engine, create this model and learn basic SQL. You do not need to complete the optional reference material first.

<details>
<summary>Extra reading — open when you want more detail</summary>

## Trade-offs

The one-enrollment-per-course rule makes our example small. A real system with retakes or terms needs a revised model. A simple design is useful when its boundaries are explicit.

## Common mistakes

- Memorising a diagram without understanding its rules.
- Treating this teaching model as suitable for every real course system.
- Waiting to master all advanced terminology before beginning SQL practice.

## Interview questions

**What changes if S101 can retake C101?** The unique student–course pair no longer identifies every separate attempt at the course. Reconsider enrollment identity, typically around a course offering or attempt. This is an optional extension, not a requirement for finishing the beginner path.

## References

PostgreSQL Global Development Group, *PostgreSQL 18 Documentation, Chapter 2: The SQL Language*. [Official next-stage tutorial](https://www.postgresql.org/docs/18/tutorial-sql.html). Introduces SQL after the database setup described in its prerequisites; checked 21 October 2026.

For later revision, use the [reference handbook](../00-before-sql.md). To practise with a different domain after the beginner path, try the optional [library-loan challenge](../../../practice/database-design/before-sql-capstone.md).

</details>

[← Previous](09-normalization.md) · **[Next: the SQL learning stage →](../../../roadmaps/database-foundations.md#next-learning-stage)**
