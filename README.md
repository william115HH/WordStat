Wordstat takes in a text file and returns the total number of words, the top 10 most common words, and the average word length.
# wordstat

A command-line tool that counts words in a text file and reports the top 10 most common words, the total word count, and the average word length.

## Usage

Count words in a text file:

```
python3 wordstat.py sample.txt
```

Exclude common words like "the" and "and":

```
python3 wordstat.py sample.txt --stopwords
```

## Running the tests

```
python3 -m pytest
```