
import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
all_books = []

for page in range(1, 6):
    url = base_url.format(page)
    print("Scraping page", page)

    response = requests.get(url, timeout=15)

    if response.status_code != 200:
        print("Failed to fetch page", page)
        continue

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.p["class"][1]
        stock = book.find(
            "p", class_="instock availability"
        ).get_text(" ", strip=True)

        all_books.append({
            "title": title,
            "price": price,
            "rating": rating,
            "stock": stock
        })

df = pd.DataFrame(all_books)
df.to_csv("books_data.csv", index=False, encoding="utf-8-sig")

print("Scraping finished!")
print("Total books collected:", len(df))
print("CSV file created: books_data.csv")
