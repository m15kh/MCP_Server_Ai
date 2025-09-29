To run the code, use the following command:

```bash
fastmcp run s1.py:mcp --transport http --port 8000
# Run the server using stdio (default)
fastmcp run server.py:mcp

# Run the server using Server-Sent Events (SSE) on port 8080
fastmcp run server.py:mcp --transport sse --port 8080 --host 0.0.0.0

# Run with a different log level
fastmcp run server.py:mcp --transport sse --log-level DEBUG
