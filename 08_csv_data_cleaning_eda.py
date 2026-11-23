# Data Cleaning, Exploratory Data Analysis and Visualization Using Pandas
# The lab manual uses a notebook %%writefile cell to create students1.csv.
# This plain Python version creates the same CSV file directly.
import pandas as pd
filename = "students1.csv"
data = {
    "Name": ["Asha", "Bala", "Charan", "Divya", "Eshan"],
    "Department": ["CSE", "CSE", "ECE", "ECE", "CSE"],
    "Attendance": [90, 80, None, 95, 85],
    "Mark": [88, 76, 92, None, 84]
}
pd.DataFrame(data).to_csv(filename, index=False)
# Load the CSV file
df = pd.read_csv(filename)
print("--- Original Dataset ---")
print(df)
print("\nMissing Values:")
print(df.isnull().sum())
# Fill missing values with column means
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Mark"] = df["Mark"].fillna(df["Mark"].mean())
# Remove duplicate records
df = df.drop_duplicates()
print("\n--- Cleaned Dataset ---")
print(df)
print("\n--- Descriptive Statistics ---")
print(df.describe())
print("\n--- Department-wise Average Marks ---")
print(df.groupby("Department")["Mark"].mean().round(2))
print("\n--- EDA Summary ---")
print("Highest Mark :", df["Mark"].max())
print("Lowest Mark :", df["Mark"].min())
print("Average Mark :", round(df["Mark"].mean(), 2))
print("Average Attendance :", round(df["Attendance"].mean(), 2))
