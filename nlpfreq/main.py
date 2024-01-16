import click
from nlpfreq.core.input_handler import *
from nlpfreq.core.text_processor import *
import json
import os
from tabulate import tabulate


@click.group()
def cli():
    pass


def load_data_callback(mode=None, source=None):
    if mode is None:
        mode = input("Enter mode (raw, file, website): ").lower()
    if mode not in ['raw', 'file', 'website']:
        raise ValueError("Invalid mode. Choose from 'raw', 'file', or 'website'.")

    if mode in ['file', 'website'] and not source:
        source = input("Enter the source:")

    input_handler = InputHandler(mode=mode, source=source)
    input_handler.get_input()
    text_processor = TextProcessor(input_handler.text)
    text_processor.preprocess()
    click.echo("Data loaded successfully.")

    # Generating data
    text_processor.generate_metrics()
    text_processor.generate_morphological_data()

    # Saving to file
    processed_data = {'metrics': text_processor.metrics}
    with open('stats.json', 'w') as json_file, open('morph-table.txt', 'w') as file:
        json.dump(processed_data, json_file)
        file.write(text_processor.morphological_data)

    click.echo("Analysis generated!")

    return text_processor  # Return TextProcessor instance


@cli.command()
@click.option('--export', is_flag=True, default=False, help='Export data to files')
def show_metrics(export):
    try:
        load_data_callback()

        # Show Metrics
        with open('stats.json', 'r') as json_file:
            data = json.load(json_file)
            click.echo("\nMetrics:")
            click.echo(json.dumps(data['metrics'], indent=2))

        # Show Frequency Table
        with open('morph-table.txt', 'r') as table:
            data = table.read()
            click.echo('\n<Frequency table: >')
            click.echo(data)

        # Export data if requested
        if export:
            export_folder = get_export_folder()
            export_path_json = get_unique_filename(export_folder, 'stats.json')
            export_path_txt = get_unique_filename(export_folder, 'morph-table.txt')

            with open(export_path_json, 'w') as json_export_file:
                json.dump(data, json_export_file)

            with open(export_path_txt, 'w') as txt_export_file:
                txt_export_file.write(data)

            click.echo(f"Exported data to: {export_path_json} and {export_path_txt}")

    except FileNotFoundError:
        print("Data not loaded. Use 'load_data' command first.")


def get_export_folder():
    if os.name == 'posix':  # Linux
        return os.path.expanduser("~/Downloads/NLPFreq")
    elif os.name == 'nt':  # Windows
        return os.path.expanduser("~\\Downloads\\NLPFreq")
    else:
        raise Exception("Unsupported operating system")


def get_unique_filename(folder, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    unique_filename = filename

    while os.path.exists(os.path.join(folder, unique_filename)):
        unique_filename = f"{base}_{counter}{ext}"
        counter += 1

    return os.path.join(folder, unique_filename)


@cli.command()
@click.option('--n', default=10, help='Top n highest occuring words')
def limit(n):
    processor = load_data_callback()

    try:
        # Get morphological data
        morphological_data = processor.morphological_data
        rows = morphological_data.split('\n')

        # Extract header and data rows
        header = [row.strip() for row in rows[1].split('|') if row.strip()]
        data_rows = rows[3:]

        # Display top n rows
        click.echo(tabulate([row.strip().split('|')[1:] for row in data_rows[:n]], headers=header, tablefmt="pipe"))

    except FileNotFoundError:
        print("Data not loaded. Use 'load_data' command first.")


@cli.command()
@click.option('--word', prompt=True, help='Word to search for')
def search_word(word):
    # Load data and get TextProcessor instance
    processor = load_data_callback()

    try:
        # Search for the word in morphological data
        morphological_data = processor.morphological_data
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

    except FileNotFoundError:
        print("Data not loaded. Use 'load_data' command first.")


@cli.command()
@click.option('--export', is_flag=True, default=False, help='Export data to files')
def generate_wordcloud(export):
    try:
        text_processor = load_data_callback()

        # Generate Word Cloud
        export_folder = get_export_folder()
        export_path_img = get_unique_filename(export_folder, 'wordcloud.jpg')
        text_processor.plot_wordcloud(export=export, output_path=export_path_img)

    except FileNotFoundError:
        print("Data not loaded. Use 'load_data' command first.")


@cli.command()
@click.option('--export', is_flag=True, default=False, help='Export data to files')
def generate_wordfreq_plot(export):
    try:
        text_processor = load_data_callback()

        # Generate Word Frequency Plot
        export_folder = get_export_folder()
        export_path_img = get_unique_filename(export_folder, 'freqchart.jpg')
        text_processor.plot_word_frequency_chart(export=export, output_path=export_path_img)

    except FileNotFoundError:
        print("Data not loaded. Use 'load_data' command first.")


if __name__ == '__main__':
    cli()
