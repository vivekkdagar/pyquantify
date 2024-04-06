import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import time


def scrape_website(source):
    try:
        response = requests.get(source)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            paragraphs = soup.find_all('p')  # Adjust based on HTML structure

            # Add tqdm for progress bar
            with tqdm(total=len(paragraphs), desc="Scraping Website") as pbar:
                extracted_text = []
                for p in paragraphs:
                    # Simulate some processing time
                    time.sleep(0.01)
                    extracted_text.append(p.get_text())
                    pbar.update(1)
            return "\n".join(extracted_text)
        else:
            print(f"Failed to retrieve content from website. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def load_file(source):
    try:
        with open(source, 'r', encoding='utf-8') as file:
            file_lines = file.readlines()

            # Add tqdm for progress bar
            with tqdm(total=len(file_lines), desc="Loading File") as pbar:
                content = ""
                for line in file_lines:
                    # Simulate some processing time
                    time.sleep(0.01)
                    content += line
                    pbar.update(1)
            return content
    except FileNotFoundError:
        print(f"File not found: {source}")
        return None


def load_data(mode):
    if mode == 'raw':
        return input("Enter the raw text: ")
    elif mode == 'website':
        return scrape_website(input("Enter the source: "))  # Return directly
    elif mode == 'file':
        return load_file(input("Enter the source: "))  # Return directly
    raise Exception("Invalid mode. Please use 'raw', 'file', or 'website'.\n")
