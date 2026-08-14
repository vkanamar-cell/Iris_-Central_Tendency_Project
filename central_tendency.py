import pandas as pd

# Load the Iris dataset
df = pd.read_csv("Iris.csv")

print("First 5 rows of the dataset:")
print(df.head())

# Numerical columns
columns = ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]

print("\n--- Measures of Central Tendency ---")

for column in columns:
    mean = df[column].mean()
    median = df[column].median()
    mode = df[column].mode()[0]

    print(f"\n{column}")
    print("Mean   :", mean)
    print("Median :", median)
    print("Mode   :", mode)
