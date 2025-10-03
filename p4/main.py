# main.py
from server import mcp

from pathlib import Path

print(f"Current script path: {Path(__file__).resolve().parent}")
# ⬇️ Import tool modules so their @mcp.tool() decorators run
import mix_server.tools.csv_tools
import mix_server.tools.parquet_tools

# Entry point to run the server
if __name__ == "__main__":
    mcp.run()