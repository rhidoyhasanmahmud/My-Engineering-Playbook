# Sprint 1 — Django Models and PostgreSQL

**Project:** Helpdesk Ticket System  
**Duration:** Two weeks

Build the data layer for the Helpdesk. Use Django shell and PostgreSQL to verify the features during this sprint. These models will support the REST API in Sprint 2.

| Feature | Build | Learn and reference | Done when |
| --- | --- | --- | --- |
| **F01 — Record a ticket** | Save a ticket with a title, status, requester and creation time. Link the requester to Django's user model. | Field types, choices, foreign keys and migrations. [Model fields](https://docs.djangoproject.com/en/6.1/ref/models/fields/) · [Migrations](https://docs.djangoproject.com/en/6.1/topics/migrations/) | Migrations run on an empty PostgreSQL database. You can save a ticket and identify the requester foreign key in the SQL shown by `sqlmigrate`. |
| **F02 — Categorize tickets** | Create categories with unique names. Assign each ticket to a category. | One-to-many relationships, reverse lookups and uniqueness. [Many-to-one relationships](https://docs.djangoproject.com/en/6.1/topics/db/examples/many_to_one/) · [Unique fields](https://docs.djangoproject.com/en/6.1/ref/models/fields/#unique) | One category can have several tickets. PostgreSQL rejects duplicate category names. |
| **F03 — Add a comment** | Save a comment linked to its ticket and author. | Reverse relationships, `related_name` and `on_delete`. [Related objects](https://docs.djangoproject.com/en/6.1/topics/db/queries/#related-objects) · [ForeignKey](https://docs.djangoproject.com/en/6.1/ref/models/fields/#foreignkey) | You can list all comments for a ticket and explain your chosen behavior when its ticket or author is deleted. |
| **F04 — List recent open tickets** | Return the latest 10 open tickets with requester and category. Use the ticket ID to break ties on creation time. | SQL `WHERE`, `JOIN`, `ORDER BY` and `LIMIT`. ORM filtering, ordering and `select_related()`. [PostgreSQL SELECT](https://www.postgresql.org/docs/current/sql-select.html) · [Django QuerySets](https://docs.djangoproject.com/en/6.1/ref/models/querysets/) | The SQL and ORM versions return the same tickets in the same order. |
| **F05 — Report on tickets and categories** | Count comments per ticket, including tickets with zero comments. List categories with at least three tickets. | `LEFT JOIN`, `COUNT`, `GROUP BY` and `HAVING`. Django `annotate()` and `Count()`. [PostgreSQL Joins](https://www.postgresql.org/docs/current/tutorial-join.html) · [PostgreSQL Aggregates](https://www.postgresql.org/docs/current/tutorial-agg.html) · [Django Aggregation](https://docs.djangoproject.com/en/6.1/topics/db/aggregation/) | Both reports match between SQL and ORM. A ticket without comments appears with a count of zero. |

## Weekly work

- **Week 1 · F01–F03.** One student owns Ticket and Category. The other owns Comment and sample data. Review each other's PRs. Seed data with a ticket without comments, a category without tickets and a category with at least three tickets.
- **Week 2 · F04–F05.** Each student independently writes `practice.sql` and `orm_examples.py` against the same sample data.

## Sprint review

Show the ER diagram, models, migrations, sample data and query results. Each student gets the same live task: **Find categories with no tickets using both SQL and the Django ORM. Explain why an inner join would omit those categories.**
