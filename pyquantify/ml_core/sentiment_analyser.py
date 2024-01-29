from textblob import TextBlob
from tabulate import tabulate


def get_sentiment_label(polarity):
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"


class SentimentAnalyzer:
    def __init__(self, data):
        self.data = data

    def get_sentiment_table(self):
        scores = []

        for sentence in self.data:
            blob = TextBlob(sentence)
            sentiment = get_sentiment_label(blob.sentiment.polarity)
            scores.append([sentence, sentiment, blob.sentiment.subjectivity])

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
