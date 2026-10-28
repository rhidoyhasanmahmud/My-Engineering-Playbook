# Session 01 — Database Engineering Fundamentals

**Format:** Volunteer discussion class  
**Level:** Beginner (no prior SQL knowledge required)  
**Purpose:** Prepare independently before the live discussion. This is a topic checklist, not a full lesson or answer sheet.

> **Before class:** Read the topics, try to explain them in your own words, and bring at least two questions. You do not need to master everything. We will clarify misunderstandings together.

## 1. Data, Databases and DBMS
- [ ] Data vs information — what is the difference?
- [ ] What is a database, and why do applications need one?
- [ ] File system / spreadsheet vs database — when is each useful?
- [ ] What is a DBMS? How is it different from a database?
- [ ] DBMS vs RDBMS — examples such as PostgreSQL, MySQL, and SQLite
- [ ] What do persistence, consistency, concurrency, and security mean at a basic level?

**Prepare to discuss:** What could go wrong if a university stores student records in separate Excel files?

## 2. Types of Databases
- [ ] Relational (SQL) databases
- [ ] Document databases
- [ ] Key-value databases
- [ ] Graph databases
- [ ] Wide-column databases
- [ ] SQL vs NoSQL — what does this distinction actually mean?
- [ ] Why is there no single best database for every application?

**Prepare to discuss:** Where might PostgreSQL, MongoDB, Redis, and Neo4j fit? Look up their typical use cases.

## 3. How a Database Works — Big Picture
- [ ] Application → database driver → DBMS → stored data
- [ ] Client-server model and database connections
- [ ] What happens conceptually when an application sends a query?
- [ ] Reading vs writing data
- [ ] What is a transaction? Why does it matter?
- [ ] What are indexes? Why might they speed up some reads?

**Prepare to discuss:** What happens after a user clicks “Register” in an application? Focus on the database's role, not implementation details.

## 4. Relational Data Modeling
- [ ] Entity and attribute
- [ ] Table, row/record, and column
- [ ] Database schema and basic data types
- [ ] NULL vs empty string vs zero
- [ ] Constraints: NOT NULL, UNIQUE, CHECK, DEFAULT
- [ ] Business rules and how they influence table design

**Prepare to discuss:** Identify possible entities and attributes for a university course registration system.

## 5. Keys and Relationships
- [ ] Primary key (PK) — purpose and properties
- [ ] Foreign key (FK) — referential integrity
- [ ] Candidate key and alternate key
- [ ] Composite key
- [ ] Natural key vs surrogate key
- [ ] Primary key vs UNIQUE constraint
- [ ] One-to-one (1:1), one-to-many (1:N), many-to-many (M:N)
- [ ] Junction/associative table for many-to-many relationships

**Prepare to discuss:** Can a student enroll in multiple courses? Can a course contain multiple students? How would you represent this?

## 6. ERD — Entity Relationship Diagram
- [ ] Why do we draw an ERD before implementing tables?
- [ ] Entity, attribute, relationship, and cardinality
- [ ] Optional vs mandatory participation
- [ ] How to identify primary and foreign keys in an ERD
- [ ] Conceptual vs logical vs physical data model (basic idea)
- [ ] Common modeling mistakes

**Prepare to discuss:** Sketch an ERD with **Student**, **Course**, and **Enrollment**. Show PKs, FKs, and cardinalities.

## 7. Data Quality and Basic Normalization
- [ ] What are data duplication and data anomalies?
- [ ] Insert, update, and delete anomalies
- [ ] Why do we normalize relational data?
- [ ] Basic intuition behind 1NF, 2NF, and 3NF
- [ ] When can too many joins become a design consideration?

**Prepare to discuss:** Why is storing a comma-separated list of course IDs inside a Student row problematic in a relational design?

## 8. Basic SQL Vocabulary (Awareness Only)
- [ ] DDL vs DML vs DQL (common teaching categories)
- [ ] CREATE TABLE, INSERT, SELECT, UPDATE, DELETE
- [ ] WHERE, ORDER BY, JOIN
- [ ] What is the difference between DELETE, TRUNCATE, and DROP? (overview)
- [ ] How do SQL queries relate to tables, keys, and relationships?

**Prepare to discuss:** In plain English, describe how to find all courses taken by a particular student. Writing SQL is optional.

## Mini Case Study — University Course Registration

Think about a system where:
- Students have a unique student ID and email.
- Courses have a unique course ID.
- A student may enroll in multiple courses.
- A course may have multiple students.
- Each enrollment has a date and a status.

**Bring to class:**
- [ ] A list of at least three entities and their attributes
- [ ] Your proposed primary and foreign keys
- [ ] A rough ERD (paper or digital)
- [ ] One example of a data-integrity problem
- [ ] Two questions you want to ask during the discussion

## Self-Assessment Before Class
- [ ] I can explain a database and DBMS without memorizing definitions.
- [ ] I can name at least three database types and possible use cases.
- [ ] I can distinguish an entity, attribute, table, and record.
- [ ] I can explain why primary and foreign keys exist.
- [ ] I can recognize 1:1, 1:N, and M:N relationships.
- [ ] I can sketch a simple ERD.
- [ ] I can explain why duplicated data can be problematic.

## Suggested Learning Approach

1. Spend **60–90 minutes** exploring the checklist; prioritize Sections 1–6.
2. Use official documentation or beginner tutorials for unfamiliar terms.
3. Write short explanations **in your own words**; avoid copying definitions.
4. Attempt the mini case study even if your design is incomplete.
5. Bring your uncertainties to the live class.

**Optional starting points:**
- [PostgreSQL Documentation](https://www.postgresql.org/docs/current/)
- [MySQL Reference Manual](https://dev.mysql.com/doc/refman/8.4/en/)
- [MongoDB Documentation](https://www.mongodb.com/docs/)
- [Redis Documentation](https://redis.io/docs/latest/)

> **Scope note:** Enterprise Service Bus (ESB) belongs primarily to enterprise application integration, so it is not part of this database fundamentals session. We can cover it in a separate software architecture discussion.
