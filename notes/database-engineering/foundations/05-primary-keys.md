---
title: Give every student an ID
track: database-foundations
status: structured
---

# Lesson 5: Give every student an ID

Lesson **5 of 10** · [Previous](04-types-and-missing-values.md) · [Course home](README.md)

**Your goal:** identify one student even when names repeat.

## Concept

Our Student table has names. What happens if two students are both named Amina?

We need a reliable way to say which record we mean. A **primary key** is the identifier chosen for a row. Its value must be unique in that table and must not be missing.

We will assign each student a `student_id`. We will also give each course a `course_id`. Names remain useful descriptions, but they are not our identifiers.

These IDs should remain stable when a name or title changes. The prefixes in `S101` and `C101` help us read the examples; they do not create a relationship by themselves.

## Why it matters

Without a reliable identifier, correcting Amina's phone could update the wrong Amina. A primary key lets the application refer to one specific record.

## Example

Add IDs to the Student sketch and allow another student with the same name:

| student_id | student_name | phone |
| --- | --- | --- |
| S101 | Amina | NULL |
| S102 | Rafi | NULL |
| S103 | Amina | NULL |

S101 and S103 are different students. If S101 changes their name, we keep S101 as their identifier.

### Try it

Which additions are valid under our identity rule?

1. A new student S104 named Amina.
2. Another student with ID S101.
3. A student with no ID.

<details>
<summary>Check your answer</summary>

Accept 1: names may repeat and S104 is new. Reject 2: S101 already identifies a student. Reject 3: a primary-key value must not be missing.

</details>

**Ready to move on when:** you can explain why two Aminas are allowed but two student records with S101 are not.

<details>
<summary>Extra reading — open when you want more detail</summary>

## Trade-offs

A dedicated ID gives us stable identity independent of names. It adds a field, and any separate business uniqueness rule still needs to be defined explicitly.

## Common mistakes

- Assuming a name is unique because today's sample has no duplicate names.
- Using the displayed row number as permanent identity.
- Assuming student ID S101 and course ID C101 are connected because they share digits.

## Interview questions

**Can a primary key contain several columns?** Yes. The next lesson uses a pair of IDs to identify an enrollment. First make sure you understand why each Student needs its own identity.

## References

PostgreSQL Global Development Group, *PostgreSQL 18 Documentation, §5.5: Constraints*. [Primary keys](https://www.postgresql.org/docs/18/ddl-constraints.html). Supports uniqueness and requiredness; checked 21 October 2026.

</details>

[← Previous](04-types-and-missing-values.md) · **[Next lesson: Connect students and courses →](06-relationships.md)**
