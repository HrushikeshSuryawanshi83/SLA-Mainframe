import re

def parse_cobol_code(file_path):
    with open(file_path, 'r') as file:
        content = file.read().upper() # Mainframe is case-insensitive usually

    # Simple Regex to find patterns (POC level)
    sql_matches = len(re.findall(r'EXEC SQL', content))
    io_matches = len(re.findall(r'(READ|WRITE|REWRITE)\s', content))
    loop_matches = len(re.findall(r'(PERFORM|LOOP)\s', content))

    return {
        'SQL_Count': sql_matches,
        'IO_Count': io_matches,
        'Loop_Count': loop_matches
    }