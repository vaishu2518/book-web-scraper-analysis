
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned CSV file
BASE_DIR = Path(__file__).resolve().parent
file_path = BASE_DIR / "books_data_cleaned.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("Total books:", len(df))

# 4. BUSINESS INSIGHTS
print("\n========== BUSINESS INSIGHTS ==========")

# Insight 1: Most common rating
rating_counts = df["rating"].value_counts()

if not rating_counts.empty:
    most_common_rating = int(rating_counts.idxmax())
    number_of_books = int(rating_counts.max())

    print(
        f"\n1. Most common rating: {most_common_rating}/5"
    )
    print(f"   Number of books with this rating: {number_of_books}")

# Insight 2: Stock availability percentage
total_books = len(df)

if total_books > 0:
    in_stock_count = int((df["in_stock"] == 1).sum())
    stock_percentage = in_stock_count / total_books * 100

    print(
        f"\n2. Stock availability: {stock_percentage:.1f}%"
    )
    print(
        f"   {in_stock_count} out of {total_books} books "
        "are in stock."
    )

# Insight 3: Highest-priced book
if not df.empty:
    expensive_book = df.loc[df["price"].idxmax()]

    print("\n3. Highest-priced book:")
    print("   Title:", expensive_book["title"])
    print(f"   Price: {expensive_book['price']:.2f}")

# Insight 4: Lowest-priced book
if not df.empty:
    cheapest_book = df.loc[df["price"].idxmin()]

    print("\n4. Lowest-priced book:")
    print("   Title:", cheapest_book["title"])
    print(f"   Price: {cheapest_book['price']:.2f}")

# Insight 5: Compare average prices by rating
average_price_by_rating = (
    df.groupby("rating")["price"].mean().sort_values(
        ascending=False
    )
)

print("\n5. Average price by rating:")
print(average_price_by_rating.round(2))

if not average_price_by_rating.empty:
    top_rating_group = average_price_by_rating.index[0]
    top_average_price = average_price_by_rating.iloc[0]

    print(
        f"   Rating group {top_rating_group:.0f}/5 has "
        f"the highest average price: {top_average_price:.2f}"
    )

# Insight 6: Check relationship between price and rating
if len(df) >= 2 and df["price"].nunique() > 1 \
        and df["rating"].nunique() > 1:

    correlation = df["price"].corr(df["rating"])

    print("\n6. Price-rating correlation:", round(correlation, 2))

    if correlation > 0.3:
        print("   The data shows a positive relationship.")
    elif correlation < -0.3:
        print("   The data shows a negative relationship.")
    else:
        print("   The linear relationship is weak.")

    print(
        "   Note: Correlation does not prove that rating "
        "causes a price change."
    )

print("\n========== END OF BUSINESS INSIGHTS ==========")

# 5. GENERATE CHARTS
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Chart 1: Book price distribution
plt.figure(figsize=(8, 5))
plt.hist(df["price"].dropna(), bins=10, edgecolor="black")
plt.title("Distribution of Book Prices")
plt.xlabel("Price")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig(BASE_DIR / "price_distribution.png")
plt.show()
plt.close()

# Chart 2: Book ratings distribution
plt.figure(figsize=(8, 5))
df["rating"].value_counts().sort_index().plot(
    kind="bar", edgecolor="black"
)
plt.title("Book Ratings Distribution")
plt.xlabel("Rating (1 to 5)")
plt.ylabel("Number of Books")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(BASE_DIR / "ratings_distribution.png")
plt.show()
plt.close()

# Chart 3: Stock availability
in_stock = int((df["in_stock"] == 1).sum())
out_of_stock = int((df["in_stock"] == 0).sum())

stock_counts = pd.Series({
    "In stock": in_stock,
    "Out of stock": out_of_stock
})

plt.figure(figsize=(7, 5))
stock_counts.plot(kind="bar", edgecolor="black")
plt.title("Book Stock Availability")
plt.xlabel("Availability")
plt.ylabel("Number of Books")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(BASE_DIR / "stock_availability.png")
plt.show()
plt.close()

print("\nAll three charts generated successfully!")
print("Saved in:", BASE_DIR)

# Business Recommendations

print("\n" + "=" * 45)
print("BUSINESS RECOMMENDATIONS")
print("=" * 45)

average_price = df["price"].mean()
average_rating = df["rating"].mean()
stock_percentage = df["in_stock"].mean() * 100

print(f"\n1. Average book price: £{average_price:.2f}")

print(f"2. Average customer rating: {average_rating:.2f}/5")

print(f"3. Books in stock: {stock_percentage:.1f}%")

if average_price > 30:
    print("4. Recommendation: Review pricing for affordability.")
else:
    print("4. Recommendation: Average prices are relatively affordable.")

if average_rating >= 4:
    print("5. Recommendation: Highlight highly rated books.")
else:
    print("5. Recommendation: Investigate ways to improve book ratings.")

if stock_percentage < 80:
    print("6. Recommendation: Review stock availability.")
else:
    print("6. Recommendation: Most books are available.")

