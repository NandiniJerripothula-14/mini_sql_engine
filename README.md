# Mini In-Memory SQL Query Engine (Python)

## Project Overview

This project is a simplified, in-memory SQL query engine built using Python.  
It demonstrates how basic SQL queries such as `SELECT`, `WHERE`, and `COUNT` are processed internally.

The engine loads data from CSV files into memory, parses a limited subset of SQL, applies filtering and aggregation logic, and displays results through a command-line interface (CLI).  
The project helps in understanding core data processing concepts like selection, filtering, projection, and aggregation.

---

## Features

- Load CSV files into memory
- Store table data as a list of dictionaries
- Execute basic SQL queries
- Supported operations:
  - `SELECT *`
  - `SELECT column1, column2`
  - `WHERE` clause with a single condition
  - `COUNT(*)` and `COUNT(column)`
- Interactive command-line interface (REPL)
- Clear and user-friendly error handling

---

## Project Structure

mini_sql_engine/
├── data/
│ ├── employees.csv
│ ├── students.csv
├── parser.py
├── engine.py
├── cli.py
├── README.md
└── requirements.txt



## Setup and Run Instructions

### Prerequisites
- Python 3.8 or higher

### How to Run

1. Clone the repository:
```bash
git clone <your-github-repository-url>
Navigate to the project directory:

bash
Copy code
cd mini_sql_engine
Run the CLI application:

bash
Copy code
python cli.py
You will see:

pgsql
Copy code
Mini SQL Engine (type 'exit' to quit)
sql>
Type SQL queries at the sql> prompt.
To exit, type exit or quit.

Supported SQL Grammar (Critical Section)
The engine supports only the following subset of SQL.

SELECT
sql
Copy code
SELECT *
SELECT column1, column2
FROM
sql
Copy code
FROM table_name
The table name must match a CSV file inside the data/ directory
(example: employees → data/employees.csv)

WHERE (Single Condition Only)
Supported operators:

yaml
Copy code
=   !=   >   <   >=   <=
Examples:

sql
Copy code
SELECT * FROM employees WHERE age > 30;
SELECT name FROM employees WHERE country = 'USA';
Aggregation: COUNT
sql
Copy code
SELECT COUNT(*) FROM table_name;
SELECT COUNT(column_name) FROM table_name;
COUNT(*) → total number of rows

COUNT(column) → number of non-null values in the column

Example Queries and Output
Query
sql
Copy code
SELECT * FROM employees;
Output
markdown
Copy code
id  name     age  country
------------------------------
1   Alice    30   USA
2   Bob      25   India
3   Charlie  35   USA
Query
sql
Copy code
SELECT name, age FROM employees WHERE age > 30;
Output
markdown
Copy code
name     age
------------------------------
Charlie  35
Query
sql
Copy code
SELECT COUNT(*) FROM employees;
Output
markdown
Copy code
COUNT
-----
3
Query
sql
Copy code
SELECT COUNT(name) FROM employees WHERE country='USA';
Output
markdown
Copy code
COUNT
-----
2
Sample CSV Files
employees.csv
csv
Copy code
id,name,age,country
1,Alice,30,USA
2,Bob,25,India
3,Charlie,35,USA
students.csv
csv
Copy code
id,name,marks,grade
1,Ravi,85,A
2,Sita,72,B
3,John,90,A
Error Handling
The engine gracefully handles common errors:

Invalid SQL syntax

Non-existent tables

Non-existent columns

Type mismatches in WHERE conditions

Example:

javascript
Copy code
Error: Column 'salary' does not exist
The application does not crash and always provides clear error messages.

Design and Implementation Details
CSV files are loaded using Python’s csv.DictReader

Tables are stored as list[dict]

SQL parsing uses simple string processing

Execution order:

Load data (FROM)

Filter rows (WHERE)

Apply aggregation (COUNT)

Apply projection (SELECT)

Modular design:

parser.py → SQL parsing

engine.py → Query execution

cli.py → CLI interface

Limitations
Only SELECT queries are supported

Only one WHERE condition is allowed

Only COUNT() aggregation is implemented

No support for:

JOIN

ORDER BY

INSERT / UPDATE / DELETE

Conclusion
This project provides a practical demonstration of how a basic SQL query engine works internally using Python.
It fulfills all the required objectives by correctly implementing data loading, parsing, filtering, aggregation, and user interaction.

Author
Developed as a hands-on learning project to build a simplified in-memory SQL query engine using Python.