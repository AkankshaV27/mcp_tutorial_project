from fastmcp import FastMCP

mcp = FastMCP(name="MiniBank")

CUSTOMERS = {
    "CUST1": {"name": "Teju", "email": "teju@example.com"}
}
ACCOUNTS = {
    "ACC123": {"customer_id": "CUST1", "balance": 1250.75}
}
STATEMENTS = {
    "ACC123": [
        {"date": "2025-08-01", "desc": "Paycheck", "amount": +2000.00},
        {"date": "2025-08-05", "desc": "Groceries", "amount": -120.40},
        {"date": "2025-08-10", "desc": "Rent", "amount": -1500.00},
    ]
}

@mcp.tool()
def get_customer(customer_id: str) -> dict:
    """Return basic customer info for a given ID."""
    return CUSTOMERS.get(customer_id, {})

@mcp.tool()
def get_balance(account_id: str) -> dict:
    """Return current account balance for a given account."""
    acc = ACCOUNTS.get(account_id)
    return {"account_id": account_id, "balance": acc["balance"]} if acc else {}

@mcp.tool()
def get_statement(account_id: str) -> list:
    """Return a tiny list of recent transactions for a given account."""
    return STATEMENTS.get(account_id, [])

@mcp.resource(uri="bank://usage", mime_type="text/markdown")
def usage() -> str:
    return (
    "# MiniBank Tools\n"
    "- get_customer(customer_id)\n"
    "- get_balance(account_id)\n"
    "- get_statement(account_id)\n"
    "\nTry: get_balance('ACC123'), get_customer('CUST1')\n"
    )

if __name__ == "__main__":
    # Serve via HTTP so any MCP-capable client (like our LangGraph client) can connect
    mcp.run(transport="http", host="127.0.0.1", port=8000)
