# Database foundations: before SQL

**New to databases? [Start here →](../notes/database-engineering/foundations/README.md)**

Learn one idea at a time, using a small Student–Course system. No programming, SQL or installation is required. Each lesson has a short explanation, a worked example, a practice question and a **Next lesson** link.

For your first session, complete only [Lesson 1](../notes/database-engineering/foundations/01-what-is-a-database.md). The list below is a map to return to, not a reading assignment for today.

## Lesson list

| Lesson | The question you will answer |
| --- | --- |
| **Part 1: Understand the data** | |
| [1. What is a database?](../notes/database-engineering/foundations/01-what-is-a-database.md) | What does our application need to remember? |
| [2. Why use a DBMS?](../notes/database-engineering/foundations/02-why-use-a-dbms.md) | Which software manages the stored information? |
| [3. Tables, rows and columns](../notes/database-engineering/foundations/03-tables-rows-and-columns.md) | What does one record represent? |
| [4. Types and missing values](../notes/database-engineering/foundations/04-types-and-missing-values.md) | What kind of value belongs in a field? |
| **Part 2: Connect and protect it** | |
| [5. Give every student an ID](../notes/database-engineering/foundations/05-primary-keys.md) | How do we distinguish two students with the same name? |
| [6. Connect students and courses](../notes/database-engineering/foundations/06-relationships.md) | How do we record who takes which course? |
| [7. Define valid data](../notes/database-engineering/foundations/07-constraints.md) | Which records should be accepted or rejected? |
| **Part 3: Complete a small design** | |
| [8. Draw your first model](../notes/database-engineering/foundations/08-draw-the-model.md) | How do the rules appear in a diagram? |
| [9. Keep each fact in the right place](../notes/database-engineering/foundations/09-normalization.md) | How do we avoid conflicting copies of the same fact? |
| [10. Finish your first design](../notes/database-engineering/foundations/10-finish-your-first-design.md) | Can we explain and check the whole model ourselves? |

All ten lessons are available in the structured study-note format. Their **Extra reading** boxes hold trade-offs, common mistakes, interview questions and references. Open those when you want more detail; the main explanation and practice come first.

## Ready to start SQL

Complete the small design task in [Lesson 10](../notes/database-engineering/foundations/10-finish-your-first-design.md). You should be able to explain what each row means, how keys connect records, why invalid changes are rejected and why descriptive facts belong in separate tables.

If a question is difficult, revisit its linked lesson and try again. There is no fixed number of days or interview score to reach.

## Next learning stage

Next, choose a database engine, create the tables and learn basic SQL for reading and changing data. A full repository SQL introduction is **planned**. The official [PostgreSQL 18 SQL-language tutorial](https://www.postgresql.org/docs/18/tutorial-sql.html) is an available next-stage resource; follow its setup prerequisites first.

Use the [database engineering roadmap](database-engineering.md) to see the later SQL, transaction and indexing stages. Advanced internals are not prerequisites for starting SQL.

<details>
<summary>Optional reference and extra practice</summary>

- [Database foundation reference handbook](../notes/database-engineering/00-before-sql.md): the comprehensive explanation, including alternative data models, additional key terminology, formal definitions and transaction awareness. Use it to look up a question after the lessons.
- [Library-loan challenge](../practice/database-design/before-sql-capstone.md): apply the ideas to a different domain, with repeat borrowing and more demanding rules. Its answer guide is included.
- [Personal study tracker](../templates/study-tracker.md): optional space for your own progress and questions.

These are optional extensions. Completing them is not a condition for finishing the beginner path.

</details>

[All roadmaps](README.md) · [Course home](../notes/database-engineering/foundations/README.md)
