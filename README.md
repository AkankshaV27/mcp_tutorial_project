## Run
```bash
# Terminal 1: start the MCP server
python mcp_server.py

# Terminal 2: run the client
python mcp_client.py
```

**Try these:**
- `What is the balance of ACC123?`
- `Show last few transactions for ACC123.`
- `Who owns ACC123?` (the agent will call get_customer via the account's customer id if needed)

---

## (Optional) Quick curl ping
The MCP transport is on `/mcp` and expects MCP protocol frames, so it’s easiest to test via the client above. If you want a raw sanity check of the HTTP port:
```bash
curl -i http://127.0.0.1:8000/
```
You should see the server is listening (though requests need the MCP framing to use tools).
