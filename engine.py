# engine.py

import csv
import os

class SQLEngineError(Exception):
    pass


def load_table(table_name):
    path = os.path.join("data", f"{table_name}.csv")
    if not os.path.exists(path):
        raise SQLEngineError(f"Table '{table_name}' not found")

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def apply_where(rows, condition):
    if not condition:
        return rows

    col = condition["column"]
    op = condition["operator"]
    val = condition["value"]

    filtered = []

    for row in rows:
        if col not in row:
            raise SQLEngineError(f"Column '{col}' does not exist")

        cell = row[col]

        try:
            if isinstance(val, (int, float)):
                cell = float(cell)
        except ValueError:
            raise SQLEngineError("Type mismatch in WHERE clause")

        if (
            (op == "=" and cell == val) or
            (op == "!=" and cell != val) or
            (op == ">" and cell > val) or
            (op == "<" and cell < val) or
            (op == ">=" and cell >= val) or
            (op == "<=" and cell <= val)
        ):
            filtered.append(row)

    return filtered


def apply_select(rows, select_cols):
    if select_cols == "*":
        return rows

    result = []
    for row in rows:
        new_row = {}
        for col in select_cols:
            if col not in row:
                raise SQLEngineError(f"Column '{col}' does not exist")
            new_row[col] = row[col]
        result.append(new_row)
    return result


def apply_count(rows, agg):
    if agg == "COUNT(*)":
        return len(rows)

    col = agg[6:-1].strip()
    count = 0
    for row in rows:
        if col not in row:
            raise SQLEngineError(f"Column '{col}' does not exist")
        if row[col] not in ("", None):
            count += 1
    return count


def execute_query(parsed):
    rows = load_table(parsed["from"])
    rows = apply_where(rows, parsed["where"])

    if parsed["aggregate"]:
        return apply_count(rows, parsed["aggregate"])

    return apply_select(rows, parsed["select"])
