# Phase 01 · Part 1 — Learn SQL with a Training Center Database

A training center runs workshops for several cohorts. Learners join a cohort, can have a mentor, and may attempt the same workshop more than once. Build the database first. Then use the same data to answer real questions, run reports and handle changes.

Work through the scenarios in order. Each one gives you a new job to do. Write the SQL yourself, compare the result with the check, and add an extra edge case. Keep `01-schema.sql`, `02-seed.sql` and `practice.sql` in your own repository. Use SQL comments to explain any decision that might surprise a reviewer. Keep the starting data unchanged so both students can compare answers.

## Scenario 1 · Open the training center

1. Create a local PostgreSQL database named `training_center` and connect to it. Confirm the connection with `current_database()`. PostgreSQL selects a database when you connect; in `psql`, you can switch with `\connect`.
2. Sketch the relationships. A cohort has many learners. A learner can mentor other learners. Each attempt belongs to one learner and one workshop.
3. Create the tables in the order below. Use `integer` for IDs and whole numbers, `text` for names and email addresses, and `date` for an attempt date. Every column is required except `mentor_id`.
4. Run the sample inserts, then check the row count in each table. The expected counts are **3 cohorts, 5 learners, 4 workshops and 9 attempts**.

| Order | Table | Columns and rules |
| --- | --- | --- |
| 1 | `cohorts` | `id` primary key; `name` unique. |
| 2 | `learners` | `id` primary key; `name`; `email` unique; `cohort_id` references `cohorts.id`; optional `mentor_id` references `learners.id`. |
| 3 | `workshops` | `id` primary key; `title`; `track` such as `SQL` or `Django`. |
| 4 | `attempts` | `id` primary key; `learner_id` and `workshop_id` are foreign keys; `attempted_on`; `score` between 0 and 100; `minutes_spent` greater than 0. A learner can attempt a workshop more than once. |

Start with this example and write the other three tables yourself:

```sql
CREATE TABLE cohorts (
    id integer PRIMARY KEY,
    name text NOT NULL UNIQUE
);
```

Once the four tables exist, load this data:

```sql
INSERT INTO cohorts VALUES (1, 'Cedar'), (2, 'Maple'), (3, 'Pine');
INSERT INTO learners VALUES
    (1, 'Ada', 'ada@example.test', 1, NULL),
    (2, 'Bina', 'bina@example.test', 1, 1),
    (3, 'Chen', 'chen@example.test', 2, 1),
    (4, 'Dara', 'dara@example.test', 2, NULL),
    (5, 'Eli', 'eli@example.test', 1, 1);
INSERT INTO workshops VALUES
    (10, 'Filtering', 'SQL'),
    (20, 'Joins', 'SQL'),
    (30, 'Models', 'Django'),
    (40, 'Testing', 'Django');
INSERT INTO attempts VALUES
    (101, 1, 10, '2026-01-01', 70, 20),
    (102, 1, 10, '2026-01-03', 90, 35),
    (103, 1, 20, '2026-01-03', 85, 25),
    (104, 2, 10, '2026-01-02', 65, 15),
    (105, 2, 20, '2026-01-04', 80, 40),
    (106, 3, 20, '2026-01-02', 80, 30),
    (107, 3, 30, '2026-01-04', 95, 20),
    (108, 4, 30, '2026-01-04', 95, 25),
    (109, 4, 10, '2026-01-05', 60, 10);
```

**Check:** Try a missing required name, a duplicate email, a nonexistent learner ID on an attempt, and a score of 101. Each should be rejected. Explain why `learners.email` is an alternate key, and why `(learner_id, workshop_id)` cannot be the primary key of `attempts`.

## Scenario 2 · Register a learner and correct a score

The coordinator needs to add records, fix mistakes and undo a practice session.

1. Read Ada's row by ID. Start a transaction. Insert a practice learner with a column list, then insert two attempts for that learner in one statement.
2. Complete the correction below inside a transaction. Check each affected row before deciding whether to commit or roll back.
3. Use a savepoint before an invalid update. After PostgreSQL rejects the update, roll back to the savepoint and show that the transaction can continue. Roll back the whole exercise to keep the fixtures unchanged.

| # | Skill | Task | Expected result |
| --- | --- | --- | --- |
| 19 | Data changes and rollback | In a transaction, insert a second Filtering attempt for Bina, update its score to 88 and delete her older Filtering attempt. Verify the result and roll back. | Use ID 110 for the new row. Before rollback: (110, 88). After rollback: (104, 65). |

**Learn:** `SELECT`, `INSERT`, multi-row inserts, `UPDATE`, `DELETE`, `WHERE`, transactions and savepoints.

