> **Draft practice:** Existing exercises and solutions; review edge cases and database/language assumptions before relying on them.

[Practice index](../../README.md)

# Problem: Find Low Fat & Recyclable Products

## Table 

Products(product_id INT, low_fats ENUM('Y','N'), recyclable ENUM('Y','N'))

## Goal

- Return product_ids where low_fats = 'Y' AND recyclable = 'Y'.

## Solution (SQL)

```sql
SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';
```

## Notes:
- Uses a simple WHERE clause with AND logic.
- Efficient: minimal conditions on indexed/enum columns.