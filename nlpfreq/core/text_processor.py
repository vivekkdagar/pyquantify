import nltk.tokenize as token
import nltk
from tabulate import tabulate
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns


def expand_pos_tag(pos_tag):
    pos_prefix = pos_tag[:2]

    pos_mapping = {
        'CC': 'Coordinating conjunction',
        'CD': 'Cardinal number',
        'DT': 'Determiner',
        'FW': 'Foreign word',
        'IN': 'Preposition or subordinating conjunction',
        'JJ': 'Adjective',
        'LS': 'List item marker',
        'MD': 'Modal',
        'NN': 'Noun',
        'PD': 'Predeterminer',
        'PR': 'Pronoun',
        'RB': 'Adverb',
        'RP': 'Particle',
        'SY': 'Symbol',
        'TO': 'to',
        'UH': 'Interjection',
        'VB': 'Verb',
        'WD': 'Wh-determiner',
        'WP': 'Wh-pronoun',
        'WR': 'Wh-adverb',
        'Unknown': 'Unknown POS Tag',
    }

    return pos_mapping.get(pos_prefix, pos_mapping['Unknown'])


class TextProcessor:
    _instances = {}

    def __new__(cls, text=''):
        if text not in cls._instances:
            cls._instances[text] = super(TextProcessor, cls).__new__(cls)
            return cls._instances[text]
        else:
            return cls._instances[text]

    def __init__(self, text=''):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.text = text
            self.cleaned_data = list()
            self.metrics = None
            self.morphological_data = None

    def preprocess(self):
        sentences = token.sent_tokenize(self.text.lower())

        # Word Tokenization and remove punctuation
        for sentence in sentences:
            words = token.word_tokenize(sentence)
            words_without_punctuations = [word.lower() for word in words if word.isalnum()]
            self.cleaned_data.append(words_without_punctuations)

    def generate_metrics(self):
        char_with_space = len(self.text)
        char_without_space = sum(len(word) for word in self.text.split())
        sentence_count = len(token.sent_tokenize(self.text))
        word_count = sum(len(words) for words in self.cleaned_data)
        paragraphs_count = self.text.count('\n') + 1

        self. metrics = {
            'char_with_space': char_with_space,
            'char_without_space': char_without_space,
            'sentence_count': sentence_count,
            'word_count': word_count,
            'paragraphs_count': paragraphs_count
        }

    def generate_morphological_data(self):
        lemmatizer = nltk.stem.WordNetLemmatizer()
        word_freq_counter = nltk.FreqDist(word for words in self.cleaned_data for word in words)

        table_data = []
        for rank, (word, count) in enumerate(word_freq_counter.most_common(), start=1):
            lemmatized_word = lemmatizer.lemmatize(word)
            pos_tags = nltk.pos_tag([word])
            pos_tag = pos_tags[0][1]
            full_pos_tag = expand_pos_tag(pos_tag)
            percent_occurrence = (count / len(self.cleaned_data)) * 100

            table_data.append([rank, word, lemmatized_word, full_pos_tag, percent_occurrence, count])

        headers = ["Rank", "Word", "Lemmatized Form", "POS Tag", "% Occurrence", "Count"]
        self. morphological_data = tabulate(table_data, headers=headers, tablefmt="pretty")

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