## Scenario 3 · Find the rows the coordinator needs

The coordinator wants a short scoreboard, not the whole attempts table.

| Task | Expected result |
| --- | --- |
| Show the distinct workshop tracks in alphabetical order. | Django, SQL |
| Show the three highest scores. Break ties with the lowest attempt ID. Then fetch the next three rows with the same ordering. | First page: 107, 108, 102. Second page: 103, 105, 106. |
| Find learners without a mentor and attempts whose score is different from 80. Return two separate lists in ID order. | Learners: 1, 4. Attempts: 101, 102, 103, 104, 107, 108, 109. |
| Show attempts in workshops 10 or 30 that scored from 90 through 100. Give the output columns readable aliases. | 102, 107, 108 |

| # | Skill | Task | Expected result |
| --- | --- | --- | --- |
| 01 | Filtering, comparisons, sorting | From January 2 through January 4 inclusive, return attempts scoring at least 80. Sort by score descending, then attempt ID ascending. | `attempt_id`: 107, 108, 102, 103, 105, 106 |

**Learn:** projection, aliases, comparisons, `AND`, `OR`, `NOT`, `IN`, `BETWEEN`, `IS NULL`, `DISTINCT`, `ORDER BY`, `LIMIT` and `OFFSET`.

## Scenario 4 · Connect learners, workshops and mentoring plans

The coordinator wants to compare what each learner planned to attend with what they actually attempted.

1. Create `enrollments(learner_id, workshop_id, status)`. Use foreign keys and a **composite primary key** on the two IDs. Give `status` a default of `planned`. Insert the pairs `(1,10)`, `(2,30)` and `(5,40)` without specifying a status. Check that all three default to `planned` and a repeated pair is rejected.
2. Compare enrollments with distinct pairs in `attempts` using a full outer join. Expect **1 matched pair, 2 planned-only pairs and 7 attempted-only pairs**. Use a right join and then an equivalent left join to list workshops without an attempt. Both should return workshop 40.
3. Build a checklist of every cohort and workshop combination with a cross join. Expect **12 rows**. Show each learner beside their mentor with a self join, keeping unmentored learners.

| # | Skill | Task | Expected result |
| --- | --- | --- | --- |
| 02 | Boolean logic, nulls, text matching | Return learners in Cedar with a mentor, plus unmentored learners in Maple. Keep only emails ending in `@example.test`. | `learner_id`: 2, 4, 5 |
| 03 | Inner join | List learner and workshop names for attempts made on January 3, one row per attempt. | `attempt_id, learner, workshop`: (102, Ada, Filtering), (103, Ada, Joins) |

**Learn:** inner, left, right, full, cross and self joins; composite keys; defaults; `LIKE` patterns and grouped Boolean conditions.

## Scenario 5 · Build the weekly report

The training lead wants to find busy workshops, learners who need help and dates with heavy activity.

| # | Skill | Task | Expected result |
| --- | --- | --- | --- |
| 04 | Outer join, zero counts | Count attempts per workshop and retain workshops with zero attempts. | `workshop_id, attempts`: (10, 4), (20, 3), (30, 2), (40, 0) |
| 05 | Self join, grouping, HAVING | Return mentors with at least two direct mentees and show each count. | `mentor_id, mentees`: (1, 3) |
| 06 | Conditional aggregation | For every learner, report the percentage of attempts scoring at least 80. Return 0.00 for a learner with no attempts. | `learner_id, pass_pct`: (1, 66.67), (2, 50.00), (3, 100.00), (4, 50.00), (5, 0.00) |
| 07 | Distinct counts, groups | Find learners who attempted at least two distinct SQL workshops. Multiple attempts at one workshop count once. | `learner_id, coverage`: (1, 2), (2, 2) |
| 08 | Aggregate totals, grouped dates | Return total minutes per attempt date over January 1–5. | `day, total_minutes`: (Jan 1, 20), (Jan 2, 45), (Jan 3, 60), (Jan 4, 85), (Jan 5, 10) |

Also show `MIN`, `MAX` and `AVG` scores per workshop, rounded to two decimals. Workshop 10 should show **60, 90 and 71.25**. Keep workshop 40 with a zero count and null score statistics. Add a `CASE` label of `Pass` for scores of 80 or higher and `Review` otherwise. Check that an exact score of 80 passes.

**Learn:** aggregation, grouping, `HAVING`, filtered counts, decimal division, rounding, `CASE`, `COUNT(*)` versus `COUNT(column)`.

## Scenario 6 · Find gaps without counting duplicates

