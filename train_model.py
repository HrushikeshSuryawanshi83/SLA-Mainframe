import pandas as pd
import numpy as np
import random
from sklearn.ensemble import RandomForestRegressor
import joblib

# --- STEP 1: GENERATE MOCK DATA ---
print("Generating synthetic training data...")
data = []
for _ in range(1000):
    sql_count = random.randint(0, 50)
    io_count = random.randint(0, 20)
    loop_count = random.randint(0, 100)
    
    # Logic: 
    # SQL is expensive (5ms per call)
    # IO is very expensive (10ms per call)
    # Loops are cheap (1ms per call)
    mips = (sql_count * 1.5) + (loop_count * 0.5) + (io_count * 2.0) + random.uniform(-2, 2)
    response_time = (sql_count * 5) + (io_count * 10) + (loop_count * 1) + random.uniform(-5, 5)
    
    data.append([sql_count, io_count, loop_count, mips, response_time])

df = pd.DataFrame(data, columns=['SQL_Count', 'IO_Count', 'Loop_Count', 'MIPS', 'Response_Time_ms'])

# --- STEP 2: TRAIN MODELS ---
print("Training AI Models...")
X = df[['SQL_Count', 'IO_Count', 'Loop_Count']]
y_mips = df['MIPS']
y_time = df['Response_Time_ms']

model_mips = RandomForestRegressor()
model_mips.fit(X, y_mips)

model_time = RandomForestRegressor()
model_time.fit(X, y_time)

# --- STEP 3: SAVE ARTIFACTS ---
joblib.dump(model_mips, 'mips_model.pkl')
joblib.dump(model_time, 'time_model.pkl')
print("Done! 'mips_model.pkl' and 'time_model.pkl' are ready.")