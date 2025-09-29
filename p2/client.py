# my_client.py
from fastmcp import Client
import asyncio

async def interact_with_server():
    print("--- Creating Client ---")

    # Option 1: Connect to a server run via `python3 server.py` (uses stdio)
    # client = Client("server.py")

    # Option 2: Connect to a server run via `fastmcp run ... --transport sse --port 8080`
    client = Client("http://0.0.0.0:8080") # Use the correct URL/port

    print(f"Client configured to connect to: {client}")

    try:
        async with client:
            print("--- Client Connected ---")
            # Call the 'greet' tool
            greet_result = await client.call_tool("greet", {"name": "Remote Client"})
            print(f"greet result: {greet_result}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("--- Client Interaction Finished ---")

if __name__ == "__main__":
    asyncio.run(interact_with_server())