The lead wants to know who missed a track and who completed the full SQL workshop set.

| # | Skill | Task | Expected result |
| --- | --- | --- | --- |
| 09 | Anti-join, NOT EXISTS | Find learners who never attempted a Django workshop. Include learners who never attempted any workshop. | `learner_id`: 1, 2, 5 |
| 10 | Relational coverage, subqueries | Find learners who attempted every SQL workshop. Make the result still work when a third SQL workshop is added. | `learner_id`: 1, 2 |
| 11 | Subquery, second distinct value | For each workshop, show its second-highest distinct score. Keep workshops without two distinct scores and return NULL for their score. | `workshop_id, second_score`: (10, 70), (20, 80), (30, NULL), (40, NULL) |
| 17 | UNION vs UNION ALL | Combine a list of learners who scored at least 85 with a list of learners who attempted a Django workshop. First return unique IDs, then keep one row per matching learner per list. | Unique: 1, 3, 4. With duplicates: 1, 3, 3, 4, 4 |

| Extra task | Expected result |
| --- | --- |
| Compare learners who attempted Filtering with learners who attempted Joins. Use `INTERSECT` for both and `EXCEPT` for Filtering only. | Both: 1, 2. Filtering only: 4. |
| Find attempts that scored higher than **any** Joins score, then higher than **all** Joins scores. Use strict greater-than comparisons. | Any: 102, 103, 107, 108. All: 102, 107, 108. |

**Learn:** nested and correlated subqueries, `EXISTS`, `NOT EXISTS`, `ANY`, `ALL`, `UNION`, `UNION ALL`, `INTERSECT`, `EXCEPT`. Explain what a null in a subquery can do to `NOT IN`.

## Scenario 7 · Prepare clean data for a dashboard

The dashboard needs readable names, valid dates and a few optional details from an import.

| # | Skill | Task | Expected result |
| --- | --- | --- | --- |
| 18 | String cleanup and aggregation | Build a roster for each cohort with lowercase learner names in alphabetical order, separated by commas. Return an empty string for an empty cohort. | `cohort_id, roster`: (1, "ada,bina,eli"), (2, "chen,dara"), (3, "") |

1. Clean the sample value `'  Ada  '` with `LTRIM` and `RTRIM`. Show the cleaned name, its uppercase version, and the email domain from Ada's record. Check valid email shape with a simple regular expression, then test a clearly invalid value.
2. Use January 5, 2026 as the report date. For attempt 101, show the elapsed days, the report month, and score divided by 100 as a decimal. Expect **4 days, January 2026 and 0.70**.
3. Put `{"source":"import","retry":true}` into a `jsonb` column in a scratch import table. Read both keys, filter rows marked as retries and handle a row with a missing `source` key.
4. Make a **wide** report with SQL and Django attempt counts side by side per learner. Then return those counts as separate rows. Ada should show **3 SQL attempts and 0 Django attempts** either way.

**Learn:** string and date functions, regular expressions, numeric calculations, casts, JSON extraction, `COALESCE`, pivot-style and unpivot-style results.

## Scenario 8 · Compare attempts over time

The lead needs the latest attempt, gaps between attempts, ties and running totals.

| # | Skill | Task | Expected result |
| --- | --- | --- | --- |
| 12 | CTE, ROW_NUMBER, ties | Find the latest attempt per learner. If dates tie, choose the larger attempt ID. Keep learners with at least one attempt. | `learner_id, attempt_id`: (1, 103), (2, 105), (3, 107), (4, 109) |
| 13 | LAG, gap calculation | Return attempts made more than one day after the same learner's immediately preceding attempt. Order each learner's attempts by date and ID before finding the prior row. | `attempt_id, gap_days`: (102, 2), (105, 2), (107, 2) |
| 14 | DENSE_RANK, ties | Return every learner tied for the highest score in each workshop that has attempts. Return each learner once per workshop. | `workshop_id, learner_id, score`: (10, 1, 90), (20, 1, 85), (30, 3, 95), (30, 4, 95) |
| 15 | Running sum, window frames | Make a queue from Ada's attempts ordered by date and ID. Return the last attempt within a 55-minute cumulative budget. | `attempt_id, cumulative_minutes`: (102, 55) |
| 16 | Date windows, weighted logic | First sum minutes per day, then report the average daily total over the current day and the preceding two calendar days ending January 3–5. Assume the fixture covers all dates in that range. | `day, avg_daily_minutes`: (Jan 3, 41.67), (Jan 4, 63.33), (Jan 5, 51.67) |

