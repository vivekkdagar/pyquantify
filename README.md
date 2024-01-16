<div align='center'>
  <h1>Semantic Profiling</h1>
</div>

**NLPFreq** is a robust Command-Line Interface (CLI) tool designed for semantic profiling. It facilitates the analysis of raw text, files, or websites, offering enhanced data visualization, exploration, and integration capabilities.

<div align='center'>
  <h4><a href="https://github.com/vivekkdagar/NLPFreq/issues">Report Bug</a> <span> · </span> <a href="https://github.com/vivekkdagar/vivekkdagar/NLPFreq/issues">Request Feature</a></h4>
</div>

> Note: NLPFreq has not been tested on Windows-based systems yet.

## :notebook_with_decorative_cover: Table of Contents

1. [Requirements](#requirements)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
   - [Show Metrics](#show-metrics)
   - [Limit Analysis](#limit-analysis)
   - [Search Word](#search-word)
   - [Generate Word Cloud](#generate-word-cloud)
   - [Generate Word Frequency Plot](#generate-word-frequency-plot)
5. [FAQ](#question)
6. [Acknowledgements](#ack)

## :star2: Requirements

Ensure you meet the following requirements before installation:

```bash
pip install -r requirements.txt
```

## :dart: Features

- **Data Loading**: Load text data from various sources, including raw input, files, and websites, with interactive prompts for user input.
- **Text Preprocessing**: Tokenize and clean the text data, removing punctuation and converting words to lowercase.
- **Metrics Generation**: Calculate and display key metrics, including character count with and without spaces, sentence count, word count, and paragraph count.
- **Morphological Analysis**: Generate a detailed table of word morphology, including word rank, original form, lemmatized form, part-of-speech (POS) tag, percentage occurrence, and count.
- **Export Functionality**: Optionally export the generated metrics, frequency tables, and visualizations to files.
- **Word Cloud Visualization**: Create and display a word cloud visualization of the processed text data.
- **Word Frequency Chart**: Generate and visualize the frequency of the top 20 words in the text.
- **Interactive Commands**: Utilize command-line interface commands to perform actions such as displaying metrics, limiting results, searching for specific words, and generating visualizations.

## :toolbox: Installation

### Install from PyPI

You can install the `nlpfreq` package directly from PyPI using the following command:

```bash
pip install nlpfreq
```

### Build from Source

1. Clone the project:

```bash
git clone <repository_url>
cd NLPFreq
```

2. Build the package:

```bash
python3 setup.py sdist bdist_wheel
```

3. Install the package:

```bash
pip install dist/*.tar.gz
```

4. Run the simulation:

```bash
nlpfreq
```

## :toolbox: Usage

### Show Metrics

Display metrics generated from the loaded data:

```bash
nlpfreq show-metrics --export
```

- `--export`: Save metrics to files.

### Limit Analysis

Limit the analysis to the top `n` highest occurring words:

```bash
nlpfreq limit --n <n>
```

- `--n`: Specify the number of top words to display.

### Search Word

Search for a specific word in the morphological data:

```bash
nlpfreq search-word --word <word>
```

- `--word`: Specify the word to search for.

### Generate Word Cloud

Generate and display a word cloud visualization:

```bash
nlpfreq generate-wordcloud --export
```

- `--export`: Save the word cloud image.

### Generate Word Frequency Plot

Generate and display a word frequency plot:

```bash
nlpfreq generate-wordfreq-plot --export
```

- `--export`: Save the word frequency plot.

## :question: FAQ

### Q: What is NLPFreq's Semantic Profiler?

A: NLPFreq's Semantic Profiler is a tool designed for in-depth analysis of textual data, focusing on extracting meaning and linguistic insights. It provides features like word frequency, morphology, and metrics generation, enhancing data exploration and visualization.

### Q: Why Develop NLPFreq as a Semantic Profiler?

A: NLPFreq was created for the ADSA subject in the fifth semester of college. The goal was to offer a versatile NLP tool, empowering users to analyze and profile text efficiently. The tool's features aim to deepen understanding and exploration of linguistic aspects within textual data.

### Q: Why Did NLPFreq Evolve from a Word Frequency Counter?

A: Originally conceived as a word frequency counter, NLPFreq's development took a different direction. The decision to expand its capabilities was driven by the desire to create a more comprehensive tool for natural language processing. The project evolved to encompass semantic profiling, offering a richer set of features such as morphology analysis, metrics generation, and enhanced data visualization. This shift aimed to provide users with a more powerful and versatile solution for exploring and understanding textual data beyond simple word frequency analysis.

## :ack: Acknowledgements

[Acknowledge contributors, libraries used, or any other relevant acknowledgments here.]
