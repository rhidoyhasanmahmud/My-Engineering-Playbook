# Phase 01 · Part 2 — Build a Helpdesk with Django Models

A requester opens a ticket and chooses a category. An agent claims the ticket, adds comments and resolves it. A support lead can see the queue, check agent workload and find old tickets by their reference codes.

Build the **data layer** in Django and PostgreSQL. Demonstrate each feature in the Django shell or with tests. Complete [Part 1 — SQL practice](../README.md) first. Work through the features at your own pace using the [Django model-layer docs](https://docs.djangoproject.com/en/6.1/#the-model-layer) for your installed Django version.

## 1. Build the data model

### F01 · Open a ticket

- **Build:** Create `Ticket` and `Category`. Each ticket has a requester, category, title, description, status, priority and timestamps. Use Django's configured user model for the requester.
- **Verify:** Run the migrations on an empty PostgreSQL database. Create a ticket in the shell and use `sqlmigrate` to identify its table, primary key and foreign keys.
- **Read:** [Model fields and defaults](https://docs.djangoproject.com/en/6.1/ref/models/fields/) · [Migrations](https://docs.djangoproject.com/en/6.1/topics/migrations/)

### F02 · Assign a ticket and enforce data rules

- **Build:** Add an `AgentProfile` linked one-to-one to a user. Allow an optional assignee and estimated effort in minutes. Enforce unique category names and reject negative estimates at database level.
- **Verify:** Save an unassigned ticket. Compare what happens to a blank title with `full_clean()` and with a direct `save()`. Verify that PostgreSQL rejects duplicate category names and negative estimates.
- **Read:** [Relationships](https://docs.djangoproject.com/en/6.1/topics/db/models/#relationships) · [Model validation](https://docs.djangoproject.com/en/6.1/ref/models/instances/#validating-objects) · [Constraints](https://docs.djangoproject.com/en/6.1/ref/models/constraints/)

### F03 · Add comments and tags

- **Build:** A ticket has many comments and tags. Use `TicketTag` to store who added each tag and when. Prevent duplicate ticket/tag pairs.
- **Verify:** List tags from a ticket and tickets from a tag. Test that deleting a ticket removes its comments (`CASCADE`), deleting an assigned agent profile clears the assignee (`SET_NULL`), and deleting a category in use is blocked (`PROTECT`).
- **Read:** [Many-to-many through models](https://docs.djangoproject.com/en/6.1/topics/db/models/#extra-fields-on-many-to-many-relationships) · [ForeignKey and deletion behavior](https://docs.djangoproject.com/en/6.1/ref/models/fields/#foreignkey)

## 2. Run the support workflow and reports

### F04 · Claim and resolve tickets safely

- **Build:** Let an agent claim an unassigned ticket. When a ticket is resolved, update its status and add a `StatusChange` entry in the same transaction.
- **Verify:** If writing the history fails, the status stays unchanged. Simulate two agents claiming the same ticket through separate database transactions. Exactly one claim succeeds. Explain your choice of a conditional update or row locking.
- **Read:** [Transactions](https://docs.djangoproject.com/en/6.1/topics/db/transactions/) · [QuerySet updates and locking](https://docs.djangoproject.com/en/6.1/ref/models/querysets/)

### F05 · Find work in the queue

- **Build:** Add reusable QuerySet methods for open tickets, unassigned tickets and an agent's queue. Combine them with priority and date filters. Break sorting ties with ticket ID.
- **Verify:** Match the ordered ticket IDs against a SQL query. On test rows, compare query counts and model `save()` behavior for a per-ticket save loop and a bulk `QuerySet.update()`.
- **Read:** [QuerySets and Q objects](https://docs.djangoproject.com/en/6.1/topics/db/queries/) · [Custom managers](https://docs.djangoproject.com/en/6.1/topics/db/managers/) · [QuerySet.update()](https://docs.djangoproject.com/en/6.1/ref/models/querysets/#update)

### F06 · Report on workload and response

- **Build:** Report ticket count per category, resolved share per agent with assigned tickets, and first comment time per ticket. Treat a ticket with no comments as having no first comment time.
- **Verify:** SQL and ORM return the same results. Include an empty category and an agent with assigned tickets and zero resolutions.
- **Read:** [Aggregation and filtered counts](https://docs.djangoproject.com/en/6.1/topics/db/aggregation/) · [Expressions and subqueries](https://docs.djangoproject.com/en/6.1/ref/models/expressions/)

### F07 · Measure and improve queue performance

- **Build:** Load queue rows with their requester, assignee, category, tags and comments. Try an index for a filter that the queue actually uses.
- **Verify:** Record query counts before and after using `select_related()` and `prefetch_related()`. Compare query plans before and after adding the index and explain the planner's choice.
- **Read:** [Database optimization](https://docs.djangoproject.com/en/6.1/topics/db/optimization/) · [Model indexes](https://docs.djangoproject.com/en/6.1/ref/models/indexes/)

## 3. Evolve the schema and extend the ORM

### F08 · Give existing tickets a reference code

- **Build:** Add a nullable reference field, backfill unique codes such as `HD-2026-000123` in a data migration, then make the field required and unique.
- **Verify:** Migrate both a clean database and one already containing tickets. Check that every existing ticket gets a distinct reference and that new tickets require one.
- **Read:** [Data migrations and historical models](https://docs.djangoproject.com/en/6.1/topics/migrations/#data-migrations) · [RunPython](https://docs.djangoproject.com/en/6.1/ref/migration-operations/#runpython)

### F09 · Create a custom ticket reference field

- **Build:** Replace the plain field with `TicketReferenceField`. Keep the PostgreSQL value as text and return a `TicketReference` object when loading it in Python.
- **Verify:** Check that existing codes survive the migration, valid codes save and load correctly, invalid codes fail validation, and exact filters work. Rebuild the database from migrations.
- **Read:** [Custom model fields: conversion, database preparation and deconstruction](https://docs.djangoproject.com/en/6.1/howto/custom-model-fields/)

### F10 · Filter ticket references by year

- **Build:** Register a custom `code_year` lookup on `TicketReferenceField`. Support `Ticket.objects.filter(reference_code__code_year=2026)` using the year embedded in the reference code.
- **Verify:** Use references from multiple years, compare results with parameterized PostgreSQL, and chain the lookup with a status filter. Test a malformed year and a valid year with no matches.
- **Read:** [Custom lookups and SQL parameters](https://docs.djangoproject.com/en/6.1/howto/custom-lookups/)

## Finish and review

- Share one Helpdesk schema and review each other's pull requests. Rotate feature ownership so both students work with models, migrations and queries.
- Submit an ER diagram, reproducible sample data, migrations, model tests and SQL/ORM examples for the reports. Each student submits their own report queries.
- In review, explain one modeling decision and solve one unseen change independently. Example: add an optional due date and report overdue open tickets per agent, including agents with zero overdue tickets.
