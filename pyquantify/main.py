import warnings
import webbrowser
from tabulate import tabulate
import click
from .utils.input_handler import load_data
from .bert_summarizer import CustomSummarizer
from .utils.export_manager import *
from .core import TextProcessor
from tqdm import tqdm
from langid import classify
import time

mode_option = click.option("--mode", type=click.Choice(["raw", "file", "website"]), required=True,
                           help="Data loading mode (raw, file, website)")
export_option = click.option("--export", is_flag=True, default=False, help="Export to file")


@click.group()
def cli():
    """
    PyQuantify CLI tool for text analysis and summarization.
    """
    pass


@cli.command()
def git():
    """
    Open the GitHub page of PyQuantify.
    """
    click.echo("Going to git page...")
    webbrowser.open("https://github.com/vivekkdagar/pyquantify")
    exit()


@cli.command()
@mode_option
@click.option('--word', prompt=True, required=True, help='Word to search for', type=str)
def search_word(mode, word):
    """
    Search for a word in data.
    """
    data = load_data(mode)

    parser = TextProcessor(data)
    parser.preprocess()

    parser.generate_morphological_data()
    morphological_data = parser.morphological_data

    rows = morphological_data.split('\n')
    header = [row.strip() for row in rows[1].split('|') if row.strip()]
    result_row = None

    total_rows = len(rows[3:])
    with tqdm(total=total_rows, desc="\nSearching for word in morphological data", unit=" row") as progress_bar:
        for line in rows[3:]:
            if word.lower() in line:
                result_row = line.strip().split('|')
                break
            progress_bar.update(1)
            import time
            time.sleep(0.01)

    if result_row:
        result_data = [item.strip() for item in result_row if item]
        result_table = tabulate([result_data], headers=header, tablefmt="pipe")
        click.echo("\n")
        click.echo(result_table)
    else:
        click.echo(f"\nWord '{word}' not found in morphological table.\n")


@cli.command()
@mode_option
@export_option
@click.option('--freq-chart', is_flag=True, default=False, help='Generate word frequency chart only')
@click.option('--wordcloud', is_flag=True, default=False, help='Generate word cloud only')
def visualize(mode, export, freq_chart, wordcloud):
    """
    Visualize data by generating charts.
    """
    if not (freq_chart or wordcloud):
        click.echo("Error: Please specify at least one of --freq-chart or --wordcloud")
        return

    data = load_data(mode)

    parser = TextProcessor(data)
    parser.preprocess()

    export_folder = get_export_folder()
    export_handler = ExportManager(export_folder)

    if freq_chart:
        export_path_freq_chart = export_handler.generate_filename('freqchart.jpg')
        with click.progressbar(length=1, label="Generating word frequency chart") as progress_bar:
            parser.plot_word_frequency_chart(export=export, output_path=export_path_freq_chart)
            progress_bar.update(1)
            time.sleep(0.01)
        click.echo("\nFrequency plot of top 20 words generated!")

    if wordcloud:
        export_path_wordcloud = export_handler.generate_filename('wordcloud.jpg')
        with click.progressbar(length=1, label="Generating wordcloud") as progress_bar:
            parser.plot_wordcloud(export=export, output_path=export_path_wordcloud)
            progress_bar.update(1)
            time.sleep(0.01)
        click.echo("\nWordcloud generated!")


