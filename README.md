# Mini In-Memory SQL Query Engine (Python)

A simplified, in-memory SQL query engine built from scratch using Python.  
This project demonstrates fundamental database concepts including data loading, SQL parsing, query execution, and command-line interface (CLI) design.

---

## Overview

This engine loads CSV files into memory and allows users to execute a limited subset of SQL queries interactively.  
It helps demystify how databases process queries internally by clearly separating parsing, filtering, aggregation, and projection logic.

The project is designed for learning purposes and focuses on clarity, modularity, and correctness rather than performance or full SQL compliance.

---

## Features

- **Data Loading**
  - Load CSV files from the `data/` directory
  - Store data as a list of dictionaries (`list[dict]`)

- **SQL Parsing**
  - Supports `SELECT`, `FROM`, and optional `WHERE` clauses
  - Simple and readable parsing logic

- **Query Execution**
  - **Projection**
    - `SELECT *`
    - `SELECT column1, column2`
  - **Filtering**
    - Single-condition `WHERE` clause
    - Operators: `=`, `!=`, `>`, `<`, `>=`, `<=`
  - **Aggregation**
    - `COUNT(*)`
    - `COUNT(column_name)`

- **Interactive CLI**
  - REPL-style interface for executing queries interactively

- **Error Handling**
  - Clear, user-friendly error messages
  - Graceful handling of invalid queries

- **Formatted Output**
  - Results displayed in tabular format

---

## Supported SQL Grammar

SELECT <select_list>
FROM <table_name>
[WHERE <condition>]

shell
Copy code

### Select List
column1, column2
COUNT(*)
COUNT(column_name)

shell
Copy code

### Condition
<column_name> <operator> <value>

shell
Copy code

### Operators
= != > < >= <=

shell
Copy code

### Values
Numbers (integer or decimal)
Strings enclosed in single quotes

makefile
Copy code

Example:
SELECT name, age FROM employees WHERE age > 30;

yaml
Copy code

---

## Project Structure

mini_sql_engine/
├── data/
│ ├── employees.csv
│ ├── students.csv
├── parser.py # SQL parsing logic
├── engine.py # Query execution engine
├── cli.py # CLI / REPL interface
├── requirements.txt
└── README.md

yaml
Copy code

---

## Installation

### Prerequisites
- Python 3.8 or higher

### Setup

Clone the repository and navigate to the project directory:

git clone https://github.com/NandiniJerripothula-14/mini_sql_engine
cd mini_sql_engine

yaml
Copy code

No external dependencies are required.

---

## Usage

### Starting the Engine

Run:
python cli.py

yaml
Copy code

You will see:
Mini SQL Engine (type 'exit' to quit)
sql>

yaml
Copy code

---

## Running Queries

### Select All Columns
sql> SELECT * FROM employees;

css
Copy code

### Select Specific Columns
sql> SELECT name, age FROM employees;

shell
Copy code

### Filtering with WHERE
sql> SELECT name, age FROM employees WHERE age > 30;

shell
Copy code

### Using Comparison Operators
sql> SELECT * FROM employees WHERE age >= 25;
sql> SELECT * FROM employees WHERE country != 'India';

shell
Copy code

### Count Rows
sql> SELECT COUNT(*) FROM employees;

sql
Copy code

### Count Non-null Values in a Column
sql> SELECT COUNT(name) FROM employees;

graphql
Copy code

### Combined Filtering and Aggregation
sql> SELECT COUNT(*) FROM employees WHERE country = 'USA';

yaml
Copy code

---

## Example Output

id name age country
1 Alice 30 USA
2 Bob 25 India
3 Charlie 35 USA

Copy code
COUNT
3

yaml
Copy code

---

## Sample CSV Files

### employees.csv
id,name,age,country
1,Alice,30,USA
2,Bob,25,India
3,Charlie,35,USA

shell
Copy code

### students.csv
id,name,marks,grade
1,Ravi,85,A
2,Sita,72,B
3,John,90,A

yaml
Copy code

---

## Architecture & Implementation

### Query Execution Pipeline

SQL Query
↓
[Parsing] → parser.py
↓
Parsed Query Dictionary
↓
[Filtering] → engine.py (WHERE)
↓
[Aggregation] → COUNT (if present)
↓
[Projection] → SELECT columns
↓
Formatted Output

yaml
Copy code

---

## Data Structures

### In-Memory Table
[
{'id': '1', 'name': 'Alice', 'age': '30', 'country': 'USA'},
{'id': '2', 'name': 'Bob', 'age': '25', 'country': 'India'}
]

shell
Copy code

### Parsed Query Representation
{
'select_cols': ['name', 'age'],
'from_table': 'employees',
'where_clause': {
'column': 'age',
'operator': '>',
'value': 30
},
'aggregate': None
}

yaml
Copy code

---

## Error Handling

The engine handles errors gracefully, including:
- Invalid SQL syntax
- Non-existent tables
- Non-existent columns
- Invalid WHERE conditions
- Type mismatches during comparisons

Example:
Error: Column 'salary' does not exist

yaml
Copy code

The application never crashes and always provides clear feedback.

---

## Limitations

- Only one WHERE condition supported
- Only COUNT aggregation is implemented
- No JOIN, GROUP BY, ORDER BY, or LIMIT
- No INSERT, UPDATE, or DELETE operations

---

## Possible Enhancements

- Multiple WHERE conditions (AND / OR)
- Additional aggregates (SUM, AVG, MIN, MAX)
- ORDER BY and GROUP BY
- LIMIT clause
- JOIN operations
- INSERT and UPDATE support

---

## Conclusion

This project provides a clean and practical demonstration of how a basic SQL query engine works internally.  
It emphasizes clarity, modular design, and correct execution of core SQL concepts using Python.

---

## Author

Developed as a hands-on learning project to understand SQL parsing and execution by building a simplified i
