import requests
from bs4 import BeautifulSoup

def get_amazon_india_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Updated list of potential price selectors based on HTML inspection
    price_selectors = [
        "priceblock_ourprice",
        "priceblock_dealprice",
        "priceblock_saleprice",
        "a-price-whole"
    ]
    
    price = None
    for selector in price_selectors:
        element = soup.find(id=selector) or soup.find(class_=selector)
        if element:
            price = element.get_text()
            break

    if not price:
        # Additional search for price span elements
        price_spans = soup.find_all("span", {"class": "a-price-whole"})
        if price_spans:
            price = price_spans[0].get_text()

    if not price:
        price = "Price not found. The page layout might have changed."
    
    return price

if __name__ == "__main__":
    url = input("Enter Amazon India Product URL: ")

    if "amazon.in" not in url:
        print("Please enter a valid Amazon India product URL.")
    else:
        price = get_amazon_india_price(url)
        print(f"The price of the product is: {price}")

