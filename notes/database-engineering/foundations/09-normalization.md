---
title: Keep each fact in the right place
track: database-foundations
status: structured
---

# Lesson 9: Keep each fact in the right place

Lesson **9 of 10** · [Previous](08-draw-the-model.md) · [Course home](README.md)

**Your goal:** explain why the four-table design avoids repeating descriptive facts.

## Concept

What if we copied the student name and department name into every enrollment? Changing one name could require many edits. Missing one edit would leave conflicting versions of the same fact.

**Normalization** helps us organise facts according to what they describe. It reduces avoidable repetition and the errors that repetition can cause.

For our simple model, use this question: **“What does this fact depend on?”** A student's name depends on the student, not on which course they take. A department's name depends on the department, not on which course belongs to it.

## Why it matters

Repeated descriptive facts can cause three problems, called anomalies:

- **Update:** the same name is corrected in some rows but not others.
- **Insertion:** we cannot record a course until somebody enrolls.
- **Deletion:** removing the last enrollment also removes the only stored course details.

Separate Student, Department and Course records let those facts exist independently of enrollments.

## Example

Keep the business rules from Lesson 8. The following small views show only the columns needed for each step.

### Step 1: One enrollment per row — 1NF

Avoid a student field containing a packed course list such as `C101, C102`. Record each student–course association separately:

| student_id | course_id | student_name |
| --- | --- | --- |
| S101 | C101 | Amina |
| S101 | C102 | Amina |
| S102 | C101 | Rafi |

Each field now holds one value for the intended purpose, with no repeating course group. This illustrates **first normal form (1NF)**. Repeated descriptive facts still remain.

### Step 2: Facts about the whole enrollment — 2NF

Our enrollment key is the pair `(student_id, course_id)`. But `student_name` depends on only `student_id`, one part of that key.

Keep the name in Student. Keep course facts in Course. Enrollment keeps the two IDs plus facts about that particular enrollment, such as its date and status.

For this model, removing these partial dependencies moves the design to **second normal form (2NF)**. These steps use the one-enrollment-per-student-and-course rule from Lesson 6.

### Step 3: Department facts belong to Department — 3NF

Suppose Course temporarily contains:

| course_id | department_id | department_name |
| --- | --- | --- |
| C101 | D10 | Computing |
| C102 | D10 | Computing |

The department name depends on `department_id`. Store that name in Department and keep only the department reference in Course.

This removes the indirect dependency and gives us **third normal form (3NF)** for our example. The result is the four-table model from Lesson 8. We can reconstruct an enrollment's details by following its student and course references, then the course's department reference.

### Try it

Computing is renamed Computing and Data. In the final design, which record changes? Should the repeated D10 references be removed from Course?

<details>
<summary>Check your answer</summary>

Update D10's name in Department. Keep D10 in both Course records: repeated references correctly describe the relationship. Normalization does not mean removing every repeated value.

</details>

**Ready to move on when:** you can explain why student names belong to Student and department names belong to Department. Understand that reasoning before memorising the normal-form labels.

<details>
<summary>Extra reading — open when you want more detail</summary>

## Trade-offs

Separate tables reduce inconsistent descriptions, but a combined view must follow relationships. Normalization alone does not guarantee faster queries. Performance decisions come after we can describe the data correctly.

## Common mistakes

- Removing useful repeated foreign-key values.
- Adding a generated ID and assuming all inappropriate dependencies disappear.
- Applying these simplified steps to every possible schema without checking its possible unique identifiers, called candidate keys. Our example assumes the enrollment pair is the only candidate key of the flat enrollment table.

## Interview questions

**Can normalization recover a student missing from the input?** No. It reorganises known facts; it cannot invent absent records.

## References

Adrienne Watt and Nelson Eng (2014), *Database Design – 2nd Edition*, textbook, BCcampus, Victoria, BC. [Official publisher edition](https://opentextbc.ca/dbdesign01/) and [Chapter 12: Normalization](https://opentextbc.ca/dbdesign01/chapter/chapter-12-normalization/). Introductory normalization; CC BY 4.0; checked 21 October 2026. The book uses simplified primary-key explanations in places.

The [reference handbook's normalization section](../00-before-sql.md#11-dependencies-anomalies-and-normalization) distinguishes candidate keys and gives the more general definitions. It is optional depth after this example.

</details>

[← Previous](08-draw-the-model.md) · **[Next lesson: Finish your first design →](10-finish-your-first-design.md)**
