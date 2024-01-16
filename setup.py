from setuptools import setup, find_packages
import os

setup(
    name='nlpfreq',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'click',
        'nltk',
        'tabulate',
        'wordcloud',
        'matplotlib',
        'seaborn',
        'requests',
        'beautifulsoup4',
    ],
    entry_points={
        'console_scripts': [
            'nlpfreq = nlpfreq.main:cli',
        ],
    },
    author='Vivek Dagar',
    author_email='vivekdagar2017@gmail.com',
    description='Advanced Feature-Rich CLI-based Word Frequency Analysis Tool',
    url='https://github.com/vivekkdagar/NLPFreq',
    license='GNU General Public License v3.0',
)
