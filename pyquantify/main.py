import click
import os
from pyquantify.utils.input_handler import *
from pyquantify.core.text_processor import TextProcessor
from pyquantify.utils.export_manager import ExportManager
from tabulate import tabulate
from pyquantify.ml_core.bert_summarizer import CustomSummarizer
import webbrowser

mode_option = click.option('--mode', type=click.Choice(['raw', 'file', 'website']), required=True,
                           help='Data loading mode (raw, file, website)')


@click.group()
@click.option('--git', is_flag=True, default=False, help='Go to github page')
def cli(git):
    if git:
        click.echo("Going to git page...")
        webbrowser.open("https://github.com/vivekkdagar/pyquantify")
        return
    else:
        pass


@cli.command()
@mode_option
@click.option('--export', is_flag=True, default=False, help='Export visualizations to files')
@click.option('--freq-chart', is_flag=True, default=False, help='Generate word frequency chart only')
@click.option('--wordcloud', is_flag=True, default=False, help='Generate word cloud only')
def visualize(mode, export, freq_chart, wordcloud):
    if not (freq_chart or wordcloud):
        click.echo("Error: Please specify at least one of --freq-chart or --wordcloud")
        return

    data = load(mode)

    parser = TextProcessor(data)
    parser.preprocess()

    export_folder = ExportManager.get_export_folder()

    if freq_chart:
        export_path_freq_chart = ExportManager(export_folder).generate_filename('freqchart.jpg')
        parser.plot_word_frequency_chart(export=export, output_path=export_path_freq_chart)
        click.echo("Frequency plot of top 20 words generated!")

    if wordcloud:
        export_path_wordcloud = ExportManager(export_folder).generate_filename('wordcloud.jpg')
        parser.plot_wordcloud(export=export, output_path=export_path_wordcloud)
        click.echo("Wordcloud generated!")


@cli.command()
@mode_option
@click.option('--word', prompt=True, required=True, help='Word to search for', type=str)
def search_word(mode, word):
    data = load(mode)

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
        click.echo(f"Word '{word}' not found in morphological table.")


@cli.command()
@mode_option
@click.option('--n', help='Display n rows of morphological data', type=int)
@click.option('--export', is_flag=True, default=False, help='Export metrics to file')
def analyze(mode, n, export):
    data = load(mode)
    # ld = LanguageDetector(data)
    # ld.load_model('model.joblib')
    result = "English"

    if result == "English":
        parser = TextProcessor(data)
        parser.preprocess()
        parser.generate_metrics()
        parser.generate_morphological_data()
        parser.generate_sentiment_data()

        if n is None:
            click.echo("Generated metrics is: \n{}\n{}\n{}".format(parser.metrics, parser.morphological_data,
                                                                   parser.sentiment_data))

            if export:
                export_folder = ExportManager.get_export_folder()
                manager = ExportManager(export_folder)

                if not os.path.exists(export_folder):
                    os.makedirs(export_folder)

                export_path_txt = manager.generate_filename('table.txt')
                export_path_json = manager.generate_filename('stats.json')
                export_path_sentiment = manager.generate_filename('sentiment.txt')
                manager.export(export_path_json, parser.metrics)
                manager.export(export_path_txt, parser.morphological_data)
                manager.export(export_path_sentiment, parser.sentiment_data)
                click.echo(f"\nAnalysis exported to {export_path_txt}, {export_path_json} and {export_path_sentiment}")
        else:
            rows = parser.morphological_data.split('\n')
            header = [row.strip() for row in rows[1].split('|') if row.strip()]
            data_rows = rows[3:]
            click.echo(tabulate([row.strip().split('|')[1:] for row in data_rows[:n]], headers=header, tablefmt="pipe"))

            if export:
                raise Exception("Sorry, we don't export limited rows yet.")
    else:
        raise Exception("Currently we only support English!")


@cli.command()
@mode_option
@click.option('--export', is_flag=True, default=False, help='Export summary to file')
def summarize(mode, export):
    data = load(mode)

    obj = CustomSummarizer(data)
    destination = None
    if export:
        destination = ExportManager.get_export_folder()
    summary = obj.summarize(destination)
    click.echo("Summary: {}".format(summary))
    if destination is not None:
        click.echo(f"Summary exported to {destination} \\ {obj.export_path_txt}")
