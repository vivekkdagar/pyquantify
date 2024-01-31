from setuptools import setup, find_packages

setup(
    name='pyquantify',
    version='1.1.1',
    packages=find_packages(),
    install_requires=[
        'click~=8.1.7',
        'nltk~=3.8.1',
        'tabulate~=0.9.0',
        'requests~=2.31.0',
        'beautifulsoup4~=4.12.2',
        'bert-extractive-summarizer~=0.10.1',
        'pandas~=2.1.4',
        'joblib~=1.2.0',
        'scikit-learn~=1.3.0',
        'matplotlib~=3.7.2',
        'seaborn~=0.12.2',
        'spacy~=3.7.2',
        'wordcloud~=1.9.2',
        'textblob~=0.15.3',
        'setuptools~=68.0.0',
    ],
    entry_points={
        'console_scripts': [
            'pyquantify = pyquantify.main:cli',
        ],
    },
    author='Vivek Dagar',
    author_email='vivekdagar2017@gmail.com',
    description='Advanced Feature-Rich CLI-based Tool for Semantic Analysis',
    url='https://github.com/vivekkdagar/pyquantify/',
    long_description="""Please refer to the Github for usage guide and more {https://github.com/vivekkdagar/pyquantify}""",
    long_description_content_type='text/markdown',
    license='GNU General Public License v3.0',
)
