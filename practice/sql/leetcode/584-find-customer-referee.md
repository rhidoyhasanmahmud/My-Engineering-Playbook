> **Draft practice:** Existing exercises and solutions; review edge cases and database/language assumptions before relying on them.

[Practice index](../../README.md)

# Problem: Find Customer Referee

## Table

- Customer(id INT, name VARCHAR, referee_id INT)

## Goal

- Return names of customers not referred by customer with id = 2.

## Solution (SQL)

```sql
SELECT name
FROM Customer
WHERE referee_id IS DISTINCT FROM 2;
```

## Alternative (MySQL-safe)

```sql
SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL;
```

## Notes:

- Handles NULL using IS DISTINCT FROM (or use OR referee_id IS NULL for broader compatibility).
- No JOIN needed — simple WHERE filter.
- referee_id IS NULL means the customer was not referred by anyone, and should be included.