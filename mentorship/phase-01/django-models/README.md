# Phase 01 · Part 2 — Build a Helpdesk with Django Models

Build a small website where people can report a problem and support agents can fix it. For example, a user opens a ticket called **“I cannot log in.”** An agent finds it in the queue, claims it, adds a comment and marks it as resolved. The support report then shows the ticket as resolved.

**Your main goal is to learn Django models and the ORM.** Each screen gives you a reason to design a model, write a query or enforce a data rule. Use PostgreSQL with simple Django views, forms and templates. Complete [Part 1 — SQL practice](../README.md) first. Use the [Django model-layer docs](https://docs.djangoproject.com/en/6.1/#the-model-layer) for your installed version.

## What you will build

| Screen | What someone can do |
| --- | --- |
| **New Ticket** | Enter a title and description, choose a category and priority, and submit the ticket. |
| **Ticket Queue** | Find open or unassigned tickets, filter the list, and search by ticket reference. |
| **Ticket Detail** | See the requester and assignee, add comments and tags, claim or resolve the ticket, and read its status history. |
| **Support Reports** | See category counts, agent workload, ticket activity, backlog age and agent rankings. |

Build the features below in order. Create categories, tags and demo accounts in Django admin or through sample data.

## 1. Create tickets and connect related data

### F01 · Open a ticket

- **Build in the UI:** Make the **New Ticket** form. After a successful submission, open the new ticket's detail page. Set the requester from the logged-in user.
- **Learn with Django models:** Create `Ticket` and `Category`. Choose field types, status and priority choices, defaults, timestamps and foreign keys. Create and run migrations.
- **Check your work:** Submit a valid ticket, reload its detail page and confirm the data is still there. Use `sqlmigrate` to find the table, primary key and foreign keys.
- **Read:** [Model fields](https://docs.djangoproject.com/en/6.1/ref/models/fields/) · [Migrations](https://docs.djangoproject.com/en/6.1/topics/migrations/)

### F02 · Show who owns a ticket

- **Build in the UI:** On **Ticket Detail**, show the agent's name or **Unassigned**. Add an optional estimated effort in minutes. Show a clear error if the estimate is negative.
- **Learn with Django models:** Link `AgentProfile` one-to-one with a user and link the optional assignee to the ticket. Use database constraints for unique category names and nonnegative estimates. Learn how `blank` differs from `null`.
- **Check your work:** Save a ticket with no assignee and no estimate. Test a blank title with `full_clean()` and with direct `save()`. Test that PostgreSQL rejects a negative estimate or a duplicate category even when the form is bypassed.
- **Read:** [Relationships](https://docs.djangoproject.com/en/6.1/topics/db/models/#relationships) · [Model validation](https://docs.djangoproject.com/en/6.1/ref/models/instances/#validating-objects) · [Constraints](https://docs.djangoproject.com/en/6.1/ref/models/constraints/)

### F03 · Add comments and tags

- **Build in the UI:** On **Ticket Detail**, add a comment and see it in the comment list. Attach an existing tag and show when and by whom it was added.
- **Learn with Django models:** A ticket has many comments and many tags. Use a `TicketTag` through model to store the tag assignment details. Use reverse relations and a unique constraint for each ticket/tag pair.
- **Check your work:** Add the same tag twice and confirm only one link exists. Test that deleting a ticket removes its comments (`CASCADE`), deleting its assignee clears the assignment (`SET_NULL`), and deleting a category in use is blocked (`PROTECT`).
- **Read:** [Many-to-many through models](https://docs.djangoproject.com/en/6.1/topics/db/models/#extra-fields-on-many-to-many-relationships) · [ForeignKey and delete rules](https://docs.djangoproject.com/en/6.1/ref/models/fields/#foreignkey)

## 2. Run the support queue and reports

### F04 · Claim and resolve a ticket

- **Build in the UI:** Add **Claim** and **Resolve** actions on **Ticket Detail**. Claim assigns an unassigned ticket to the current agent. Resolve updates the status and adds an entry to the status history.
- **Learn with Django models:** Use a conditional update or row locking for claims. Use a transaction for the status update and its `StatusChange` record.
- **Check your work:** Have two agents try to claim the same ticket. Exactly one succeeds, and the other sees a clear message. If saving the history fails, the ticket stays in its previous status.
- **Read:** [Transactions](https://docs.djangoproject.com/en/6.1/topics/db/transactions/) · [QuerySet updates and locking](https://docs.djangoproject.com/en/6.1/ref/models/querysets/)

### F05 · Filter the queue

- **Build in the UI:** On **Ticket Queue**, let an agent show open tickets, unassigned tickets or their own tickets. Add priority and date filters. Show the newest tickets first, using ticket ID to break ties.
- **Learn with Django models:** Write reusable QuerySet methods and combine conditions with `Q` objects. Use a manager to expose the queue methods.
- **Check your work:** Combine two filters and compare the ordered results with your SQL query. On sample tickets, also compare a loop using `save()` with one `QuerySet.update()` for the same priority change. Check the query count and whether the model's `save()` runs.
- **Read:** [Queries and Q objects](https://docs.djangoproject.com/en/6.1/topics/db/queries/) · [Managers](https://docs.djangoproject.com/en/6.1/topics/db/managers/) · [Bulk updates](https://docs.djangoproject.com/en/6.1/ref/models/querysets/#update)

### F06 · Build the Support Reports page

Add these five reports in order. Start with a SQL query in PostgreSQL, then build the Django ORM version and show its results in a simple table. Use the same sample data to check that both versions agree.

| Report | What the screen should show | Query practice and checks |
| --- | --- | --- |
| **R01 · Tickets by category** | Show every category with its total, open and resolved ticket counts. | Use an outer join, grouping and conditional counts. A category with no tickets must appear with three zeroes. |
| **R02 · Agent workload and resolution rate** | For every agent, show assigned, open and resolved ticket counts. Show `resolved ÷ assigned × 100` when the agent has assignments. | Use filtered aggregates and decimal division. An agent with assignments but no resolutions shows `0%`. An agent with no assignments shows a dash for the rate. Unassigned tickets do not belong to any agent. |
| **R03 · Ticket activity** | Show each ticket's first comment time and author, comment count and tag count. If two comments have the same time, use the smaller comment ID as the first comment. | Use an ordered subquery for the first comment and distinct counts or separate aggregates to avoid counting the same row twice. A ticket with two comments and three tags must show `2` and `3`, not `6` and `6`. Keep tickets with no activity. |
| **R04 · Open backlog by age** | Show open ticket counts by category in three age groups: `0–2 days`, `3–6 days` and `7+ days`. Count age in calendar days from the ticket's creation date to today. | Use date comparisons and conditional counts. Freeze today's date in the test and include tickets exactly 2, 3, 6 and 7 days old. Resolved tickets must stay out of the count. |
| **R05 · Top agents in each category** | Within each category, rank current assignees by their resolved ticket count. Show ranks 1–3 and keep all ties. | Group by category and agent first, then use a window function with `DENSE_RANK` within each category. In one category, counts of `5, 4, 4, 3, 2` should show ranks `1, 2, 2, 3` for the first four agents. |

**Models you will query:** `Category`, `Ticket`, `AgentProfile`, `Comment` and `TicketTag`.

**Review check:** Each student submits their own SQL and ORM queries for all five reports. In the review, explain why an inner join loses empty categories, why joining comments and tags can inflate counts, and why ties can produce more than three rows for a category.

**Read:** [Aggregation and filtered counts](https://docs.djangoproject.com/en/6.1/topics/db/aggregation/) · [Query expressions, subqueries and windows](https://docs.djangoproject.com/en/6.1/ref/models/expressions/) · [Window functions](https://docs.djangoproject.com/en/6.1/ref/models/database-functions/#window-functions)

### F07 · Keep the queue fast

- **Build in the UI:** Show the requester, assignee, category and tags on each queue row. On **Ticket Detail**, show comments with their authors.
- **Learn with Django models:** Use `select_related()` for single related objects and `prefetch_related()` for related lists. Try an index for a filter the queue uses.
- **Check your work:** Render the same page before and after optimizing and compare query counts. Load more ticket rows and check whether queries grow with the number of rows. Use `explain()` on the indexed filter and explain the plan.
- **Read:** [Database optimization](https://docs.djangoproject.com/en/6.1/topics/db/optimization/) · [Model indexes](https://docs.djangoproject.com/en/6.1/ref/models/indexes/)

## 3. Add references and extend the ORM

### F08 · Give every ticket a reference

- **Build in the UI:** Show a reference such as `HD-2026-000123` on both **Ticket Queue** and **Ticket Detail**, including tickets created before this feature.
- **Learn with Django models:** Add a nullable field, fill in unique references for old rows in a data migration, then require unique references for all tickets. Make sure new tickets get a reference when saved.
- **Check your work:** Migrate a clean database and one with old tickets. Open an old ticket and a newly created ticket in the browser and check that both show valid, different references.
- **Read:** [Data migrations and historical models](https://docs.djangoproject.com/en/6.1/topics/migrations/#data-migrations) · [RunPython](https://docs.djangoproject.com/en/6.1/ref/migration-operations/#runpython)

### F09 · Search by an exact reference

- **Build in the UI:** Add an exact reference search to **Ticket Queue**. A valid existing reference finds one ticket. Show a helpful error for a bad format and an empty result for a valid reference that does not exist.
- **Learn with Django models:** Use a custom `TicketReferenceField`. Keep the database value as text and return a `TicketReference` object when Django loads it. Use the same reference validation rule for the search form.
- **Check your work:** Test saving, reloading and filtering with an exact reference. Confirm that older reference codes still work and the custom field can be rebuilt from migrations.
- **Read:** [Custom model fields](https://docs.djangoproject.com/en/6.1/howto/custom-model-fields/)

### F10 · Filter references by year

- **Build in the UI:** Add a **Reference Year** filter to **Ticket Queue**. Choosing 2026 shows tickets whose reference code contains that year. The filter works together with the status filter.
- **Learn with Django models:** Register a custom `code_year` lookup on `TicketReferenceField`. The view calls `reference_code__code_year=2026`. Pass the year to SQL as a parameter.
- **Check your work:** Use tickets from two years. Check that the UI and raw PostgreSQL return the same IDs. Test a malformed year and a valid year with no matches.
- **Read:** [Custom lookups](https://docs.djangoproject.com/en/6.1/howto/custom-lookups/)

## Finish and review

- Each student demos an end-to-end flow: open a ticket, find it in the queue, claim it, add a comment, resolve it and show the updated report.
- Submit the ER diagram, models, migrations, repeatable sample data and tests. Each student writes their own SQL and ORM queries for the reports.
- In review, explain how one screen uses the models and complete one new change independently. Example: add an optional due date and show overdue open tickets per agent, including agents with zero overdue tickets.

## What you learned

Use this table in your final review. For each row, point to an example in your own code or tests.

| You can now | Where you used it |
| --- | --- |
| Choose fields, defaults and choices. Explain when to use `blank` or `null`. | Ticket form and optional effort · F01–F02 |
| Link models and control what happens when related rows are deleted. | Agent profiles, tickets, comments and tags · F02–F03 |
| Explain the difference between model validation and database constraints. | Blank titles, duplicate categories and negative estimates · F02–F03 |
| Keep data consistent when a write fails or two people act at once. | Claiming and resolving tickets · F04 |
| Write reusable QuerySets and explain bulk updates. | Queue filters and priority updates · F05 |
| Build SQL and ORM reports with joins, counts, subqueries and window functions. | Support Reports · F06 |
| Measure query counts and check whether an index helps. | Queue loading and query plans · F07 |
| Change a schema and update data that already exists. | Ticket reference backfill · F01, F08 |
| Create a custom field and a custom lookup. | Ticket reference and reference-year filter · F09–F10 |

## What to learn next

| Topic | What to practice later |
| --- | --- |
| Model inheritance | Compare abstract base models, multi-table inheritance and proxy models. |
| Model signals | Try a lifecycle hook and compare it with putting the same action in an explicit function. |
| Multiple databases and legacy schemas | Route queries between databases and connect Django to existing tables. |
| PostgreSQL-specific features | Try full-text search and PostgreSQL-specific field or index types. |
| More advanced ORM extensions | Write a custom transform or database function. Try running a parameterized raw query through Django. |

These topics are follow-up practice. The Helpdesk project is complete when you can demonstrate and explain the features above.
