from server import mcp

from mix_server.utils.file_reader import read_parquet_summary


@mcp.tool()
def summarize_parquet_file(filename: str) -> str:
    """
    Summarize a parquet file by reporting its number of rows and columns.
    Args:
        filename: Name of the parquet file in the /data directory (e.g., 'sample.parquet')
    Returns:
        A string describing the file's dimensions.
    """
    return read_parquet_summary(filename)