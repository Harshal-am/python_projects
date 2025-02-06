import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  

        soup = BeautifulSoup(response.text, 'html.parser')

        titles = soup.find_all('h1')
        if titles:
            print("\nArticle Titles:")
            for title in titles:
                print("-", title.get_text(strip=True))
        else:
            print("No <h1> titles found on this page.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")

url = input("Enter the URL to scrape: ")
scrape_titles(url)
