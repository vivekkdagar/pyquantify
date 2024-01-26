from setuptools import setup, find_packages

setup(
    name='pyquantify',
    version='1.0.1',
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
