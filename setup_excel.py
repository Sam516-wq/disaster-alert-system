import pandas as pd

# Create initial people data
data = [
    {"Name": "satyam", "Age": 18, "Phone": "+918146567907", "Zone": "Zone A"}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to Excel with correct engine
df.to_excel("people.xlsx", index=False, engine="openpyxl")

print("people.xlsx created successfully ✅")
