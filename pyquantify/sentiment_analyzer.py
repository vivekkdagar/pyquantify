import multiprocessing

from textblob import TextBlob
from tabulate import tabulate
from concurrent.futures import ProcessPoolExecutor
import time
import concurrent
from tqdm import tqdm


def get_sentiment_label(polarity):
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    return "Neutral"


def _analyze_sentence(sentence):
    blob = TextBlob(sentence)
    sentiment = get_sentiment_label(blob.sentiment.polarity)
    subjectivity = blob.sentiment.subjectivity

    # Display only the first 5 words of sentences that are more than 7 words long
    if len(sentence.split()) > 7:
        shortened_sentence = ' '.join(sentence.split()[:5]) + '...'
    else:
        shortened_sentence = sentence

    return [shortened_sentence, sentiment, subjectivity]


class SentimentAnalyzer:
    def __init__(self, data: list):
        self.data: list = data

    def get_sentiment_table(self):
        # Split data into chunks for parallel processing
        num_chunks = min(len(self.data),
                         multiprocessing.cpu_count())  # Adjust number of chunks based on available CPU cores
        chunk_size = len(self.data) // num_chunks
        data_chunks = [self.data[i:i + chunk_size] for i in range(0, len(self.data), chunk_size)]

        # Flatten the list of chunks
        flattened_chunks = [item for sublist in data_chunks for item in sublist]

        # Initialize a progress bar with the total number of chunks
        with tqdm(total=len(flattened_chunks), desc="Processing Sentiment Analysis") as pbar:
            # Use ProcessPoolExecutor for asynchronous processing
            with ProcessPoolExecutor() as executor:
                # Submit tasks for each chunk and asynchronously process them
                future_to_chunk = {executor.submit(_analyze_sentence, chunk): chunk for chunk in flattened_chunks}

                scores = []
                # Iterate over completed futures to collect results
                for future in concurrent.futures.as_completed(future_to_chunk):
                    chunk = future_to_chunk[future]
                    try:
                        score = future.result()
                        scores.append(score)
                    except Exception as exc:
                        print(f'Chunk {chunk} generated an exception: {exc}')
                    finally:
                        # Update the progress bar for each completed chunk
                        pbar.update(1)
                        # Introduce a slight delay for simulating progress
                        time.sleep(0.01)

        return scores

    def get_overall_sentiment(self):
        total = TextBlob(' '.join(self.data))
        overall = [["Overall", get_sentiment_label(total.sentiment.polarity), total.sentiment.subjectivity]]
        return overall

    def __str__(self):
        headers = ["Sentiment", "Subjectivity"]
        table = tabulate(self.get_sentiment_table(), headers=headers, tablefmt="pretty")

        output = str(table) + "\n\n"
        overall = self.get_overall_sentiment()
        output += tabulate(overall, headers=headers, tablefmt="pretty")
        return output
