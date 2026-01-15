import joblib
import pandas as pd
import sys
from parser import parse_cobol_code

# 1. Load the Models
mips_model = joblib.load('mips_model.pkl')
time_model = joblib.load('time_model.pkl')

# 2. Parse the Input File (Passed as command line argument)
filename = sys.argv[1] 
features = parse_cobol_code(filename)

# Convert to DataFrame for prediction
input_df = pd.DataFrame([features])

# 3. Predict Impact
pred_mips = mips_model.predict(input_df)[0]
pred_time = time_model.predict(input_df)[0]

# 4. Define SLA Thresholds (e.g., from a config file)
SLA_MAX_TIME_MS = 100 

# 5. Output Report
print(f"--- SLA GUARDIAN REPORT for {filename} ---")
print(f"Detected Features: {features}")
print(f"Predicted MIPS Consumption: {pred_mips:.2f}")
print(f"Predicted Response Time: {pred_time:.2f} ms")
print(f"SLA Threshold: {SLA_MAX_TIME_MS} ms")

if pred_time > SLA_MAX_TIME_MS:
    print("\n[FAIL] CRITICAL: Code predicted to BREACH SLA.")
    sys.exit(1) # Return Error Code 1 to fail the Jenkins/CI build
else:
    print("\n[PASS] Code is within SLA limits.")
    sys.exit(0) # Return Success