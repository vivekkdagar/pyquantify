import requests
from bs4 import BeautifulSoup


class InputHandler:
    def __init__(self, mode, source):
        self.mode = mode
        self.source = source
        self.text = None

    def get_file_input(self):
        try:
            with open(self.source, 'r', encoding='utf-8') as file:
                self.text = file.read()
        except FileNotFoundError:
            print(f"File not found: {self.source}")

    def get_website_input(self):
        try:
            response = requests.get(self.source)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                paragraphs = soup.find_all('p')  # You can adjust this based on the HTML structure
                self.text = "\n".join([p.get_text() for p in paragraphs])
            else:
                print(f"Failed to retrieve content from the website. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_input(self):
        if self.mode == 'raw':
            self.text = input("Enter the raw text: ")
        elif self.mode == 'file':
            self.get_file_input()
        elif self.mode == 'website':
            self.get_website_input()
        else:
            print("Invalid mode. Please use 'raw', 'file', or 'website'.")