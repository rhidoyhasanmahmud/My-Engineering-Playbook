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

## How the project grows

Build one stage at a time. Demo it before reading the next stage. Keep the same database and use migrations when the requirements change.

| Stage | New requirement | Demo before moving on |
| --- | --- | --- |
| **1 · A small helpdesk (F01–F03)** | Save a ticket, then add an assignee, comments and tags. | Open a ticket in the browser, refresh the page and find it again with its related data. |
| **2 · A support workflow (F04–F07)** | Agents need to claim and resolve tickets, filter the queue and see support reports. | Run one ticket through the workflow. Show the basic reports first, then finish the three harder reports after measuring queue queries. |
| **3 · A system with existing data (F08–F10)** | Users need a permanent ticket reference and a way to find older tickets. | Upgrade a database with old tickets. Find one by its full reference and filter the queue by reference year. |
| **4 · A helpdesk with multiple teams (F11–F13)** | Route work to the right team, track response deadlines and answer questions about past ticket statuses. | Route a ticket, show its response deadline, resolve and reopen it, then run a report for a time before it was reopened. |

Create categories, tags and demo accounts in Django admin or with sample data.

## 1. Build a small helpdesk

### F01 · Open a ticket

- **Build in the UI:** Start with a title, description and category. After a successful submission, open the ticket's detail page. Set the requester from the logged-in user and default the status to Open.
- **Learn with Django models:** Create `Ticket` and `Category`. Choose field types, status choices, defaults, timestamps and foreign keys. Create and run migrations.
- **Check your work:** Submit a valid ticket, reload its detail page and confirm the data is still there. Use `sqlmigrate` to find the table, primary key and foreign keys.
- **Read:** [Model fields](https://docs.djangoproject.com/en/6.1/ref/models/fields/) · [Migrations](https://docs.djangoproject.com/en/6.1/topics/migrations/)

### F02 · Show who owns a ticket

- **Build in the UI:** On **Ticket Detail**, show the agent's name or **Unassigned**. Add priority choices to the ticket form and an optional estimate in minutes. Show a clear error if the estimate is negative.
- **Learn with Django models:** Link `AgentProfile` one-to-one with a user and link the optional assignee to the ticket. Use database constraints for unique category names and nonnegative estimates. Learn how `blank` differs from `null`.
- **Check your work:** Save a ticket with no assignee and no estimate. Test a blank title with `full_clean()` and with direct `save()`. Test that PostgreSQL rejects a negative estimate or a duplicate category even when the form is bypassed.
- **Read:** [Relationships](https://docs.djangoproject.com/en/6.1/topics/db/models/#relationships) · [Model validation](https://docs.djangoproject.com/en/6.1/ref/models/instances/#validating-objects) · [Constraints](https://docs.djangoproject.com/en/6.1/ref/models/constraints/)

### F03 · Add comments and tags

- **Build in the UI:** On **Ticket Detail**, add a comment and see it in the comment list. Attach an existing tag and show when and by whom it was added.
- **Learn with Django models:** A ticket has many comments and many tags. Use a `TicketTag` through model to store the tag assignment details. Use reverse relations and a unique constraint for each ticket/tag pair.
- **Check your work:** Add the same tag twice and confirm only one link exists. Test that deleting a ticket removes its comments (`CASCADE`), deleting its assignee clears the assignment (`SET_NULL`), and deleting a category in use is blocked (`PROTECT`).
- **Read:** [Many-to-many through models](https://docs.djangoproject.com/en/6.1/topics/db/models/#extra-fields-on-many-to-many-relationships) · [ForeignKey and delete rules](https://docs.djangoproject.com/en/6.1/ref/models/fields/#foreignkey)

## 2. Add the support workflow and reports

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

Build R01 and R02 first. Finish F07, then return to R03–R05. For each report, write a SQL query in PostgreSQL, build the Django ORM version and show its results in a simple table. Use the same sample data to check that both versions agree.

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

## 3. Upgrade a system with existing data

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

## 4. Handle multiple teams, deadlines and history

### F11 · Route tickets to support teams

**New requirement:** One shared queue worked when there were only a few agents. Now Billing and Technical Support need separate queues, and an agent may work on more than one team.

- **Build in the UI:** Give each category a default support team. New tickets go to that team's queue. Show unrouted tickets in a separate view. An agent can claim a team ticket only while they are an active member of that team.
- **Learn with Django models:** Add `SupportTeam` and `TeamMembership` as a many-to-many through model. Store whether a membership is active and add a unique constraint on the team and agent pair. Store the routed team on the ticket so changing a category's default only affects new tickets. Use migrations to add these fields to the existing database.
- **Check your work:** Existing tickets with no routed team are still visible. An active member can claim a ticket, but an inactive member and an agent from another team cannot. Changing a category's default team leaves earlier tickets in their original team.
- **Read:** [Relationships and through models](https://docs.djangoproject.com/en/6.1/topics/db/models/#extra-fields-on-many-to-many-relationships) · [Constraints](https://docs.djangoproject.com/en/6.1/ref/models/constraints/) · [Migrations](https://docs.djangoproject.com/en/6.1/topics/migrations/)

### F12 · Track the first-response deadline

**New requirement:** High-priority tickets need a public agent reply within 4 hours. Other tickets have 24 hours. Changing the rule later must leave existing deadlines intact.

- **Build in the UI:** Show the response deadline and one of four states in the queue: **Waiting**, **Overdue**, **Replied on time** or **Replied late**. Add an **Overdue** filter. Use elapsed hours from creation for this exercise.
- **Learn with Django models:** Save the deadline at ticket creation and store whether each comment is a public reply written by an agent when it is posted. Find the first qualifying reply with an ordered subquery. Use conditional expressions to calculate the state. For old tickets without a recorded deadline, show **Not tracked**.
- **Check your work:** A requester comment or an internal note does not stop the clock. A qualifying reply exactly at the deadline is on time, and a ticket with no reply becomes overdue once the deadline passes. An agent leaving a team does not change their past reply. Compare the overdue filter and report output with SQL using a fixed test clock.
- **Read:** [Subqueries and expressions](https://docs.djangoproject.com/en/6.1/ref/models/expressions/) · [Conditional expressions](https://docs.djangoproject.com/en/6.1/ref/models/conditional-expressions/)

### F13 · Reopen tickets and report past status

**New requirement:** Sometimes a fix fails and a ticket must reopen. A manager also wants to know how many tickets were open, in progress or resolved at an earlier time.

- **Build in the UI:** Add the flow **Open → In Progress → Resolved → Open**. Show who changed each status and when. On **Support Reports**, let a manager choose a cutoff time and see the ticket counts by status at that time.
- **Learn with Django models:** Record an opening event for new tickets and keep status changes as ordered events. Update the current status and add the event in one transaction. For the report, use a subquery to find each ticket's latest event at or before the cutoff, then count tickets by that status. Use event ID to break timestamp ties.
- **Check your work:** Reject invalid transitions and duplicate submissions that repeat a completed transition. A ticket resolved Monday and reopened Tuesday still counts as resolved in Monday's report. Exclude tickets created after the cutoff. If an older ticket has no known status at the cutoff, show it in **Unknown** instead of guessing. Verify the report against PostgreSQL.
- **Read:** [Transactions](https://docs.djangoproject.com/en/6.1/topics/db/transactions/) · [Subqueries and outer references](https://docs.djangoproject.com/en/6.1/ref/models/expressions/) · [Aggregation](https://docs.djangoproject.com/en/6.1/topics/db/aggregation/)

## Finish and review

- Each student opens a ticket, checks its team and deadline, claims it, adds a public reply, resolves it and reopens it. Run the report for a cutoff before reopening and explain why its result differs from the current queue.
- Submit the ER diagram, models, migrations, repeatable sample data and tests. Each student writes their own SQL and ORM queries for the reports.
- In review, explain how one screen uses the models and complete one new change independently. Example: add an optional due date and show overdue open tickets per agent, including agents with zero overdue tickets.

## What you learned

Use this table in your final review. For each row, point to an example in your own code or tests.

| You can now | Where you used it | Official Django docs |
| --- | --- | --- |
| Choose fields, defaults and choices. Explain when to use `blank` or `null`. | Ticket form and optional effort · F01–F02 | [Model fields](https://docs.djangoproject.com/en/6.1/ref/models/fields/) |
| Link models and control what happens when related rows are deleted. | Agent profiles, tickets, comments and tags · F02–F03 | [Relationships](https://docs.djangoproject.com/en/6.1/topics/db/models/#relationships) · [ForeignKey and on_delete](https://docs.djangoproject.com/en/6.1/ref/models/fields/#foreignkey) |
| Explain the difference between model validation and database constraints. | Blank titles, duplicate categories and negative estimates · F02–F03 | [Model validation](https://docs.djangoproject.com/en/6.1/ref/models/instances/#validating-objects) · [Constraints](https://docs.djangoproject.com/en/6.1/ref/models/constraints/) |
| Keep data consistent when a write fails or two people act at once. | Claiming and resolving tickets · F04 | [Transactions](https://docs.djangoproject.com/en/6.1/topics/db/transactions/) · [QuerySet updates and locking](https://docs.djangoproject.com/en/6.1/ref/models/querysets/) |
| Write reusable QuerySets and explain bulk updates. | Queue filters and priority updates · F05 | [Managers](https://docs.djangoproject.com/en/6.1/topics/db/managers/) · [Bulk updates](https://docs.djangoproject.com/en/6.1/ref/models/querysets/#update) |
| Build SQL and ORM reports with joins, counts, subqueries and window functions. | Support Reports · F06 | [Aggregation](https://docs.djangoproject.com/en/6.1/topics/db/aggregation/) · [Subqueries and windows](https://docs.djangoproject.com/en/6.1/ref/models/expressions/) |
| Measure query counts and check whether an index helps. | Queue loading and query plans · F07 | [Database optimization](https://docs.djangoproject.com/en/6.1/topics/db/optimization/) · [Indexes](https://docs.djangoproject.com/en/6.1/ref/models/indexes/) |
| Change a schema and update data that already exists. | Ticket reference backfill · F01, F08 | [Migrations](https://docs.djangoproject.com/en/6.1/topics/db/migrations/) · [Data migrations](https://docs.djangoproject.com/en/6.1/topics/db/migrations/#data-migrations) |
| Create a custom field and a custom lookup. | Ticket reference and reference-year filter · F09–F10 | [Custom fields](https://docs.djangoproject.com/en/6.1/howto/custom-model-fields/) · [Custom lookups](https://docs.djangoproject.com/en/6.1/howto/custom-lookups/) |
| Model team membership, calculate time-based states and report from event history. | Team routing, response deadlines and past status · F11–F13 | [Through models](https://docs.djangoproject.com/en/6.1/topics/db/models/#extra-fields-on-many-to-many-relationships) · [Conditional expressions](https://docs.djangoproject.com/en/6.1/ref/models/conditional-expressions/) · [Subqueries](https://docs.djangoproject.com/en/6.1/ref/models/expressions/) |

## What to learn next

| Topic | What to practice later | Official Django docs |
| --- | --- | --- |
| Model inheritance | Compare abstract base models, multi-table inheritance and proxy models. | [Model inheritance](https://docs.djangoproject.com/en/6.1/topics/db/models/#model-inheritance) |
| Model signals | Try a lifecycle hook and compare it with putting the same action in an explicit function. | [Model signals](https://docs.djangoproject.com/en/6.1/ref/signals/#model-signals) |
| Multiple databases and legacy schemas | Route queries between databases and connect Django to existing tables. | [Multiple databases](https://docs.djangoproject.com/en/6.1/topics/db/multi-db/) · [Legacy databases](https://docs.djangoproject.com/en/6.1/howto/legacy-databases/) |
| PostgreSQL-specific features | Try full-text search and PostgreSQL-specific field or index types. | [Full-text search](https://docs.djangoproject.com/en/6.1/ref/contrib/postgres/search/) · [PostgreSQL fields](https://docs.djangoproject.com/en/6.1/ref/contrib/postgres/fields/) · [PostgreSQL indexes](https://docs.djangoproject.com/en/6.1/ref/contrib/postgres/indexes/) |
| More advanced ORM extensions | Write a custom transform or database function. Try running a parameterized raw query through Django. | [Custom transforms](https://docs.djangoproject.com/en/6.1/howto/custom-lookups/#a-transformer-example) · [Database functions](https://docs.djangoproject.com/en/6.1/ref/models/database-functions/) · [Raw SQL](https://docs.djangoproject.com/en/6.1/topics/db/sql/) |

These topics are follow-up practice. The Helpdesk project is complete when you can demonstrate and explain the features above.
