---
title: Define valid data
track: database-foundations
status: structured
---

# Lesson 7: Define valid data

Lesson **7 of 10** · [Previous](06-relationships.md) · [Course home](README.md)

**Your goal:** explain why a proposed record should be accepted or rejected.

## Concept

A **constraint** is a rule about which stored data is allowed. The primary key from Lesson 5 is one example.

Our model needs a few explicit rules:

| Rule | What it protects |
| --- | --- |
| Required | A student must have an ID and name; phone may be absent |
| Unique | Each student ID is distinct; each enrollment pair appears at most once |
| Valid reference | Enrollment must refer to an existing Student and Course |
| Allowed value | Enrollment status must be `active`, `completed` or `cancelled` |

The valid-reference rule is enforced through a foreign-key constraint. Merely naming a column `student_id` does not establish that rule.

We also choose a deletion policy: a course with enrollment records cannot be deleted until those dependent records are handled explicitly.

## Why it matters

A registration screen is not the only place that can change data. Imports and background processes may also write records. Database constraints help the defined rules apply across those entry points.

## Example

Extend Enrollment with a required acceptance date and status:

| student_id | course_id | enrolled_on | status |
| --- | --- | --- | --- |
| S101 | C101 | 2026-10-01 | active |
| S101 | C102 | 2026-10-02 | active |
| S102 | C101 | 2026-10-03 | completed |

S103 exists as a student, but S999 does not. C101 and C102 both exist.

### Try it

Consider each change independently:

1. Add S103 to C102 with a supplied date and `active` status.
2. Add S999 to C101.
3. Add another enrollment for S101 and C101.
4. Change an enrollment's status to `waiting`.
5. Delete C101 while the enrollments above remain.

<details>
<summary>Check your answer</summary>

Accept 1. Reject 2 because the student reference is invalid. Reject 3 because the enrollment pair already exists. Reject 4 because the status is outside our allowed set. Reject 5 under our chosen deletion policy.

</details>

**Ready to move on when:** you can name the rule behind each decision, rather than only guessing accept or reject.

<details>
<summary>Extra reading — open when you want more detail</summary>

## Trade-offs

Strict rules prevent inconsistent records, but can also reject legitimate cases if we misunderstood the requirements. Agree on the rule before enforcing it.

## Common mistakes

- Assuming a default value rejects all other values; a default only supplies an omitted value.
- Assuming a valid status proves a valid transition between statuses.
- Treating a required name as automatically nonblank. Empty or whitespace-only names need an explicit validation rule too.

## Interview questions

**Does a foreign key prove the student wanted to enroll?** No. It establishes a valid reference, not real-world consent or every business condition.

## References

PostgreSQL Global Development Group, *PostgreSQL 18 Documentation, §5.5: Constraints*. [Official documentation](https://www.postgresql.org/docs/18/ddl-constraints.html). Required values, uniqueness, foreign keys and deletion actions; checked 21 October 2026.

</details>

[← Previous](06-relationships.md) · **[Next lesson: Draw your first model →](08-draw-the-model.md)**
