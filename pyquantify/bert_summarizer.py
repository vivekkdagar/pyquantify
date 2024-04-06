import sqlite3
from summarizer import Summarizer
from .utils.export_manager import ExportManager
import warnings
import os
from tqdm import tqdm
import time

warnings.filterwarnings("ignore")


def get_cache_folder():
    """
    Returns the path to the cache folder based on the operating system.

    Returns:
        str: Path to the cache folder.

    Raises:
        Exception: If the operating system is not supported.
    """
    if os.name == 'posix':  # Linux
        return os.path.expanduser("~/Documents/pyquantify/cache")
    elif os.name == 'nt':  # Windows
        return os.path.expanduser("~\\Documents\\pyquantify\\cache")
    raise Exception("Unsupported operating system\n")


class CustomSummarizer:
    """
    A custom summarizer class that utilizes a cache for faster summarization.
    """
    def __init__(self, data):
        """
        Initializes the CustomSummarizer.

        Args:
            data (str): The text to be summarized.
        """
        self.text = data
        self.db_filename = os.path.join(get_cache_folder(), 'summarization_cache.db')
        os.makedirs(os.path.dirname(self.db_filename), exist_ok=True)
        self.conn = sqlite3.connect(self.db_filename)
        self.create_table()

    def create_table(self):
        """
        Creates the summarization cache table if it does not exist.
        """
        cursor = self.conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS summarization_cache (text TEXT PRIMARY KEY, res TEXT)')
        self.conn.commit()

    def summarize(self, loc=None):
        """
        Summarizes the text and optionally exports the summary to a file.

        Args:
            loc (str, optional): The location to export the summary.

        Returns:
            tuple: A tuple containing the summary text and the destination file path if exported.
        """
        cursor = self.conn.cursor()
        cursor.execute('SELECT res FROM summarization_cache WHERE text = ?', (self.text,))
        cached_summary = cursor.fetchone()
        if cached_summary:
            res = cached_summary[0]
        else:
            summarizer = Summarizer()
            with tqdm(total=100, desc="Summarizing") as pbar:
                res = summarizer(self.text)
                pbar.update(100)
            cursor.execute('INSERT INTO summarization_cache (text, res) VALUES (?, ?)', (self.text, res))
            self.conn.commit()
        time.sleep(0.01)

        dest = None
        if loc:
            manager = ExportManager(loc)
            dest = manager.export('summary.txt', res)
        return [res, dest]

    def __del__(self):
        """
        Closes the database connection when the instance is deleted.
        """
        self.conn.close()


# Example usage:
if __name__ == "__main__":
    text = ("Natural Language Processing (NLP) is a branch of artificial intelligence that focuses on the interaction "
            "between computers and human languages. It encompasses a wide range of tasks, including text "
            "understanding, machine translation, sentiment analysis, and language generation. NLP techniques enable "
            "computers to comprehend, interpret, and generate human language in a meaningful way, facilitating "
            "communication and interaction between humans and machines. Through the use of statistical models, "
            "machine learning algorithms, and linguistic rules, NLP systems can extract insights from large volumes "
            "of text data, automate tasks such as document classification and information retrieval, and even assist "
            "in language learning and translation. As NLP continues to advance, it plays an increasingly vital role "
            "in various domains, including healthcare, finance, customer service, and education, revolutionizing the "
            "way we interact with technology and access information.")
    summarizer = CustomSummarizer(text)
    summary, _ = summarizer.summarize()
    print(summary)
