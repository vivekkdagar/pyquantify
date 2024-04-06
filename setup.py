from setuptools import setup, find_packages

setup(
    name='pyquantify',
    version='1.2.0',
    packages=find_packages(),
    install_requires=[
        'requests~=2.31.0',
        'beautifulsoup4~=4.12.3',
        'tqdm~=4.66.2',
        'click~=8.1.7',
        'matplotlib~=3.7.5',
        'nltk~=3.8.1',
        'seaborn~=0.12.2',
        'spacy~=3.7.4',
        'scikit-learn~=1.3.2',
        'tabulate~=0.9.0',
        'wordcloud~=1.9.3',
        'bert-extractive-summarizer',
        'wheel',
        'build',
        'setuptools~=68.0.0',
        'textblob~=0.15.3',
        'langid~=1.1.6',
        'torch',
        'lxml',
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
    long_description="""Please refer to the Github for usage guide and more {
    https://github.com/vivekkdagar/pyquantify}""",
    long_description_content_type='text/markdown',
    license='GNU General Public License v3.0',
)