**One more task:** In a transaction, make a temporary learner mentored by Bina. Use a recursive CTE to show Ada's mentoring tree with depth. Ada is at depth 0, Bina at depth 1 and the temporary learner at depth 2. Roll back your new row. Explain how you would prevent the recursion from following a cycle.

**Learn:** `WITH`, recursive CTEs, `ROW_NUMBER`, `LAG`, `DENSE_RANK`, partitions and window frames. In the rolling average, explain why three rows are only equivalent to three calendar days when each date has a row.

## Scenario 9 · Repair a messy import without losing data

A spreadsheet has extra copies of the same registration and repeats cohort names on every row.

1. In a scratch copy, import a few rows with PostgreSQL `COPY` or `psql`'s `\copy`. Create a temporary table with an import ID, learner ID, workshop ID and an optional cohort name. Use an identity column or an explicit sequence for import IDs and explain the difference from the fixture's manually chosen IDs.
2. Load the pair `(1,10)` twice into the scratch table. Keep its earliest import ID and delete the other copy. Practice an `UPDATE ... FROM` to fill cohort names from a lookup table and a `DELETE ... USING` to remove scratch rows whose IDs appear in a separate rejection list. Check the affected rows before committing.
3. Sketch the flat import and the normalized tables. List dependencies such as `learner_id → learner_name, cohort_id` and `cohort_id → cohort_name`. Trace what a learner ID determines, identify partial and transitive dependencies where they apply, and explain how the current design reaches 3NF. Identify one repeated value you might keep in a reporting snapshot and what could make it stale.
4. Copy a table with `CREATE TABLE AS`. In the copy, add a column, rename the table, clear its rows with `TRUNCATE` and drop it. Compare those effects with `DELETE`. Practice creating, renaming and dropping a separate disposable database while connected to a different database.

**Learn:** imports, duplicate cleanup, joined updates and deletes, identity/sequence, ER modeling, functional dependencies, normalization and schema changes.

## Scenario 10 · Publish the report and check its performance

1. Create a view for the report that counts attempts per workshop. Query it, replace its definition with a compatible change, rename it and drop it when finished. Separately try updating through a simple single-table view in a transaction and explain why the aggregated report view is different.
2. Add enough generated attempt rows to a scratch dataset to test a date-range query for one learner. Capture its plan with `EXPLAIN`, then create an index on `(learner_id, attempted_on)` and run the same query again. List indexes and remove the scratch index after comparing plans.
3. Find the unique index behind the email constraint and explain what makes it different from the report index. Explain how PostgreSQL's one-time `CLUSTER` operation differs from ordinary index lookups. The planner may still choose a sequential scan on small tables.

**Learn:** views, index types and uniqueness, execution plans and basic SQL tuning.

## Scenario 11 · Make routine updates safe

1. In the scratch schema, add an audit table and a trigger that records an attempt ID, old score and new score when the score changes. Write a stored procedure that corrects a score. Call it on a scratch attempt and check for exactly one audit row.
2. Roll back a valid correction and confirm the score change and audit row both disappear. Try a score of 101 and confirm there is no partial update.
3. Iterate through workshop counts once with a cursor, then produce the same output with a single set-based query. Explain which version you would keep for this report.

**Learn:** stored procedures, triggers, cursors, atomicity and rollback.

## Scenario 12 · Hand over the database

1. Write a small parameterized report query that accepts a cohort name and date range from an application. If users can choose the sort order, map their input to a fixed list of allowed columns. Explain how this prevents SQL injection and why choosing a column differs from binding a value.
2. Give a demo reporting role read access to a test report, verify it cannot change attempt scores, and revoke access. Describe what you would protect with TLS in transit and encryption at rest, including backups.
3. Create a custom-format dump of the sample database with `pg_dump` and restore it into a different local database with `pg_restore`. Verify row counts and rerun the workshop and attempt reports. Explain what changes when the database moves from a local setup to a managed host.
4. Explain how the next Django project will use an ORM to perform operations against tables like these. Identify where a database driver or ODBC fits and how that differs from an ODM used with documents.

**Learn:** least privilege, parameterized queries, encryption, backup and recovery, hosting basics and application connectivity.

## Interview practice and completion

- Complete the scenario queries independently. Keep the sample checks and add your own tests for nulls, empty groups, duplicate rows and ties.
- After the scenarios, submit all **50** problems in [SQL 50](https://leetcode.com/studyplan/top-sql-50/) through your own account and record **50 accepted results**.
- In review, explain a join, an aggregate and a window or subquery before solving one unseen variation. Then continue to [Part 2 — Django Models Project](django-models/README.md).
