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
- [:grey_question: FAQ](#ques)
- [:gem: Acknowledgements](#ack)



<h2><a id="srn"> :camera:</a> Demo screenshot</h2>
<div align="center"> <a href=""><img src="https://github.com/vivekkdagar/pyquantify/blob/main/sample-output/demo.png" alt='image' width='800'/></a> </div>


<h2><a id="feat">:dart:</a> Features</h2>

1. **Data Loading**: Load text data from raw input, files, or websites with interactive prompts for user input.

2. **Metrics Generation**: Calculate and display key metrics, including character count (with and without spaces), sentence count, word count, and paragraph count.

3. **Morphological Analysis**: Generate a detailed table of word morphology, including word rank, original form, lemmatized form, part-of-speech (POS) tag, percentage occurrence, and count.

4. **Export Functionality**: Optionally export generated metrics, frequency tables, and visualizations to files.

5. **Visualization**:
    - Generate and visualize the frequency of the top 20 words in the text.
    - Create and display a word cloud visualization of processed text data.

6. **Interactive Commands**: Utilize command-line interface commands for actions like displaying metrics, limiting results, searching for specific words, and generating visualizations.

7. **Summarize Text**: Summarize text using a BERT Extractive Summarizer.

8. **Sentiment Analysis**:
    - Perform sentiment analysis on the text.
    - Provides insights into sentiment polarity and subjectivity.


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
python3 -m build
```

3. Install the package:

```bash
pip install dist/*gz
```

4. Run the tool in terminal:

```bash
pyquantify
```
<h2><a id="use"> :book: Usage Guide</a></h3>

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
   
### Additional Commands

- View the Pyquantify GitHub page:
```bash
pyquantify --git
```

Feel free to explore additional options and functionalities by checking the help documentation for each command:

```bash
pyquantify [command] --help
```
</div>


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
