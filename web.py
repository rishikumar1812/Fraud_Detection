import requests
from urllib.parse import urlparse

# Expanded list of legitimate shopping domains (for illustration purposes)
LEGITIMATE_DOMAINS = [
    "amazon.com", "amazon.in", "ebay.com", "walmart.com", "bestbuy.com", "target.com",
    "flipkart.com", "alibaba.com", "aliexpress.com", "shopify.com", "costco.com"
]

def is_legitimate_domain(domain):
    """Check if the domain is in the list of legitimate domains."""
    return domain in LEGITIMATE_DOMAINS

def check_url(url):
    try:
        # Check if the URL starts with http or https
        if not url.startswith(('http://', 'https://')):
            print("URL must start with http:// or https://")
            return False

        # Parse the URL to check for validity
        parsed_url = urlparse(url)
        if not parsed_url.netloc:
            print("Invalid URL")
            return False

        # Extract the domain from the URL
        domain = parsed_url.netloc.replace('www.', '')
        
        # Check if the domain is in the list of legitimate domains
        if not is_legitimate_domain(domain):
            print(f"The URL '{url}' is not from a verified shopping website. It may be fraudulent.")
            return False

        # Send a request to the URL
        response = requests.get(url, timeout=10)

        # Check if the response status code indicates success
        if response.status_code == 200:
            # Check if the site is using HTTPS for security
            if parsed_url.scheme == 'https':
                print(f"The URL '{url}' is verified and secure.")
                return True
            else:
                print(f"The URL '{url}' is verified but not secure (HTTP).")
                return True
        else:
            print(f"The URL '{url}' returned a status code of {response.status_code}.")
            return False

    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
url_to_check = input("Enter the URL to check: ")
check_url(url_to_check)


