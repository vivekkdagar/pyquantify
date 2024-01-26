<div align='center'>

<h1>pyquantify</h1>
<p>Pyquantify is a powerful CLI tool for semantic analysis. It leverages natural language processing to unveil insights from text, files, or websites, empowering sophisticated data visualization and exploration.</p>

<h4> <a href="https://github.com/vivekkdagar/pyquantify/issues"> Report Bug </a> <span> · </span> <a href="https://github.com/vivekkdagar/pyquantify/issues"> Request Feature </a> </h4>


</div>
  
# :notebook_with_decorative_cover: Table of Contents

- [:camera: Demo screenshot](#srn)
- [:dart: Features](#feat)
- [:toolbox: Getting Started](#strt)
- [:toolbox: Installation](#insta)
- [:book: Usage Guide](#use)
- [:compass: Roadmap](#map)
- [:grey_question: FAQ](#ques)
- [:gem: Acknowledgements](#ack)



<h2><a id="srn"> :camera:</a> Demo screenshot</h2>
<div align="center"> <a href=""><img src="https://github.com/vivekkdagar/pyquantify/blob/main/assets/demo.png" alt='image' width='800'/></a> </div>


<h2><a id="feat">:dart:</a> Features</h2>

1. **Data Loading**: Load text data from raw input, files, or websites with interactive prompts for user input.

2. **Text Preprocessing**: Tokenize and clean the text data by removing punctuation and converting words to lowercase.

3. **Metrics Generation**: Calculate and display key metrics, including character count (with and without spaces), sentence count, word count, and paragraph count.

4. **Morphological Analysis**: Generate a detailed table of word morphology, including word rank, original form, lemmatized form, part-of-speech (POS) tag, percentage occurrence, and count.

5. **Export Functionality**: Optionally export generated metrics, frequency tables, and visualizations to files.

6. **Word Cloud Visualization**: Create and display a word cloud visualization of processed text data.

7. **Word Frequency Chart**: Generate and visualize the frequency of the top 20 words in the text.

8. **Interactive Commands**: Utilize command-line interface commands for actions like displaying metrics, limiting results, searching for specific words, and generating visualizations.

9. **Summarize Text**: Summarize text using a BERT Extractive Summarizer.


<h2><a id="strt"> :toolbox:</a> Getting Started</h2>

### :bangbang: Prerequisites

Ensure you meet the following requirements before installation (if you're building from source):

```bash
pip install -r requirements.txt
```

<h2><a id="insta"> :toolbox:</a> Installation</h2>

<h3><a id="pypi"> Install from PyPI</a></h3>

You can install the `pyquantify` package directly from PyPI using the following command:

```bash
pip install pyquantify
```

<h3><a id="src"> Build from Source</a></h3>

1. Clone the project:

```bash
git clone <repository_url>
cd pyquantify
```

2. Build the package:

```bash
python3 setup.py sdist bdist_wheel
```

3. Install the package:

```bash
pip install dist/*.tar.gz
```

4. Run the tool in terminal:

```bash
pyquantify
```
<h2><a id="use"> :book: Usage Guide</a></h3>

Pyquantify provides several commands for analyzing and visualizing text data. Below is a guide on how to use the key functionalities:

### 1. Generate Word Frequency Plot

To generate a word frequency plot for the top 20 words in the text, use the following command:

```bash
pyquantify generate-freq_plot --mode [raw/file/website] --export
```

- `--mode`: Specify the data loading mode (raw input, file, or website).
- `--export`: Optional flag to export the frequency plot to a file.
<br>

### 2. Generate Word Cloud

Create and display a word cloud visualization of the processed text data with the following command:

```bash
pyquantify generate-wordcloud --mode [raw/file/website] --export
```

- `--mode`: Specify the data loading mode (raw input, file, or website).
- `--export`: Optional flag to export the word cloud to a file.
<br>

### 3. Search for a Specific Word in Morphological Analysis

To search for a specific word in the detailed table of word morphology, use the following command:

```bash
pyquantify search-word --mode [raw/file/website] --word [desired_word]
```

- `--mode`: Specify the data loading mode (raw input, file, or website).
- `--word`: Specify the word you want to search for.
<br>

### 4. Text Analysis and Metrics Generation

Analyze the text and generate key metrics, including morphology analysis, with the following command:

```bash
pyquantify analyze --mode [raw/file/website] --n [number_of_rows] --export
```

- `--mode`: Specify the data loading mode (raw input, file, or website).
- `--n`: Optional parameter to display a specific number of rows in the analysis.
- `--export`: Optional flag to export the analysis results to files.
<br>

### 5. Summarize Text

Summarize the text using a BERT Extractive Summarizer with the following command:

```bash
pyquantify summarize --mode [raw/file/website] --export
```

- `--mode`: Specify the data loading mode (raw input, file, or website).
- `--export`: Optional flag to export the summary to a file.
<br>

### Additional Commands

- View the Pyquantify GitHub page:
```bash
pyquantify --git [any command with its parameters]
```

Feel free to explore additional options and functionalities by checking the help documentation for each command:

```bash
pyquantify [command] --help
```
</div>

<h2><a id="map"> :compass: Roadmap</a></h2>

* [ ] Minimize training time for the multinomial NB model on subsequent project uses by leveraging pre-trained models.
* [ ] Diversifying export options to include formats such as CSV and xlsx.
* [ ] Investigate whether pre-trained conversational AI models can be leveraged to provide interactive access to the text's insights.
* [ ] Implement persistent data storage to eliminate repetitive data input and streamline user workflow.
* [ ] Ensure compatability with Windows operating system.



<h2><a id="ques">:grey_question: FAQ</a></h2>

### Q: What is Pyquantify?

Pyquantify is a tool designed for in-depth analysis of textual data, focusing on extracting meaning and linguistic insights. It provides features like word frequency, morphology, and metrics generation, enhancing data exploration and visualization.

### Q: Why Develop Pyquantify as a Semantic Profiler?

Pyquantify was created for the DSA subject in the fifth semester of college. The goal was to offer a versatile NLP tool, empowering users to analyze and profile text efficiently. The tool's features aim to deepen understanding and exploration of linguistic aspects within textual data.

### Q: Why Did Pyquantify evolve from a Word Frequency Counter?

Originally conceived as a word frequency counter, Pyquantify's development took a different direction. The decision to expand its capabilities was driven by the desire to create a more comprehensive tool for natural language processing. The project evolved to encompass semantic profiling, offering a richer set of features such as morphology analysis, metrics generation, and enhanced data visualization. This shift aimed to provide users with a more powerful and versatile solution for exploring and understanding textual data beyond simple word frequency analysis.

### Q: Why the name change from NLPFreq to Pyquantify?

NLPFreq felt limiting and didn't capture the full scope of the project. Pyquantify more accurately reflects its capabilities as a Python-based tool for quantitative data analysis.


<h2> <a id = "ack">:gem: Acknowledgements</a></h2>

- [NeuralNine's Publish Your Own Python Package](https://www.youtube.com/watch?v=tEFkHEKypLI)

<hr/>
**Note:** Pyquantify has undergone thorough testing on Linux, and its functionality is confirmed to work seamlessly. However, it's important to note that when running on Windows Subsystem for Linux (WSL), certain features may have limited functionality due to the absence of the complete Linux toolset in the WSL environment.
