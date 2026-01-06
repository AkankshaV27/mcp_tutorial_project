import asyncio, os
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model("google_genai:gemini-2.0-flash")

async def main():
    # Connect to our MCP server over HTTP
    client = MultiServerMCPClient({
        "bank": {
            "url": "http://127.0.0.1:8000/mcp",
            "transport": "streamable_http",
        }
    })

    # Discover tools (get_customer / get_balance / get_statement)
    tools = await client.get_tools()

    agent = create_react_agent(model=llm, tools=tools)

    res = await agent.ainvoke({"messages": [{"role": "user", "content": "get details of teju. Her id is CUST1"}]})
    for message in res["messages"]:
        print(message)


if __name__ == "__main__":
    asyncio.run(main())
