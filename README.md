<div align='center'>

<h1>pyquantify</h1>
<p>Pyquantify is a powerful CLI tool for semantic analysis. It leverages natural language processing to unveil insights from text, files, or websites, empowering sophisticated data visualization and exploration.</p>

<h4> <a href="https://github.com/vivekkdagar/pyquantify/issues"> Report Bug </a> <span> · </span> <a href="https://github.com/vivekkdagar/pyquantify/issues"> Request Feature </a> </h4>


</div>

# :notebook_with_decorative_cover: Table of Contents

- [About the Project](#star2-about-the-project)
- [Roadmap](#compass-roadmap)
- [FAQ](#grey_question-faq)
- [License](#warning-license)
- [Contact](#handshake-contact)
- [Acknowledgements](#gem-acknowledgements)


## :star2: About the Project

### :camera: Screenshots
<div align="center"> <a href=""><img src="s" alt='image' width='800'/></a> </div>


### :dart: Features
- **Data Loading**: Load text data from various sources, including raw input, files, and websites, with interactive prompts for user input.
- **Text Preprocessing**: Tokenize and clean the text data, removing punctuation and converting words to lowercase.
- **Metrics Generation**: Calculate and display key metrics, including character count with and without spaces, sentence count, word count, and paragraph count.
- **Morphological Analysis**: Generate a detailed table of word morphology, including word rank, original form, lemmatized form, part-of-speech (POS) tag, percentage occurrence, and count.
- **Export Functionality**: Optionally export the generated metrics, frequency tables, and visualizations to files.
- **Word Cloud Visualization**: Create and display a word cloud visualization of the processed text data.
- **Word Frequency Chart**: Generate and visualize the frequency of the top 20 words in the text.
- **Interactive Commands**: Utilize command-line interface commands to perform actions such as displaying metrics, limiting results, searching for specific words, and generating visualizations.
- **Summarize text**: It can now summarize your text and utilizes a BERT Extractive Summarizer to achieve it.


## :toolbox: Getting Started

### :bangbang: Prerequisites

Ensure you meet the following requirements before installation (if you're building from source):

```bash
pip install -r requirements.txt
```

## :toolbox: Installation

### Install from PyPI

You can install the `pyquantify` package directly from PyPI using the following command:

```bash
pip install pyquantify
```

### Build from Source

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

## :compass: Roadmap

* [ ] Minimize training time for the multinomial NB model on subsequent project uses by leveraging pre-trained models.
* [ ] Diversifying export options to include formats such as CSV and xlsx.
* [ ] Investigate whether pre-trained conversational AI models can be leveraged to provide interactive access to the text's insights.
* [ ] Implement persistent data storage to eliminate repetitive data input and streamline user workflow.
* [ ] Ensure compatability with Windows operating system.


### :scroll: Code of Conduct

Please read the [Code of Conduct](https://github.com/vivekkdagar/pyquantify/blob/master/CODE_OF_CONDUCT.md)

## :grey_question: FAQ

### Q: What is Pyquantify?

Pyquantify is a tool designed for in-depth analysis of textual data, focusing on extracting meaning and linguistic insights. It provides features like word frequency, morphology, and metrics generation, enhancing data exploration and visualization.

### Q: Why Develop Pyquantify as a Semantic Profiler?

Pyquantify was created for the DSA subject in the fifth semester of college. The goal was to offer a versatile NLP tool, empowering users to analyze and profile text efficiently. The tool's features aim to deepen understanding and exploration of linguistic aspects within textual data.

### Q: Why Did Pyquantify evolve from a Word Frequency Counter?

Originally conceived as a word frequency counter, Pyquantify's development took a different direction. The decision to expand its capabilities was driven by the desire to create a more comprehensive tool for natural language processing. The project evolved to encompass semantic profiling, offering a richer set of features such as morphology analysis, metrics generation, and enhanced data visualization. This shift aimed to provide users with a more powerful and versatile solution for exploring and understanding textual data beyond simple word frequency analysis.

### Q: Why the name change from NLPFreq to Pyquantify?

NLPFreq felt limiting and didn't capture the full scope of the project. Pyquantify more accurately reflects its capabilities as a Python-based tool for quantitative data analysis.



## :warning: License

Distributed under the MIT License. See LICENSE for more information.

## :gem: Acknowledgements

- [NeuralNine's Publish Your Own Python Package](https://www.youtube.com/watch?v=tEFkHEKypLI)
