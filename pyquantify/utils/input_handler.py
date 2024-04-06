# import requests
# from bs4 import BeautifulSoup
#
#
# def scrape_website(source):
#     try:
#         response = requests.get(source)
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, 'html.parser')
#             paragraphs = soup.find_all('p')  # Adjust based on HTML structure
#             return "\n".join([p.get_text() for p in paragraphs])
#         else:
#             print(f"Failed to retrieve content from website. Status code: {response.status_code}")
#             return None
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return None
#
#
# def load_file(source):
#     try:
#         with open(source, 'r', encoding='utf-8') as file:
#             return file.read()
#     except FileNotFoundError:
#         print(f"File not found: {source}")
#         return None
#
#
# def load_data(mode):
#     if mode == 'raw':
#         return input("Enter the raw text: ")
#     elif mode == 'website':
#         return scrape_website(input("Enter the source: "))  # Return directly
#     elif mode == 'file':
#         return load_file(input("Enter the source: "))  # Return directly
#     else:
#         raise Exception("Invalid mode. Please use 'raw', 'file', or 'website'.")
import asyncio
import aiohttp
import aiofiles
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import os

# Use requests.Session for reusing TCP connections
session = requests.Session()

async def scrape_website_async(source):
    try:
        async with aiohttp.ClientSession() as client_session:
            async with client_session.get(source) as response:
                if response.status == 200:
                    html = await response.text()
                    soup = BeautifulSoup(html, 'html.parser')
                    paragraphs = soup.find_all('p')
                    return "\n".join([p.get_text() for p in paragraphs])
                else:
                    print(f"Failed to retrieve content from website. Status code: {response.status}")
                    return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def scrape_website(source):
    try:
        response = session.get(source)
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

async def load_file_async(source):
    try:
        async with aiofiles.open(source, mode='r', encoding='utf-8') as file:
            return await file.read()
    except FileNotFoundError:
        print(f"File not found: {source}")
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
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

async def load_data_async(mode, source):
    if mode == 'website':
        return await scrape_website_async(source)
    elif mode == 'file':
        return await load_file_async(source)
    else:
        raise Exception("Invalid mode. Please use 'file' or 'website'.")

def load_data(mode, source):
    if mode == 'website':
        return scrape_website(source)
    elif mode == 'file':
        return load_file(source)
    else:
        raise Exception("Invalid mode. Please use 'file' or 'website'.")

async def scrape_website_wrapper(source):
    return await scrape_website_async(source)

def scrape_website_parallel(sources):
    with Pool() as pool:
        return pool.map(scrape_website, sources)

async def load_file_wrapper(source):
    return await load_file_async(source)

def load_file_parallel(sources):
    with Pool() as pool:
        return pool.map(load_file, sources)
