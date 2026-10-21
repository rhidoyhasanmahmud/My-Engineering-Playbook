---
title: "B- Tree and B+ Tree"
track: database-engineering
status: draft
---

> **Draft:** Existing study material. The seven-section format, references and technical details still need review.

[Study roadmap](../../roadmaps/database-engineering.md) · [All notes](../README.md)

# B- Tree and B+ Tree

Both B-Tree and B+ Tree are self-balancing tree data structures used in databases for efficient indexing and range
queries.

**Key Differences: B-Tree vs B+ Tree**

| Feature            | B-Tree                                          | B+ Tree                                              |
|--------------------|--------------------------------------------------|------------------------------------------------------|
| Data storage       | Data is stored in **all nodes** (internal + leaf)| Data is stored **only in leaf nodes**               |
| Internal nodes     | Store keys and **data pointers**                | Store only keys (**no data**)                       |
| Leaf nodes         | Contain **some** data                           | Contain **all** data                                |
| Linked leaves      | ❌ Not necessarily linked                        | ✅ Leaf nodes are **linked**                         |
| Range queries      | ❌ Slower (must traverse up/down)                | ✅ Fast (sequential leaf scan)                       |
| Height (depth)     | Taller (less fan-out)                           | Shorter (more fan-out per level)                    |
| Index-only scan    | ❌ May need to access internal node data         | ✅ Leaf scan is complete                             |
| Used in (examples) | Older DBs, memory-efficient trees               | Most modern DBMS (e.g., MySQL, PostgreSQL, Oracle)  |

**Example Layout**

B-Tree (Simplified)

```csharp
          [50]
        /     \
     [10,20]  [60,70] ← internal and leaf nodes both store data
```

B+ Tree (Simplified)

```css
          [50]
        /     \
     [10,20]  [60,70] ← only keys here
     ↓         ↓
  [10,20]→[30,40]→[50,60]→[70,80] ← all data in linked leaf nodes
```

**Summary**

| Use Case                                | Choose... |
|-----------------------------------------|-----------|
| Efficient range scans                   | B+ Tree   |
| Smaller index (but less optimal scans)  | B-Tree    |
| All modern DBMS use for indexes         | B+ Tree   |

**💡 In real-world databases, B+ Trees dominate because:**

* They support fast range scans
* Leaf nodes can be scanned like a linked list
* Internal nodes stay smaller = better cache performance

---

**B-Tree Example (Simplified)**


