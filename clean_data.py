
from pathlib import Path
import pandas as pd

# Locate the project folder
BASE_DIR = Path(__file__).resolve().parent

# Read the raw CSV file
input_file = BASE_DIR / "books_data.csv"
df = pd.read_csv(input_file)

# Clean book prices
df["price"] = pd.to_numeric(
    df["price"].astype(str).str.replace(
        r"[^\d.]", "", regex=True
    ),
    errors="coerce"
)

# Convert ratings into numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["rating"] = df["rating"].map(rating_map)

# Create stock availability column
df["stock"] = df["stock"].fillna("").str.strip()

df["in_stock"] = df["stock"].str.contains(
    "In stock", case=False
).astype(int)

# Remove invalid or duplicate records
df = df.drop_duplicates(subset=["title"])
df = df.dropna(subset=["price", "rating"])

# Save cleaned data
output_file = BASE_DIR / "books_data_cleaned.csv"

df.to_csv(output_file, index=False, encoding="utf-8-sig")

print("Data cleaning completed successfully!")
print("Total cleaned books:", len(df))
print("Created:", output_file.name)
print(df.head())
