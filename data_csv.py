import pandas as pd

data = {
    "Name": ["Rohan", "Aman", "Saurya", "Dev", "Manav"],
    "Age": [24, 22, 23, 21, 25],
    "Score": [85, 90, 78, 88, 92]
}

df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)  # Save to CSV

print("✅ data.csv file has been created successfully!")