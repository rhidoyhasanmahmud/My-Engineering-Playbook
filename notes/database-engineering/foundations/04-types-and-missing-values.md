---
title: Types and missing values
track: database-foundations
status: structured
---

# Lesson 4: Types and missing values

Lesson **4 of 10** · [Previous](03-tables-rows-and-columns.md) · [Course home](README.md)

**Your goal:** choose a sensible kind of value for a column and explain a missing value.

## Concept

A **data type** describes the kind of value a column can hold. Choose it from the field's meaning.

| Kind of value | Example use |
| --- | --- |
| Text | A student's name or phone number |
| Whole number | A count of available places |
| Date | The calendar date a registration was accepted |

A phone number is text even when it contains digits. We do not add two phone numbers together, and a leading zero or `+` can be meaningful.

Sometimes we do not have a value. **NULL** is the marker used for a missing value in SQL databases. It is different from zero, an empty string and the text `"NULL"`.

For our optional phone field, NULL will mean **“no phone value was supplied.”** Choosing that meaning is part of the design.

## Why it matters

An unsuitable type can damage the meaning of data. Replacing a missing phone with zero invents a value rather than recording its absence.

## Example

Replace the explanatory labels from Lesson 3 with a missing-value marker:

| student_name | phone |
| --- | --- |
| Amina | NULL |
| Rafi | NULL |

The names are required for our application. A phone is optional. NULL here is a symbol for absence, not something we ask the user to type.

Later, each enrollment will have an `enrolled_on` date such as `2026-10-01`. A calendar date is sufficient for this teaching example; exact event times would require more decisions.

### Try it

A form gives you a name, a phone value beginning with zero and a registration date. Choose a conceptual type for each. What should the phone contain if the person supplies no number?

<details>
<summary>Check your answer</summary>

Use text for the name and phone, and a date for the registration date. Use a missing value for the optional phone, with the meaning “not supplied.” Do not use numeric zero as a substitute.

</details>

**Ready to move on when:** you can explain why a phone number is text and why missing is different from zero.

<details>
<summary>Extra reading — open when you want more detail</summary>

## Trade-offs

Optional fields let us record a student without every detail, but every reader must understand what absence means. Require a field when the business genuinely needs it.

## Common mistakes

- Treating all digit-containing values as quantities.
- Using one missing marker for several meanings when the business needs to distinguish them.
- Assuming NULL participates in comparisons exactly like an ordinary value. SQL will teach its special behaviour later.

## Interview questions

**Is a missing count equal to zero?** No. Zero is a known quantity; missing means the quantity has not been supplied or established.

## References

PostgreSQL Global Development Group, *PostgreSQL 18 Documentation, §2.2: Concepts* and *§9.2: Comparison Functions and Operators*. [Column types](https://www.postgresql.org/docs/18/tutorial-concepts.html) and [missing-value behaviour](https://www.postgresql.org/docs/18/functions-comparison.html). Checked 21 October 2026; the SQL syntax is for later study.

</details>

[← Previous](03-tables-rows-and-columns.md) · **[Next lesson: Give every student an ID →](05-primary-keys.md)**
