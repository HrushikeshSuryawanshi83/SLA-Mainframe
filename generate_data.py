import pandas as pd
import numpy as np
import random

# Generate 1000 synthetic historical records
data = []
for _ in range(1000):
    sql_count = random.randint(0, 50)
    io_count = random.randint(0, 20)
    loop_count = random.randint(0, 100)
    
    # Simulate Logic: More SQL/Loops = Higher MIPS and Response Time
    # Randomness added to simulate real-world variance
    mips = (sql_count * 1.5) + (loop_count * 0.5) + (io_count * 2.0) + random.uniform(-2, 2)
    response_time = (sql_count * 5) + (io_count * 10) + (loop_count * 1) + random.uniform(-10, 10)
    
    data.append([sql_count, io_count, loop_count, mips, response_time])

df = pd.DataFrame(data, columns=['SQL_Count', 'IO_Count', 'Loop_Count', 'MIPS', 'Response_Time_ms'])
df.to_csv('historical_performance_data.csv', index=False)
print("Mock historical data generated.")