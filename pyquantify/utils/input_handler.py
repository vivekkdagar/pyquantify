import requests
from bs4 import BeautifulSoup


def scrape_website(source):
    try:
        response = requests.get(source)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')  # Adjust based on HTML structure
            return "\n".join([p.get_text() for p in paragraphs])
        else:
            print(f"Failed to retrieve content from website. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def load_file(source):
    try:
        with open(source, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {source}")
        return None


def load(mode):
    if mode == 'raw':
        return input("Enter the raw text: ")
    elif mode == 'website':
        return scrape_website(input("Enter the source: "))  # Return directly
    elif mode == 'file':
        return load_file(input("Enter the source: "))  # Return directly
    else:
        raise Exception("Invalid mode. Please use 'raw', 'file', or 'website'.")
