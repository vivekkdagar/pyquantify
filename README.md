
# pyquantify

Pyquantify is a powerful CLI tool for semantic analysis. It leverages natural language processing to unveil insights from text, files, or websites, empowering sophisticated data visualization and exploration.


## Badges

![Pyquantify Version](https://img.shields.io/badge/PyQuantify-1.2.0-brightgreen)

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)

[![Python 3](https://img.shields.io/badge/Python-3-brightgreen)](https://www.python.org/)

## Table Of Contents
   * [Features](#features)
   * [Installation](#installation)
         - [Install pyquantify with pip](#install-pyquantify-with-pip)
         - [or you can build locally](#or-you-can-build-locally)
   * [Before running pyquantify](#before-running-pyquantify)
   * [Usage/Examples](#usageexamples)
   * [FAQ](#faq)
   * [Screenshots](#screenshots)
   * [Acknowledgements](#acknowledgements)


## Demo

<img src="https://github.com/vivekkdagar/pyquantify/blob/main/assets/screenshots/menu.png">


## Features

1. **Text Summarization**:
   - Utilizes the BERT model for summarizing text.
   - Provides caching functionality to speed up summarization for previously processed text.
   - Supports exporting summaries to text files.

2. **Text Analysis**:
   - Preprocesses text data including tokenization and part-of-speech tagging.
   - Generates various metrics such as character count, word count, sentence count, etc.
   - Analyzes morphological data including lemmatized forms, part-of-speech tags, and word frequencies.
   - Performs sentiment analysis using the TextBlob library.
   - Visualizes data through word clouds and word frequency charts.

3. **Text Processing**:
   - Offers functionality for cleaning and preprocessing text data.
   - Implements functions for generating word clouds and word frequency charts.
   - Calculates cosine similarity between two texts.

4. **Data Loading and Exporting**:
   - Supports loading text data from raw input, files, or websites.
   - Provides export functionality for analyzed data, summaries, sentiment analysis results, and keywords extracted from text.

5. **CLI Interface**:
   - Implements a command-line interface (CLI) using Click library.
   - Offers commands for various text analysis and summarization tasks, including data visualization and sentiment analysis.
   - Provides options for specifying data loading mode and exporting analysis results.

6. **Parallel Processing**: Utilizes multiprocessing and concurrent.futures for parallel processing of tasks, improving performance for tasks like sentiment analysis and summarization.

7. **Unit Testing**:
   - Includes unit tests for different modules and functionalities using the `unittest` framework.
   - Uses mocking to isolate and test individual components such as data loading, summarization, and exporting.

8. **Exception Handling and Error Reporting**:
   - Handles exceptions gracefully and provides informative error messages.
   - Reports errors such as unsupported operating systems, file not found, and invalid input modes.
## Installation

#### Install pyquantify with pip

```bash
  pip install pyquantify
```
    
#### or you can build locally

Clone the project

```bash
  git clone https://github.com/vivekkdagar/pyquantify.git
```

Go to the project directory

```bash
  cd pyquantify
```

Build the package:

```bash
  python3 -m build
```

Install the package:

```bash
  pip install dist/*gz
```


## Before running pyquantify

Clone the project

```bash
  git clone https://github.com/vivekkdagar/pyquantify.git
```

Go to the project directory

```bash
  cd pyquantify
```

Run the script nltk_datasets.py in scripts directory

```bash
  python3 nltk_datasets.py
```

Download dataset for spacy

```bash
  python3 -m spacy download en_core_web_sm
```


## Usage/Examples

Pyquantify provides several commands for analyzing and visualizing text data. Below is a guide on how to use the key functionalities:

1. **Search for a Specific Word in Morphological Analysis:**

   ```bash
   pyquantify search-word --mode [raw/file/website] --word [desired_word]
   ```

   - `--mode`: Specify the data loading mode (raw input, file, or website).
   - `--word`: Specify the word you want to search for.

2. **Generate Word Frequency Plot:**

   ```bash
   pyquantify visualize --mode [raw/file/website] --freq-chart --export
   ```

   - `--mode`: Specify the data loading mode (raw input, file, or website).
   - `--freq-chart`: Flag to generate word frequency chart.
   - `--export`: Optional flag to export the frequency plot to a file.

3. **Generate Word Cloud:**

   ```bash
   pyquantify visualize --mode [raw/file/website] --wordcloud --export
   ```

   - `--mode`: Specify the data loading mode (raw input, file, or website).
   - `--wordcloud`: Flag to generate word cloud.
   - `--export`: Optional flag to export the word cloud to a file.

4. **Text Analysis and Metrics Generation:**

   ```bash
   pyquantify analyze --mode [raw/file/website] --n [number_of_rows] --export
   ```

   - `--mode`: Specify the data loading mode (raw input, file, or website).
   - `--n`: Optional parameter to display a specific number of rows in the analysis.
   - `--export`: Optional flag to export the analysis results to files.

5. **Summarize Text:**

   ```bash
   pyquantify summarize --mode [raw/file/website] --export
   ```

   - `--mode`: Specify the data loading mode (raw input, file, or website).
   - `--export`: Optional flag to export the summary to a file.

6. **Sentiment Analysis**

   ```bash
   pyquantify sentiment-analysis --mode [raw/file/website] --export
   ```

   - `--mode`: Specify the data loading mode (raw input, file, or website).
   - `--export`: Optional flag to export the summary to a file.

7. **View the pyquantify git page**

```bash
pyquantify git
```

8. **Extract keywords from the data**

```bash
pyquantify keywords --mode [raw/file/website] --export
```

- `--mode`: Specify the data loading mode (raw input, file, or website).
- `--export`: Optional flag to export the extracted keywords to a file.


9. **Calculate Cosine Similarity:**

   ```bash
   pyquantify similarity --mode [raw/file/website] --other [raw/file/website]
   ```

   - `--mode`: Specify the data loading mode for the first text (raw input, file, or website).
   - `--other`: Specify the data loading mode for the second text (raw input, file, or website).

Feel free to explore additional options and functionalities by checking the help documentation for each command:

```bash
pyquantify [command] --help
```


## FAQ


### Q: What is Pyquantify?

Pyquantify is a tool designed for in-depth analysis of textual data, focusing on extracting meaning and linguistic insights. It provides features like word frequency, morphology, and metrics generation, enhancing data exploration and visualization.

### Q: Why Develop Pyquantify as a Semantic Profiler?

Pyquantify was created for the DSA subject in the fifth semester of college. The goal was to offer a versatile NLP tool, empowering users to analyze and profile text efficiently. The tool's features aim to deepen understanding and exploration of linguistic aspects within textual data.

### Q: Why Did Pyquantify evolve from a Word Frequency Counter?

Originally conceived as a word frequency counter, Pyquantify's development took a different direction. The decision to expand its capabilities was driven by the desire to create a more comprehensive tool for natural language processing. The project evolved to encompass semantic profiling, offering a richer set of features such as morphology analysis, metrics generation, and enhanced data visualization. This shift aimed to provide users with a more powerful and versatile solution for exploring and understanding textual data beyond simple word frequency analysis.

### Q: Why the name change from NLPFreq to Pyquantify?

NLPFreq felt limiting and didn't capture the full scope of the project. Pyquantify more accurately reflects its capabilities as a Python-based tool for quantitative data analysis.
## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## Acknowledgements

- [NeuralNine's Publish Your Own Python Package](https://www.youtube.com/watch?v=tEFkHEKypLI)
- [Github Readme Generator](https://readme.so/)
- [Table of Content Generator](https://derlin.github.io/bitdowntoc/)
