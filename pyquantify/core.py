import time
from collections import Counter

import click
import matplotlib.pyplot as plt
import nltk.tokenize as tokenizer
import seaborn as sns
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tabulate import tabulate
from tqdm import tqdm
from wordcloud import WordCloud

from .sentiment_analyzer import SentimentAnalyzer
from .utils.misc import expand_pos_tag


class TextProcessor:
    def __init__(self, text):
        self.cleaned_data = None
        self.text = text
        self.metrics = None
        self.morphological_data = None
        self.sentiment_data = str()

    def preprocess(self):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(self.text)

        # Initialize a progress bar with the total number of tokens
        with tqdm(total=len(doc), desc="Preprocessing Text") as pbar:
            # Process each token in the document
            self.cleaned_data = []
            for token in doc:
                # Check if the token is alphabetic
                if token.is_alpha:
                    self.cleaned_data.append(token.text)

                # Update the progress bar
                pbar.update(1)
                time.sleep(0.01)

    def generate_metrics(self):
        char_with_space = len(self.text)
        char_without_space = sum(len(word) for word in self.text.split())
        sentence_count = len(list(spacy.load("en_core_web_sm")(self.text).sents))
        word_count = len(self.cleaned_data)
        paragraphs_count = self.text.count('\n') + 1

        self.metrics = {
            'char_with_space': char_with_space,
            'char_without_space': char_without_space,
            'sentence_count': sentence_count,
            'word_count': word_count,
            'paragraphs_count': paragraphs_count
        }

    def generate_morphological_data(self):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(" ".join(self.cleaned_data))

        table_data = []
        total_tokens = len(list(doc))
        with tqdm(total=total_tokens, desc="Generating Morphological Data") as pbar:
            for rank, token in enumerate(doc, start=1):
                lemmatized_form = token.lemma_
                pos_tag = expand_pos_tag(token.pos_)

                # Filter out non-alphabetic tokens
                if token.is_alpha:
                    word = token.text
                    count = sum(1 for t in self.cleaned_data if t == word)
                    percent_occurrence = (count / len(self.cleaned_data)) * 100

                    table_data.append([rank, word, lemmatized_form, pos_tag, percent_occurrence, count])
                import time
                time.sleep(0.01)
                pbar.update(1)

        headers = ["Rank", "Word", "Lemmatized Form", "POS Tag", "% Occurrence", "Count"]
        self.morphological_data = tabulate(table_data, headers=headers, tablefmt="pretty")

    def generate_sentiment_data(self):
        analyzer = SentimentAnalyzer(tokenizer.sent_tokenize(self.text))
        self.sentiment_data = str(analyzer)

    def plot_wordcloud(self, export=False, output_path=None):
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(self.cleaned_data))

        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')

        # Save Word Cloud image if requested
        if export and output_path:
            plt.savefig(output_path)
            click.echo(f"Exported Word Cloud image to: {output_path}")

        plt.show()

    def plot_word_frequency_chart(self, export=False, output_path=None):
        word_freq_counter = Counter(self.cleaned_data)
        most_common_words = word_freq_counter.most_common(20)

        plt.figure(figsize=(12, 6))
        sns.barplot(x=[word[0] for word in most_common_words],
                    y=[word[1] for word in most_common_words])
        plt.xlabel('Word')
        plt.ylabel('Frequency')
        plt.title('Top 20 Words Frequency')
        plt.xticks(rotation=45)

        # Save Word Frequency chart if requested
        if export and output_path:
            plt.savefig(output_path)
            click.echo(f"Exported Word Frequency chart to: {output_path}")

        plt.show()

    def calculate_cosine_similarity(self, other_text):
        # Tokenize and preprocess the other text
        other_cleaned_data = [token.text for token in spacy.load("en_core_web_sm")(other_text) if token.is_alpha]
        other_text = ' '.join(other_cleaned_data)

        # Create a CountVectorizer instance
        vectorizer = CountVectorizer().fit([self.text, other_text])

        # Transform documents to a matrix of token counts
        vectorized_docs = vectorizer.transform([self.text, other_text])

        # Calculate cosine similarity
        cosine_similarities = cosine_similarity(vectorized_docs)

        # Wrap the loop with tqdm for progress bar
        with tqdm(total=vectorized_docs.shape[0] * vectorized_docs.shape[1],
                  desc="Calculating Cosine Similarity") as pbar:
            for i in range(vectorized_docs.shape[0]):
                for j in range(vectorized_docs.shape[1]):
                    # Introduce a slight delay for simulating progress
                    time.sleep(0.01)
                    pbar.update(1)

        return cosine_similarities[0][1]
