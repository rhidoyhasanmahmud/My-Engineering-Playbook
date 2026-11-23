# Phase 01 · Part 1 — SQL Foundations and Interview Practice

Learn SQL on a small training database. Solve each original problem before attempting the corresponding section of SQL 50. After completing the SQL work, continue to [Part 2 — Django Models Project](django-models/README.md).

## How to work

1. Read the schema, task and expected output. Research any unfamiliar SQL concept.
2. Write a query locally in PostgreSQL. Check it against the sample rows, then add an edge case that could break it.
3. Submit your own solutions for all 50 problems in the [SQL 50 study plan](https://leetcode.com/studyplan/top-sql-50/). Use a SQL dialect accepted by the platform and its exact output requirements.
4. Keep an individual log of the problem, SQL pattern, submission result and any mistake you corrected. Keep your original practice solutions in numbered SQL files or one `practice.sql`.

## Run this fixture

Run this once in an empty practice database. Use IDs as the sort order unless a problem specifies a different order. Display rates and averages rounded to two decimal places where requested.

```sql
CREATE TABLE cohorts (
    id integer PRIMARY KEY,
    name text NOT NULL UNIQUE
);

CREATE TABLE learners (
    id integer PRIMARY KEY,
    name text NOT NULL,
    email text NOT NULL,
    cohort_id integer NOT NULL REFERENCES cohorts(id),
    mentor_id integer REFERENCES learners(id)
);

CREATE TABLE workshops (
    id integer PRIMARY KEY,
    title text NOT NULL,
    track text NOT NULL
);

CREATE TABLE attempts (
    id integer PRIMARY KEY,
    learner_id integer NOT NULL REFERENCES learners(id),
    workshop_id integer NOT NULL REFERENCES workshops(id),
    attempted_on date NOT NULL,
    score integer NOT NULL CHECK (score BETWEEN 0 AND 100),
    minutes_spent integer NOT NULL CHECK (minutes_spent > 0)
);

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

## Original practice problems

| # | Skill | Problem | Expected output on the fixture |
| --- | --- | --- | --- |
| 01 | Filtering, comparisons, sorting | From January 2 through January 4 inclusive, return attempts scoring at least 80. Sort by score descending, then attempt ID ascending. | `attempt_id`: 107, 108, 102, 103, 105, 106 |
| 02 | Boolean logic, nulls, text matching | Return learners in Cedar with a mentor, plus unmentored learners in Maple. Keep only emails ending in `@example.test`. | `learner_id`: 2, 4, 5 |
| 03 | Inner join | List learner and workshop names for attempts made on January 3, one row per attempt. | `attempt_id, learner, workshop`: (102, Ada, Filtering), (103, Ada, Joins) |
| 04 | Outer join, zero counts | Count attempts per workshop and retain workshops with zero attempts. | `workshop_id, attempts`: (10, 4), (20, 3), (30, 2), (40, 0) |
| 05 | Self join, grouping, HAVING | Return mentors with at least two direct mentees and show each count. | `mentor_id, mentees`: (1, 3) |
| 06 | Conditional aggregation | For every learner, report the percentage of attempts scoring at least 80. Return 0.00 for a learner with no attempts. | `learner_id, pass_pct`: (1, 66.67), (2, 50.00), (3, 100.00), (4, 50.00), (5, 0.00) |
| 07 | Distinct counts, groups | Find learners who attempted at least two distinct SQL workshops. Multiple attempts at one workshop count once. | `learner_id, coverage`: (1, 2), (2, 2) |
| 08 | Aggregate totals, grouped dates | Return total minutes per attempt date over January 1–5. | `day, total_minutes`: (Jan 1, 20), (Jan 2, 45), (Jan 3, 60), (Jan 4, 85), (Jan 5, 10) |
| 09 | Anti-join, NOT EXISTS | Find learners who never attempted a Django workshop. Include learners who never attempted any workshop. | `learner_id`: 1, 2, 5 |
| 10 | Relational coverage, subqueries | Find learners who attempted every SQL workshop. Make the result still work when a third SQL workshop is added. | `learner_id`: 1, 2 |
| 11 | Subquery, second distinct value | For each workshop, show its second-highest distinct score. Keep workshops without two distinct scores and return NULL for their score. | `workshop_id, second_score`: (10, 70), (20, 80), (30, NULL), (40, NULL) |
| 12 | CTE, ROW_NUMBER, ties | Find the latest attempt per learner. If dates tie, choose the larger attempt ID. Keep learners with at least one attempt. | `learner_id, attempt_id`: (1, 103), (2, 105), (3, 107), (4, 109) |
| 13 | LAG, gap calculation | Return attempts made more than one day after the same learner's immediately preceding attempt. Order each learner's attempts by date and ID before finding the prior row. | `attempt_id, gap_days`: (102, 2), (105, 2), (107, 2) |
| 14 | DENSE_RANK, ties | Return every learner tied for the highest score in each workshop that has attempts. Return each learner once per workshop. | `workshop_id, learner_id, score`: (10, 1, 90), (20, 1, 85), (30, 3, 95), (30, 4, 95) |
| 15 | Running sum, window frames | Make a queue from Ada's attempts ordered by date and ID. Return the last attempt within a 55-minute cumulative budget. | `attempt_id, cumulative_minutes`: (102, 55) |
| 16 | Date windows, weighted logic | First sum minutes per day, then report the average daily total over the current day and the preceding two calendar days ending January 3–5. Assume the fixture covers all dates in that range. | `day, avg_daily_minutes`: (Jan 3, 41.67), (Jan 4, 63.33), (Jan 5, 51.67) |
| 17 | UNION vs UNION ALL | Combine a list of learners who scored at least 85 with a list of learners who attempted a Django workshop. First return unique IDs, then keep one row per matching learner per list. | Unique: 1, 3, 4. With duplicates: 1, 3, 3, 4, 4 |
| 18 | String cleanup and aggregation | Build a roster for each cohort with lowercase learner names in alphabetical order, separated by commas. Return an empty string for an empty cohort. | `cohort_id, roster`: (1, "ada,bina,eli"), (2, "chen,dara"), (3, "") |
| 19 | Data changes and rollback | In a transaction, insert a second Filtering attempt for Bina, update its score to 88 and delete her older Filtering attempt. Verify the result and roll back. | Use ID 110 for the new row. Before rollback: (110, 88). After rollback: (104, 65). |

Work through **01–03** before basic selects and joins, **04–08** before aggregation and grouping, **09–11** before subqueries, and **12–18** before advanced joins, ranking, date windows and string problems. Use **19** to practice data changes against a disposable database.

## Move to Part 2 when

- Each student has solved the original practice set independently and tested extra cases for nulls, ties and duplicate rows.
- Each student has submitted all **50** study-plan problems under their own account and recorded **50 accepted results**.
- Each student can explain a join, an aggregate and a window or subquery solution, then solve one unseen variation without a prepared answer.
