import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load data
df = pd.read_csv('historical_performance_data.csv')

# Features (Input) and Targets (Output)
X = df[['SQL_Count', 'IO_Count', 'Loop_Count']]
y_mips = df['MIPS']
y_time = df['Response_Time_ms']

# Train two separate models
model_mips = RandomForestRegressor()
model_mips.fit(X, y_mips)

model_time = RandomForestRegressor()
model_time.fit(X, y_time)

# Save the brains (models) to files
joblib.dump(model_mips, 'mips_model.pkl')
joblib.dump(model_time, 'time_model.pkl')
print("Models trained and saved as .pkl files.")