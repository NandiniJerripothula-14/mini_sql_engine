# parser.py

import re

class SQLParserError(Exception):
    pass


def parse_sql(query: str) -> dict:
    query = query.strip().rstrip(";")

    if not query.lower().startswith("select"):
        raise SQLParserError("Only SELECT queries are supported")

    parsed = {
        "select": None,
        "from": None,
        "where": None,
        "aggregate": None
    }

    query_upper = query.upper()

    # -------- SELECT & FROM --------
    try:
        select_part = query[query_upper.index("SELECT") + 6: query_upper.index("FROM")].strip()
        from_part = query[query_upper.index("FROM") + 4:].strip()
    except ValueError:
        raise SQLParserError("Invalid SQL syntax")

    # -------- WHERE --------
    where_part = None
    if "WHERE" in from_part.upper():
        from_name, where_part = re.split(r"\bWHERE\b", from_part, flags=re.IGNORECASE)
        parsed["from"] = from_name.strip()
    else:
        parsed["from"] = from_part.strip()

    # -------- SELECT --------
    if select_part.upper().startswith("COUNT"):
        parsed["aggregate"] = select_part.strip()
    elif select_part == "*":
        parsed["select"] = "*"
    else:
        parsed["select"] = [c.strip() for c in select_part.split(",")]

    # -------- WHERE Parsing --------
    if where_part:
        match = re.search(r"(<=|>=|!=|=|<|>)", where_part)
        if not match:
            raise SQLParserError("Invalid WHERE condition")

        op = match.group()
        col, val = where_part.split(op)

        val = val.strip()
        if val.startswith("'") and val.endswith("'"):
            val = val[1:-1]
        else:
            try:
                val = int(val)
            except ValueError:
                try:
                    val = float(val)
                except ValueError:
                    pass

        parsed["where"] = {
            "column": col.strip(),
            "operator": op,
            "value": val
        }

    return parsed
