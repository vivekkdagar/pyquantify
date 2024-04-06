from summarizer import Summarizer
#from .utils.export_manager import ExportManager
import torch


class CustomSummarizer:
    def __init__(self, text):
        self.export_path_txt = None
        self.text = text
        # Load the summarizer model once during initialization
        self.parser = Summarizer()
        # Use GPU if available
        self.parser.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        # Initialize a dictionary to cache summarization results
        self.summary_cache = {}

    def summarize(self, loc=None):
        # Check if the summary for the current text is already cached
        if self.text in self.summary_cache:
            summary = self.summary_cache[self.text]
        else:
            # Generate the summary using the summarizer model
            summary = self.parser(self.text)
            # Cache the summary for future use
            self.summary_cache[self.text] = summary

        dest = None
        #if loc:
         #   manager = ExportManager(loc)
          #  dest = manager.export('summary.txt', summary)
        return [summary, dest]


# Example usage:
if __name__ == "__main__":
    # Sample text
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
