# Phase 01 · Part 2 — Build a Helpdesk with Django Models

Build a small website where people can report a problem and support agents can fix it. For example, a user opens a ticket called **“I cannot log in.”** An agent finds it in the queue, claims it, adds a comment and marks it as resolved. The support report then shows the ticket as resolved.

**Your main goal is to learn Django models and the ORM.** Each screen gives you a reason to design a model, write a query or enforce a data rule. Use PostgreSQL with simple Django views, forms and templates. Complete [Part 1 — SQL practice](../README.md) first. Use the [Django model-layer docs](https://docs.djangoproject.com/en/6.1/#the-model-layer) for your installed version.

## What you will build

| Screen | What someone can do |
| --- | --- |
| **New Ticket** | Enter a title and description, choose a category and priority, and submit the ticket. |
| **Ticket Queue** | Find open or unassigned tickets, filter the list, and search by ticket reference. |
| **Ticket Detail** | See the requester and assignee, add comments and tags, claim or resolve the ticket, and read its status history. |
| **Support Reports** | See ticket counts by category, resolution rates by agent and the first comment time for each ticket. |

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

### F06 · Show support reports

- **Build in the UI:** On **Support Reports**, show the ticket count for each category, the percentage of assigned tickets each agent has resolved, and the time of the first comment on each ticket.
- **Learn with Django models:** Use aggregation, filtered counts and expressions. Try a subquery for the first comment time.
- **Check your work:** Show a category with zero tickets and an agent with assigned tickets but zero resolutions. Show a dash for tickets without comments. Compare all three reports with raw SQL.
- **Read:** [Aggregation](https://docs.djangoproject.com/en/6.1/topics/db/aggregation/) · [Expressions and subqueries](https://docs.djangoproject.com/en/6.1/ref/models/expressions/)

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
