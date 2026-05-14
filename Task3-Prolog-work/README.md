
# README FOR TASK 3 — PROLOG

```markdown
# Task 3 — Prolog Logic Programming

## Objective

The objective of this task is to:

1. Install SWI-Prolog
2. Configure Prolog
3. Run basic logical programs
4. Create a family tree system

# Technologies Used

- SWI-Prolog

# Files

```text
Task3_Prolog
│
├── family.pl
└── README.md

## Running the Program

### 1. Start SWI-Prolog

```bash
swipl
```

## 2. Load the File

```prolog
['family.pl'].
```

### 3. Run Queries

```prolog
?- grandparent(john, sarah).
output: true

```

```prolog
?- uncle(X, david).
output: X = peter

```

```prolog
?- cousin(X, sarah).
OUTPUT: X = david
```
