# Mini In-Memory SQL Query Engine (Python)

## Project Overview

This project implements a simplified, in-memory SQL query engine built using Python.  
It demonstrates how basic SQL queries such as `SELECT`, `WHERE`, and `COUNT` are processed internally by a database system.

The engine loads data from CSV files into memory, parses a limited subset of SQL queries, applies filtering and aggregation logic, and displays results through a command-line interface (CLI).  
The project focuses on understanding core data processing concepts such as selection, filtering, projection, and aggregation.

---

## Key Features

- Load CSV files into memory
- Store table data as a list of dictionaries (`list[dict]`)
- Parse and execute basic SQL queries
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

yaml
Copy code

---

## Setup and Run Instructions

### Prerequisites
- Python 3.8 or higher

### Steps to Run

1. Clone the repository:
git clone https://github.com/NandiniJerripothula-14/mini_sql_engine

css
Copy code

2. Navigate to the project directory:
cd mini_sql_engine

markdown
Copy code

3. Run the CLI application:
python cli.py

yaml
Copy code

You will see:
Mini SQL Engine (type 'exit' to quit)
sql>

yaml
Copy code

Type SQL queries at the `sql>` prompt.  
To exit the application, type `exit` or `quit`.

---

## Supported SQL Grammar (Critical Section)

The engine supports **only the following subset of SQL**.

### SELECT
SELECT *
SELECT column1, column2

shell
Copy code

### FROM
FROM table_name

less
Copy code
- The table name must match a CSV file inside the `data/` directory  
  (example: `employees` → `data/employees.csv`)

### WHERE (Single Condition Only)

Supported comparison operators:
= != > < >= <=

makefile
Copy code

Examples:
SELECT * FROM employees WHERE age > 30;
SELECT name FROM employees WHERE country = 'USA';

shell
Copy code

### Aggregation: COUNT
SELECT COUNT(*) FROM table_name;
SELECT COUNT(column_name) FROM table_name;

yaml
Copy code

- `COUNT(*)` → total number of rows  
- `COUNT(column)` → number of non-null values in the column  

---

## Example Queries and Output

Example queries:
SELECT * FROM employees;
SELECT name, age FROM employees WHERE age > 30;
SELECT COUNT(*) FROM employees;
SELECT COUNT(name) FROM employees WHERE country='USA';

lua
Copy code

Example output:
id name age country
1 Alice 30 USA
2 Bob 25 India
3 Charlie 35 USA

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

## Error Handling

The engine gracefully handles:
- Invalid SQL syntax
- Querying a non-existent table
- Selecting a non-existent column
- Type mismatches in `WHERE` conditions

Example error message:
Error: Column 'salary' does not exist

yaml
Copy code

The application does not crash and always provides clear, informative messages.

---

## Design and Implementation

- CSV files are loaded using Python’s built-in `csv.DictReader`
- Tables are stored in memory as `list[dict]`
- SQL parsing is implemented using simple string processing
- Query execution flow:
  1. Load data (FROM)
  2. Filter rows (WHERE)
  3. Apply aggregation (COUNT)
  4. Apply projection (SELECT)
- Modular design ensures separation of concerns:
  - `parser.py` → SQL parsing
  - `engine.py` → Query execution
  - `cli.py` → User interaction

---

## Limitations

- Only `SELECT` queries are supported
- Only one `WHERE` condition is allowed
- Only `COUNT()` aggregation is implemented
- No support for:
  - JOIN
  - ORDER BY
  - INSERT / UPDATE / DELETE

---

## Conclusion

This project provides a clear and practical demonstration of how a basic SQL query engine works internally using Python.  
It fulfills all submission and evaluation requirements by implementing data loading, parsing, filtering, aggregation, and CLI interaction in a clean and modular way.

---

## Author

Developed as a hands-on learning project to build a simplified in-memory SQL query engine using Python.
