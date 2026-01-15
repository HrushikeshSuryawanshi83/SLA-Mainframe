import re
import os

def parse_code(file_path):
    # Determine language by file extension
    ext = os.path.splitext(file_path)[1].lower()
    
    with open(file_path, 'r') as file:
        content = file.read().upper()

    sql_count = 0
    io_count = 0
    loop_count = 0

    if ext in ['.cbl', '.cob']:
        # --- COBOL PARSING ---
        print(f"Analyzing COBOL file: {file_path}")
        sql_count = len(re.findall(r'EXEC SQL', content))
        io_count = len(re.findall(r'(READ|WRITE|REWRITE|OPEN|CLOSE)\s', content))
        loop_count = len(re.findall(r'(PERFORM|LOOP)\s', content))

    elif ext in ['.pli', '.pl1']:
        # --- PL/I PARSING ---
        print(f"Analyzing PL/I file: {file_path}")
        # PL/I uses 'EXEC SQL' too, but I/O is GET/PUT/READ/WRITE
        sql_count = len(re.findall(r'EXEC SQL', content))
        io_count = len(re.findall(r'(GET DATA|PUT DATA|READ FILE|WRITE FILE)', content))
        # PL/I loops are DO...END
        loop_count = len(re.findall(r'\bDO\s', content))

    elif ext in ['.rex', '.rexx']:
        # --- REXX PARSING ---
        print(f"Analyzing REXX file: {file_path}")
        # REXX DB2 interactions often use EXECSQL
        sql_count = len(re.findall(r'EXECSQL', content))
        # REXX I/O often uses EXECIO or STREAM
        io_count = len(re.findall(r'(EXECIO|STREAM|LINEOUT|LINEIN)', content))
        # REXX loops are DO...END
        loop_count = len(re.findall(r'\bDO\s', content))

    else:
        print(f"Unsupported file type: {ext}")
        return None

    return {
        'SQL_Count': sql_count,
        'IO_Count': io_count,
        'Loop_Count': loop_count
    }

# Update the main script to call this generic function
# (This alias allows your existing main script to work without changes)
def parse_cobol_code(file_path):
    return parse_code(file_path)