@cli.command()
@mode_option
@click.option('--n', help='Display n rows of morphological data', type=int)
@export_option
def analyze(mode, n, export):
    """
    Analyze text data.
    """
    data = load_data(mode)

    lang = classify(data)
    click.echo(f"Language of your data is: {lang[0]}")

    if lang[0] == 'en':
        parser = TextProcessor(data)
        parser.preprocess()

        parser.generate_metrics()
        parser.generate_morphological_data()

        if n is None:
            click.echo("Generated metrics is: \n{}\n{}".format(parser.metrics, parser.morphological_data))

            if export:
                export_loc = get_export_folder()
                manager = ExportManager(export_loc)

                dest1 = manager.export('table.txt', parser.morphological_data)
                dest2 = manager.export('stats.json', parser.metrics)
                click.echo(f"\nAnalysis exported to {dest1} and {dest2}\n")
        else:
            rows = parser.morphological_data.split('\n')
            header = [row.strip() for row in rows[1].split('|') if row.strip()]
            data_rows = rows[3:]

            # Add tqdm for progress bar
            with tqdm(total=n, desc="Processing Rows") as pbar:
                for row in data_rows[:n]:
                    # Simulate processing time
                    pbar.update(1)
                    click.echo(row.strip().split('|')[1:], nl=False)
                    click.echo('\n', nl=False)

                    time.sleep(0.01)

            if export:
                raise Exception("Sorry, we don't export limited rows yet.\n")
    else:
        raise Exception(f"Currently we only support English! Your data had {lang} language\n")


@cli.command()
@mode_option
@export_option
def sentiment_analysis(mode, export):
    """
    Perform sentiment analysis.
    """
    data = load_data(mode)

    lang = classify(data)

    if lang[0] == "en":
        parser = TextProcessor(data)
        parser.generate_sentiment_data()

        click.echo("Sentiment Analysis performed successfully!\n{}: ".format(parser.sentiment_data))

        if export:
            export_loc = get_export_folder()
            manager = ExportManager(export_loc)
            dest = manager.export('sentiment.txt', parser.sentiment_data)
            click.echo(f"Sentiment Analysis results exported to {dest}\n")


@cli.command()
@mode_option
@export_option
def summarize(mode, export):
    """
    Summarize text data.
    """
    data = load_data(mode)

    warnings.filterwarnings("ignore")

    obj = CustomSummarizer(data)

    dest = None
    if export:
        dest = get_export_folder()

    summary = obj.summarize(dest)
    click.echo("\nSummary: {}\n".format(summary[0]))

    if dest is not None:
        click.echo(f"Summary exported to {summary[1]}\n")


@cli.command()
@mode_option
@export_option
def keywords(mode, export):
    """
    Extract keywords from data.
    """
    data = load_data(mode)

    from rake_nltk import Rake
    # Initialize Rake to extract keywords
    rake = Rake()

    # Extract keywords from the text
    rake.extract_keywords_from_text(data)

    # Get ranked keywords
    ranked_keywords = rake.get_ranked_phrases()

    # Print or export the keywords
    if ranked_keywords:
        click.echo("\nExtracted Keywords:")
        for keyword in ranked_keywords:
            click.echo(keyword)
        if export:
            export_loc = get_export_folder()
            manager = ExportManager(export_loc)
            dest = manager.export('keywords.txt', "\n".join(ranked_keywords))
            click.echo(f"Keywords exported to {dest}\n")
    else:
        click.echo("\nNo keywords extracted.\n")


@cli.command()
@mode_option
@click.option('--other', type=click.Choice(["raw", "file", "website"]), required=True,
              help="Mode for providing the second text (raw, file, website)")
def similarity(mode, other):
    """
    Calculate the cosine similarity.
    """
    # Load data
    data = load_data(mode)

    second_text = load_data(other)

    # Process the loaded data and the second text
    parser_data = TextProcessor(data)
    parser_data.preprocess()
    parser_second = TextProcessor(second_text)
    parser_second.preprocess()

    # Calculate cosine similarity
    similarity_score = parser_data.calculate_cosine_similarity(parser_second.text)

    # Output the similarity score
    click.echo(f"\nCosine Similarity between the loaded data and the provided text: {similarity_score}\n")

    # Interpret the similarity score
    if similarity_score == 1:
        click.echo("The texts are highly similar.\n")
    elif similarity_score == -1:
        click.echo("The texts are highly dissimilar.\n")
    elif similarity_score == 0:
        click.echo("The texts are independent.\n")
    else:
        click.echo("The texts have moderate similarity or dissimilarity.\n")
