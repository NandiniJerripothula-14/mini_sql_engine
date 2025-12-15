# Mini In-Memory SQL Query Engine (Python)

## 📌 Overview

This project implements a simplified, in-memory SQL query engine built entirely using Python. It demonstrates how basic SQL queries are processed internally by a database system.

The engine loads data from CSV files into memory, parses a limited subset of SQL queries, applies filtering and aggregation logic, and displays results through a command-line interface (CLI). This project is designed to build a foundational understanding of data processing concepts such as selection, filtering, projection, and aggregation.

---

## ✨ Key Features

- Load CSV files into memory
- Store table data as a list of dictionaries (`list[dict]`)
- Parse and execute basic SQL queries
- Supported operations:
  - `SELECT *`
  - `SELECT column1, column2`
  - `WHERE` clause with a single condition
  - `COUNT(*)` and `COUNT(column)`
- Interactive CLI (REPL)
- Clear and user-friendly error handling

---

## 📁 Project Structure
mini_sql_engine/
├── data/
│ ├── employees.csv
│ ├── students.csv
├── parser.py
├── engine.py
├── cli.py
├── README.md
└── requirements.txt


---

## ⚙️ Setup and Execution

### Prerequisites
- Python 3.8 or higher

### Steps to Run

1. Clone the repository:


git clone https://github.com/NandiniJerripothula-14/mini_sql_engine


2. Navigate to the project directory:


cd mini_sql_engine


3. Run the CLI application:


python cli.py


You will see:


Mini SQL Engine (type 'exit' to quit)
sql>


Type SQL queries at the `sql>` prompt.  
To exit, type `exit` or `quit`.

---

## 🧠 Supported SQL Grammar (Critical Section)

The engine supports **only the following subset of SQL**.

### SELECT


SELECT *
SELECT column1, column2


### FROM


FROM table_name

The table name must match a CSV file inside the `data/` directory  
(example: `employees` → `data/employees.csv`)

### WHERE (Single Condition Only)

Supported comparison operators:


= != > < >= <=


Examples:


SELECT * FROM employees WHERE age > 30;
SELECT name FROM employees WHERE country = 'USA';


### Aggregation: COUNT


SELECT COUNT(*) FROM table_name;
SELECT COUNT(column_name) FROM table_name;


- `COUNT(*)` → total number of rows  
- `COUNT(column)` → number of non-null values in the column  

---

## 🧪 Example Queries and Output

Example queries:


SELECT * FROM employees;
SELECT name, age FROM employees WHERE age > 30;
SELECT COUNT(*) FROM employees;
SELECT COUNT(name) FROM employees WHERE country='USA';


Example output:

id name age country

1 Alice 30 USA
2 Bob 25 India
3 Charlie 35 USA

COUNT

3


---

## 📊 Sample CSV Files

### employees.csv


id,name,age,country
1,Alice,30,USA
2,Bob,25,India
3,Charlie,35,USA


### students.csv


id,name,marks,grade
1,Ravi,85,A
2,Sita,72,B
3,John,90,A


---

## 🚨 Error Handling

The engine gracefully handles:
- Invalid SQL syntax
- Non-existent tables
- Non-existent columns
- Type mismatches in `WHERE` conditions

Example error message:


Error: Column 'salary' does not exist


The application never crashes and always provides clear, informative messages.

---

## 🏗️ Design and Implementation

- CSV files are loaded using Python’s `csv.DictReader`
- Tables are stored as `list[dict]`
- SQL parsing uses simple string processing
- Query execution flow:
  1. Load data (FROM)
  2. Filter rows (WHERE)
  3. Apply aggregation (COUNT)
  4. Apply projection (SELECT)
- Modular design:
  - `parser.py` → SQL parsing
  - `engine.py` → Query execution
  - `cli.py` → User interaction

---

## ⚠️ Limitations

- Only `SELECT` queries are supported
- Only one `WHERE` condition is allowed
- Only `COUNT()` aggregation is implemented
- No support for:
  - JOIN
  - ORDER BY
  - INSERT / UPDATE / DELETE

---

## ✅ Conclusion

This project provides a practical demonstration of how a basic SQL query engine works internally using Python. It fulfills all requirements by implementing data loading, parsing, filtering, aggregation, and CLI interaction in a clean and modular way.

---

## 👩‍💻 Author

Developed as a hands-on learning project to build a simplified in-memory SQL query engine using Python.
