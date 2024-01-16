from setuptools import setup, find_packages

setup(
    name='nlpfreq',
    version='0.1',
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
            'your_command_name = your_module_name:cli',
        ],
    },
    author='Vivek Dagar',
    author_email='vivekdagar',
    description='Description of your project',
    url='https://github.com/yourusername/your_project_name',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
