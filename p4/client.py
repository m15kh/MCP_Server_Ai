# client.py (FastMCP Client)
import asyncio
from fastmcp import Client

async def main():
    # This will spawn your server via stdio (python main.py)
    client = Client("main.py")

    async with client:
        tools = await client.list_tools()
        print("Tools:", [t.name for t in tools])

        result = await client.call_tool(
            "summarize_csv_file", {"filename": "sample.csv"}
        )
        print("Result:", result)

if __name__ == "__main__":
    asyncio.run(main())
