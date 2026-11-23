# Phase 01 — Django Models and PostgreSQL

**Project:** Helpdesk Ticket System  
**Goal:** Build the Helpdesk data layer and use it to practice Django models, PostgreSQL and interview-style SQL. Each student moves to Phase 02 after completing the checks below.

Use the [W3Schools SQL tutorial](https://www.w3schools.com/sql/) as a topic checklist. Run exercises in PostgreSQL and follow its syntax, such as `LIMIT` for the tutorial's SELECT TOP topic. Use Django shell for ORM practice and a disposable PostgreSQL database for DDL and destructive exercises.

## Feature and learning map

| Feature to build | Django practice | PostgreSQL practice |
| --- | --- | --- |
| **F01 · Record a ticket** with title, status, requester and creation time | Fields, choices, defaults, user foreign key and migrations. [Model fields](https://docs.djangoproject.com/en/6.1/ref/models/fields/) · [Migrations](https://docs.djangoproject.com/en/6.1/topics/migrations/) | Read generated DDL with `sqlmigrate`. In a scratch schema, create a practice table, add a column, insert rows, update one status, delete one seed row, then reset the table. [DDL](https://www.postgresql.org/docs/current/ddl.html) · [Data manipulation](https://www.postgresql.org/docs/current/dml.html) · [TRUNCATE](https://www.postgresql.org/docs/current/sql-truncate.html) |
| **F02 · Categorize and assign tickets** with an optional agent | Foreign keys, reverse relations, nullable fields, `on_delete` and constraints. [Relationships](https://docs.djangoproject.com/en/6.1/topics/db/examples/many_to_one/) · [Constraints](https://docs.djangoproject.com/en/6.1/ref/models/constraints/) | Verify primary and foreign keys, unique category names, required fields, defaults and a status check constraint. List unassigned tickets using `IS NULL`; show requester and assigned agent by joining the user table twice. [Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) · [Joins](https://www.postgresql.org/docs/current/tutorial-join.html) |
| **F03 · Store comments and build a ticket timeline** | Reverse lookups, `on_delete`, related loading and combining query results. [Making queries](https://docs.djangoproject.com/en/6.1/topics/db/queries/) · [QuerySet API](https://docs.djangoproject.com/en/6.1/ref/models/querysets/) | Retrieve comments with author aliases. Combine ticket creation and comments into one timeline using `UNION ALL`; compare with `UNION`. [Combining queries](https://www.postgresql.org/docs/current/queries-union.html) |
| **F04 · Search and filter the ticket queue** | Field lookups, `Q` objects, stable ordering, slicing and a composite index. [Making queries](https://docs.djangoproject.com/en/6.1/topics/db/queries/) · [Model indexes](https://docs.djangoproject.com/en/6.1/ref/models/indexes/) | Search titles with `LIKE` or PostgreSQL `ILIKE`; combine status, priority and date filters using `AND`, `OR`, `NOT`, `IN` and a date range. Practice `DISTINCT`, `ORDER BY` and `LIMIT`. Compare plans with `EXPLAIN` before and after indexing. [SELECT](https://www.postgresql.org/docs/current/sql-select.html) · [Pattern matching](https://www.postgresql.org/docs/current/functions-matching.html) · [EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) |
| **F05 · Report on category and agent workload** | `annotate()`, filtered aggregations, `Exists`, `Subquery`, `Case` and `Coalesce`. [Aggregation](https://docs.djangoproject.com/en/6.1/topics/db/aggregation/) · [Expressions](https://docs.djangoproject.com/en/6.1/ref/models/expressions/) · [Database functions](https://docs.djangoproject.com/en/6.1/ref/models/database-functions/) | Use `LEFT JOIN` and `COUNT` to include empty categories. Use `GROUP BY` and `HAVING` for categories with at least three tickets. Report `MIN`, `MAX`, `SUM` and `AVG` of estimated effort by agent. Find categories without open tickets using `NOT EXISTS`. Use `CASE` for workload labels, `COALESCE` for missing totals and a view for the workload report. [Aggregate functions](https://www.postgresql.org/docs/current/functions-aggregate.html) · [Subqueries](https://www.postgresql.org/docs/current/functions-subquery.html) · [Conditional expressions](https://www.postgresql.org/docs/current/functions-conditional.html) · [Views](https://www.postgresql.org/docs/current/sql-createview.html) |

Use fixtures with an empty category, an unassigned ticket, a ticket with zero comments, multiple comments on one ticket, and two tickets with the same timestamp. Give tickets a priority and an optional estimated effort in minutes for queue and reporting exercises.

For the remaining W3Schools join and subquery topics, use the same dataset. Compare `RIGHT JOIN` with an equivalent `LEFT JOIN`; compare two agent queues with `FULL OUTER JOIN`; find pairs of tickets from the same requester with a self join; find agents whose ticket exceeds every estimate in a comparison set with `> ALL`, and repeat with `> ANY`. Use `INSERT INTO ... SELECT` and `CREATE TABLE ... AS SELECT` to copy a report into a scratch snapshot. [Table expressions](https://www.postgresql.org/docs/current/queries-table-expressions.html) · [Subqueries](https://www.postgresql.org/docs/current/functions-subquery.html) · [INSERT](https://www.postgresql.org/docs/current/sql-insert.html) · [CREATE TABLE AS](https://www.postgresql.org/docs/current/sql-createtableas.html)

W3Schools includes database-specific syntax. Compare SQL Server `TOP`, `IDENTITY`, `SELECT INTO` and stored procedures with PostgreSQL equivalents. Practice PostgreSQL identity columns and write a small read-only procedure exercise that reports how many open tickets a given agent has. [Identity columns](https://www.postgresql.org/docs/current/ddl-identity-columns.html) · [CREATE PROCEDURE](https://www.postgresql.org/docs/current/sql-createprocedure.html)

## Interview practice

1. List every ticket and its comment count. Why does `COUNT(*)` give the wrong result for some tickets after a left join?
2. Find requesters with at least three open tickets created in the last 30 days. Which condition belongs in `WHERE` and which belongs in `HAVING`?
3. Return the latest ticket per requester, breaking ties by ticket ID. Solve it with a window function or PostgreSQL `DISTINCT ON`. [Window functions](https://www.postgresql.org/docs/current/tutorial-window.html) · [SELECT](https://www.postgresql.org/docs/current/sql-select.html)
4. Find categories without open tickets. What happens to a `NOT IN` check if its subquery returns a null?
5. Joining comments inflated the total estimated effort per agent. Explain why and correct the report.
6. A queue query slows down as ticket count grows. Show its query plan and explain whether your index helped.

## SQL 50-inspired Helpdesk challenges

Use the existing Helpdesk schema and fixtures. Write PostgreSQL queries for the outputs below. The [LeetCode SQL 50 study plan](https://leetcode.com/studyplan/top-sql-50/) is a source of practice patterns.

| Feature | Challenge and expected output | SQL pattern | Inspiration |
| --- | --- | --- | --- |
| F02 · Categories | List every category that has never received a ticket. Return category ID and name. Compare `NOT EXISTS` with a left join. | Anti-join | [Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/) |
| F03 · Comments | For each ticket with comments, return the date of its first comment and the number of comments posted on that date. Include ties on the first date. | Grouped minimum, join back and aggregation | [Product Sales Analysis III](https://leetcode.com/problems/product-sales-analysis-iii/) |
| F04 · SLA queue | Find open tickets created yesterday whose priority exceeds the priority of the previous ticket from the same requester. Exclude tickets with no predecessor. Find the predecessor before applying the date and status filters. Break timestamp ties by ticket ID. | `LAG()`, partitioning and filter order | [Rising Temperature](https://leetcode.com/problems/rising-temperature/) |
| F05 · Agent workload | For every agent with assigned tickets, return the share of assigned tickets that are resolved, rounded to two decimals. Keep agents whose share is zero. | Conditional aggregation, decimal division and rounding | [Confirmation Rate](https://leetcode.com/problems/confirmation-rate/) |
| F05 · Effort report | Return the second-highest **distinct** estimated effort across all tickets. Return one row with `NULL` if fewer than two distinct non-null values exist. | `DISTINCT`, scalar result and missing values | [Second Highest Salary](https://leetcode.com/problems/second-highest-salary/) |
| F05 · Staffing | Ignore tickets with unknown effort. Order the open queue by priority descending, then creation time and ID ascending. With a 120-minute budget, return the last ticket in the longest prefix that fits, plus the cumulative effort at that point. | Running sum and deterministic ordering | [Last Person to Fit in the Bus](https://leetcode.com/problems/last-person-to-fit-in-the-bus/) |

Add rows for the edge cases before running each challenge. Keep solutions in each student's own `practice.sql`.

## Completion criteria

- Each student reviews the shared schema and can explain its relationships and constraints.
- Each student submits their own `practice.sql` and `orm_examples.py`. For reads with a natural ORM equivalent, verify that SQL and ORM agree against the same sample data. Use direct SQL for database exercises such as DDL and views.
- Demonstrate migrations on an empty database and show the edge cases in the fixtures.
- Independently solve and explain one unseen Helpdesk query during review.
