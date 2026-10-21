# Database foundations: before SQL

[All roadmaps](README.md) · [Comprehensive note](../notes/database-engineering/00-before-sql.md) · [Practice worksheet](../practice/database-design/before-sql-capstone.md)

**Goal:** Start with “What is a database?” and finish able to design and explain a small relational model before writing SQL.

**Prerequisites:** Familiarity with everyday applications or spreadsheets. No programming, SQL, database installation or paid course is required.

**Materials:** One comprehensive note follows the seven-section study format. A separate worksheet includes an answer guide. Read the note in stages rather than trying to memorise it in one sitting.

## Scope and boundary

| Included in this foundation | Continue with later |
| --- | --- |
| Data, metadata, databases, DBMS and RDBMS | Database installation and engine-specific configuration |
| Files, spreadsheets and common data models | Detailed product selection and storage architecture |
| Tables, schema, types, missing values and keys | SQL statements, filtering, joins and aggregation |
| Constraints, relationships and ER modelling | Executable schema definitions and migrations |
| Dependencies, anomalies and normalization through 3NF | Formal decomposition proofs, BCNF and higher normal forms |
| CRUD, transactions, permissions and recovery at awareness level | Isolation experiments, indexing, query plans and operations |

You do not need to master advanced internals before beginning SQL. The finish line here is a coherent model and an explanation of its rules.

## Learning sequence

Each row is a study session or a group of shorter sessions. Move on when you can complete the checkpoint; the numbering is a sequence, not a deadline. **Structured** describes content availability, not your completion status.

| Step | Focus and reading | Practical checkpoint | Content |
| --- | --- | --- | --- |
| 1 | [Data, information and metadata](../notes/database-engineering/00-before-sql.md#1-data-information-and-metadata) and [database vocabulary](../notes/database-engineering/00-before-sql.md#2-database-dbms-rdbms-and-sql) | Explain database, DBMS, RDBMS and SQL in your own words; label data and metadata in a student list | Structured |
| 2 | [Files and spreadsheets](../notes/database-engineering/00-before-sql.md#3-files-spreadsheets-and-databases) and [common data models](../notes/database-engineering/00-before-sql.md#4-common-data-models) | Give one case where a spreadsheet is sufficient and one where coordinated database access helps | Structured |
| 3 | [Tables, entities and schema](../notes/database-engineering/00-before-sql.md#5-tables-entities-and-schema) | State the meaning of one row in Student, Course and Enrollment; distinguish a schema change from a data change | Structured |
| 4 | [Types, domains and missing values](../notes/database-engineering/00-before-sql.md#6-data-types-domains-and-missing-values) | Choose conceptual types for an identifier, phone, quantity, money amount and date; explain missing versus zero | Structured |
| 5 | [Keys and identity](../notes/database-engineering/00-before-sql.md#7-keys-and-identity) | Find candidate, primary, composite and foreign keys; explain why names are unsuitable in this model | Structured |
| 6 | [Constraints](../notes/database-engineering/00-before-sql.md#8-constraints-and-integrity) and [relationships](../notes/database-engineering/00-before-sql.md#9-relationships-cardinality-and-optionality) | State both ends of each relationship, including optionality; identify the rule that rejects a duplicate enrollment | Structured |
| 7 | [Modelling process](../notes/database-engineering/00-before-sql.md#10-from-requirements-to-an-er-diagram) and [worked ER diagram](../notes/database-engineering/00-before-sql.md#worked-er-diagram) | Draw the model from the written business rules before looking at the supplied diagram | Structured |
| 8 | [Dependencies and normal forms](../notes/database-engineering/00-before-sql.md#11-dependencies-anomalies-and-normalization) and [normalization walkthrough](../notes/database-engineering/00-before-sql.md#normalization-walkthrough) | Explain one anomaly and separate the flat enrollment table into four tables while retaining its relationships | Structured |
| 9 | [Operations and reliability](../notes/database-engineering/00-before-sql.md#12-operations-transactions-and-responsible-data-handling) and [predicted changes](../notes/database-engineering/00-before-sql.md#predict-changes-before-learning-sql) | Predict accepted/rejected changes and explain why the last available seat needs coordinated handling | Structured |
| 10 | [Trade-offs](../notes/database-engineering/00-before-sql.md#trade-offs), [common mistakes](../notes/database-engineering/00-before-sql.md#common-mistakes) and [interview questions](../notes/database-engineering/00-before-sql.md#interview-questions) | Defend one design decision and identify the assumption that breaks when retakes are allowed | Structured |
| 11 | [Library-loan capstone](../practice/database-design/before-sql-capstone.md) | Produce a new model, test it with sample records and compare it with the answer guide | Worksheet and answer guide available |

## How to study each step

1. Read the assigned part and write a three-sentence explanation without copying.
2. Draw or modify the running example on paper or in a diagram tool.
3. Test a normal case and an edge case: a duplicate, missing value, invalid reference or record with no dependents.
4. Complete the checkpoint and explain why the result follows from the business rules.
5. Revisit the relevant section if your explanation depends on memorised terms.

Use a personal copy of the [study tracker](../templates/study-tracker.md) for dates and progress. Keep the shared roadmap focused on what material exists.

## Capstone deliverables

The [worksheet](../practice/database-design/before-sql-capstone.md) asks you to design a small library-loan system. Submit these to your own study folder or notes:

- A short statement of scope and business rules.
- A data dictionary with one-row meaning, conceptual types and required fields.
- Keys, relationships and a labelled ER diagram.
- A normalization explanation with one example of each anomaly.
- A small valid dataset and expected outcomes for invalid changes.
- One design trade-off and a response to a changed requirement.

No database server or SQL statements are needed. An explanation that acknowledges a rule it cannot yet enforce is better than claiming an ordinary foreign key solves it.

## Ready to start SQL

Use this as a self-check, not an examination score. Revisit any item you cannot explain using an example.

- [ ] I can distinguish the database, DBMS, data model and SQL language.
- [ ] I can justify whether a simple file/spreadsheet or a DBMS fits a stated need.
- [ ] I can state exactly what one row represents and distinguish schema from stored values.
- [ ] I can choose conceptual types and explain missing values without treating them as zero.
- [ ] I can distinguish candidate, primary, alternate, composite and foreign keys.
- [ ] I can derive uniqueness from business rules rather than from a small sample.
- [ ] I can model one-to-one, one-to-many and many-to-many relationships, including optionality.
- [ ] I can explain required, unique, domain and reference rules and a deletion policy.
- [ ] I can trace 1NF, 2NF and 3NF in the example and reconstruct the original enrollment facts.
- [ ] I can explain why a transaction may need to group related changes.
- [ ] I can complete the library capstone and discuss a changed requirement without copying the example.

## Next learning stage

Continue with the [database engineering roadmap](database-engineering.md). The next practical step is to choose a database engine, create a small schema and learn SQL for reading and changing records. A complete repository SQL introduction is **planned**; the existing exercises are supplemental practice.

The official [PostgreSQL 18 SQL-language tutorial](https://www.postgresql.org/docs/18/tutorial-sql.html) is an available next-stage resource. Its installation prerequisites belong to that next stage. Return to this foundation whenever a query problem is really a modelling problem.
