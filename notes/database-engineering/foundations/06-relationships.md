---
title: Connect students and courses
track: database-foundations
status: structured
---

# Lesson 6: Connect students and courses

Lesson **6 of 10** · [Previous](05-primary-keys.md) · [Course home](README.md)

**Your goal:** record which student takes which course.

## Concept

We now have student IDs and course IDs. A student may take several courses, and a course may have several students. This is a **many-to-many relationship**.

Create an **Enrollment** table. One row means one student enrolled in one course. Each row contains the student's ID and the course's ID.

An ID used as a controlled reference to an existing record is a **foreign key**. Enrollment's `student_id` refers to Student; its `course_id` refers to Course. We will define the rule that protects these references in Lesson 7.

For this small teaching system, a student can have only one enrollment record per course. Together, `(student_id, course_id)` identify the enrollment. This is a **composite primary key**: one key made from two fields. Retakes are outside this version of the model.

## Why it matters

The relationship is a fact of its own. An enrollment connects two records without copying the student's whole profile or the course's whole description.

## Example

Keep the Student records from Lesson 5. Our courses are:

| course_id | course_title |
| --- | --- |
| C101 | Database Foundations |
| C102 | Backend Basics |

Now record these enrollments:

| student_id | course_id |
| --- | --- |
| S101 | C101 |
| S101 | C102 |
| S102 | C101 |

S101 takes two courses. C101 has two students. S103 has no enrollment yet; that is allowed. We do not create an empty Enrollment row for S103.

### Try it

S103 enrolls in C102. Which table needs a new row? Write that row. Do we need another Student or Course record?

<details>
<summary>Check your answer</summary>

Add `(S103, C102)` to Enrollment. Both the student and the course already exist, so no new Student or Course record is needed.

</details>

**Ready to move on when:** you can follow an enrollment's two IDs back to its student and course.

<details>
<summary>Extra reading — open when you want more detail</summary>

## Trade-offs

An association table adds another place to read, but supports any number of courses without adding fields such as `course_1`, `course_2` and `course_3` to Student.

## Common mistakes

- Making `student_id` alone the enrollment key, which would allow only one enrollment per student.
- Storing a comma-separated list of courses inside one student field.
- Forgetting that “zero enrollments” can be a valid state.

## Interview questions

**Where should the date of enrollment go?** In Enrollment, because the date describes a particular student joining a particular course.

## References

PostgreSQL Global Development Group, *PostgreSQL 18 Documentation, §5.5: Constraints*. [Foreign keys and many-to-many relationships](https://www.postgresql.org/docs/18/ddl-constraints.html). Checked 21 October 2026; executable syntax is for later study.

</details>

[← Previous](05-primary-keys.md) · **[Next lesson: Define valid data →](07-constraints.md)**
