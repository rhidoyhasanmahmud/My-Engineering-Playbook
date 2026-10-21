---
title: Tables, rows and columns
track: database-foundations
status: structured
---

# Lesson 3: Tables, rows and columns

Lesson **3 of 10** · [Previous](02-why-use-a-dbms.md) · [Course home](README.md)

**Your goal:** explain exactly what one row represents.

## Concept

We chose the relational approach in Lesson 2. It organises data into **tables**.

A table holds records about a particular kind of thing or relationship. A **row** is one record. A **column** describes one attribute of that record.

Before choosing columns, finish this sentence: **“One row in this table represents…”**

For Student, one row represents one student registered in our system. A name and a phone value both describe that student. Course information will have its own table.

The table's structure and rules are part of its **schema**. The actual records stored today are its **data**. Adding a student changes the data. Adding a new column changes the schema.

## Why it matters

If we cannot explain what a row means, we may mix several different things in one record. Clear row meaning tells us where a new fact belongs.

## Example

This first sketch of Student has two rows and two columns:

| student_name | phone |
| --- | --- |
| Amina | Not provided |
| Rafi | Not provided |

“Not provided” is an explanatory label here. Lesson 4 explains how to represent missing values.

A Course table has a different row meaning: one row represents one course in the catalogue.

| course_title |
| --- |
| Database Foundations |
| Backend Basics |

We have not connected students to courses yet. We will first learn to describe values and identify records.

### Try it

Add a student named Hasan to the Student sketch. Do you add a row or a column? What would adding a `preferred_language` column change?

<details>
<summary>Check your answer</summary>

Add a row for Hasan, because each row is one student. Adding `preferred_language` changes the table's structure so every student record can hold that new attribute.

</details>

**Ready to move on when:** you can explain the row meaning of both Student and Course.

<details>
<summary>Extra reading — open when you want more detail</summary>

## Trade-offs

Separating students and courses keeps their meanings clear. Later, we will need an explicit way to connect them; copying everything into one table creates other problems.

## Common mistakes

- Adding a new column for every new student.
- Using a displayed row position as a permanent identifier. Stored rows have no guaranteed display order.
- Confusing a new record with a structural change.

## Interview questions

**Does correcting Amina's name change the schema?** No. It changes a value in the existing structure.

## References

PostgreSQL Global Development Group, *PostgreSQL 18 Documentation, §2.2: Concepts*. [Official documentation](https://www.postgresql.org/docs/18/tutorial-concepts.html). Tables, rows, columns and ordering; checked 21 October 2026.

</details>

[← Previous](02-why-use-a-dbms.md) · **[Next lesson: Types and missing values →](04-types-and-missing-values.md)**
