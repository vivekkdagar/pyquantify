import nltk
import nltk.tokenize as tokenizer
from tabulate import tabulate
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
import spacy
from pyquantify.misc import expand_pos_tag


class TextProcessor:
    def __init__(self, text):
        self.text = text
        self.cleaned_data = list()
        self.metrics = None
        self.morphological_data = None

    def preprocess(self):
        sentences = tokenizer.sent_tokenize(self.text.strip())

        # Word Tokenization and remove punctuation
        for sentence in sentences:
            words = tokenizer.word_tokenize(sentence)
            words_without_punctuations = [word for word in words if word.isalnum()]
            self.cleaned_data.append(words_without_punctuations)

    def generate_metrics(self):
        char_with_space = len(self.text)
        char_without_space = sum(len(word) for word in self.text.split())
        sentence_count = len(tokenizer.sent_tokenize(self.text))
        word_count = sum(len(words) for words in self.cleaned_data)
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
        lemmatizer = nltk.stem.WordNetLemmatizer()
        word_freq_counter = nltk.FreqDist(word for words in self.cleaned_data for word in words)

        table_data = []
        for rank, (word, count) in enumerate(word_freq_counter.most_common(), start=1):
            lemmatized_word = lemmatizer.lemmatize(word)
            pos_tags = nltk.pos_tag([word])
            pos_tag = pos_tags[0][1]
            full_pos_tag = expand_pos_tag(pos_tag)
            percent_occurrence = (count / len(self.cleaned_data)) * 100

            doc = nlp(word)
            ner_la = doc.ents[0].label_ if doc.ents else 'N/A'
            table_data.append([rank, word, lemmatized_word, full_pos_tag, ner_la, percent_occurrence, count])

        headers = ["Rank", "Word", "Lemmatized Form", "POS Tag", "NER Label", "% Occurrence", "Count"]
        self.morphological_data = tabulate(table_data, headers=headers, tablefmt="pretty")

    def plot_wordcloud(self, export=False, output_path=None):
        preprocessed_text = ' '.join([' '.join(words) for words in self.cleaned_data])
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(preprocessed_text)

        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')

        # Save Word Cloud image if requested
        if export and output_path:
            plt.savefig(output_path)
            print(f"Exported Word Cloud image to: {output_path}")

        plt.show()

    def plot_word_frequency_chart(self, export=False, output_path=None):
        word_freq_counter = nltk.FreqDist(word for words in self.cleaned_data for word in words)
        plt.figure(figsize=(12, 6))
        sns.barplot(x=[word[0] for word in word_freq_counter.most_common(20)],
                    y=[word[1] for word in word_freq_counter.most_common(20)])
        plt.xlabel('Word')
        plt.ylabel('Frequency')
        plt.title('Top 20 Words Frequency')
        plt.xticks(rotation=45)

        # Save Word Frequency chart if requested
        if export and output_path:
            plt.savefig(output_path)
            print(f"Exported Word Frequency chart to: {output_path}")

        plt.show()
