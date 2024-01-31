import warnings
import webbrowser
from tabulate import tabulate
import click
from .utils.input_handler import load_data
from .ml_core.bert_summarizer import CustomSummarizer
from .utils.export_manager import *
from .core.text_processor import TextProcessor
from lingua import Language, LanguageDetectorBuilder

mode_option = click.option("--mode", type=click.Choice(["raw", "file", "website"]), required=True,
                           help="Data loading mode (raw, file, website)")
export_option = click.option("--export", is_flag=True, default=False, help="Export to file")


@click.group()
@click.option('--git', is_flag=True, default=False, help='Go to github page')
def cli(git):
    if git:
        click.echo("Going to git page...")
        webbrowser.open("https://github.com/vivekkdagar/pyquantify")
        exit()


@cli.command()
@mode_option
@click.option('--word', prompt=True, required=True, help='Word to search for', type=str)
def search_word(mode, word):
    data = load_data(mode)

    parser = TextProcessor(data)
    parser.preprocess()

    parser.generate_morphological_data()
    morphological_data = parser.morphological_data

    rows = morphological_data.split('\n')
    header = [row.strip() for row in rows[1].split('|') if row.strip()]
    result_row = None

    for line in rows[3:]:
        if word.lower() in line:
            result_row = line.strip().split('|')
            break

    if result_row:
        result_data = [item.strip() for item in result_row if item]
        result_table = tabulate([result_data], headers=header, tablefmt="pipe")
        click.echo(result_table)
    else:
        click.echo(f"\nWord '{word}' not found in morphological table.")


@cli.command()
@mode_option
@export_option
@click.option('--freq-chart', is_flag=True, default=False, help='Generate word frequency chart only')
@click.option('--wordcloud', is_flag=True, default=False, help='Generate word cloud only')
def visualize(mode, export, freq_chart, wordcloud):
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
        parser.plot_word_frequency_chart(export=export, output_path=export_path_freq_chart)
        click.echo("\nFrequency plot of top 20 words generated!")

    if wordcloud:
        export_path_wordcloud = export_handler.generate_filename('wordcloud.jpg')
        parser.plot_wordcloud(export=export, output_path=export_path_wordcloud)
        click.echo("\nWordcloud generated!")


@cli.command()
@mode_option
@click.option('--n', help='Display n rows of morphological data', type=int)
@export_option
def analyze(mode, n, export):
    data = load_data(mode)
    detector = LanguageDetectorBuilder.from_all_languages().build()

    lang = detector.detect_language_of(data)
    if lang == Language.ENGLISH:
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
                click.echo(f"\nAnalysis exported to {dest1} and {dest2}")
        else:
            rows = parser.morphological_data.split('\n')
            header = [row.strip() for row in rows[1].split('|') if row.strip()]
            data_rows = rows[3:]
            click.echo(
                tabulate([row.strip().split('|')[1:] for row in data_rows[:n]], headers=header, tablefmt="pipe"))

            if export:
                raise Exception("Sorry, we don't export limited rows yet.")
    else:
        raise Exception(f"Currently we only support English! Your data had {lang} language")


@cli.command()
@mode_option
@export_option
def sentiment_analysis(mode, export):
    data = load_data(mode)

    detector = LanguageDetectorBuilder.from_all_languages().build()
    lang = detector.detect_language_of(data)

    if lang == Language.ENGLISH:
        parser = TextProcessor(data)
        parser.generate_sentiment_data()

        click.echo("Sentiment Analysis performed successfully!\n{}: ".format(parser.sentiment_data))

        if export:
            export_loc = get_export_folder()
            manager = ExportManager(export_loc)
            dest = manager.export('sentiment.txt', parser.sentiment_data)
            click.echo(f"Sentiment Analysis results exported to {dest}")


@cli.command()
@mode_option
@export_option
def summarize(mode, export):
    data = load_data(mode)

    warnings.filterwarnings("ignore", category=FutureWarning)

    obj = CustomSummarizer(data)

    dest = None
    if export:
        dest = get_export_folder()

    summary = obj.summarize(dest)
    click.echo("\nSummary: {}".format(summary[0]))

    if dest is not None:
        click.echo(f"Summary exported to {summary[1]}")
