# Web scraping service
# services/web_scraping/scraper.py - Web scraping service

import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """
    Fetches content from the specified URL and extracts information using BeautifulSoup.
    
    Parameters:
        url (str): The URL of the website to scrape.
    
    Returns:
        str: Extracted information or an error message.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
        
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Extract and return the title of the webpage
        # Modify this to extract other information as needed
        title = soup.title.text if soup.title else 'No title found'
        return title
    except requests.RequestException as e:
        return f"An error occurred while fetching the webpage: {e}"

# If you want to test the scraper functionality directly, you can uncomment the following lines:
# if __name__ == "__main__":
#     test_url = "https://www.example.com"
#     print(f"Scraping {test_url}")
#     result = scrape_website(test_url)
#     print(f"Result: {result}")
