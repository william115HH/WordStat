from collections import Counter
import string
import argparse
import sys

STOPWORDS = {"the", "a", "an", "and", "or", "of", "to", "in", "on", "at", "is", "it", "its", "for", "with", "as", "by"}


def remove_punctuation(text : str) -> str:
    result = ""
    for char in text:
        if char not in string.punctuation:
            result += char
    return result

def clean_words(text: str) -> list[str]:
   text = text.lower()
   text = remove_punctuation(text)
   text = text.split()
   return text

def average_word_length(words: list[str]) -> float:
    total_length = sum(len(word) for word in words)
    return total_length / len(words) if words else 0.0

def remove_stopwords(words: list[str]) -> list[str]:
    text = [word for word in words if word not in STOPWORDS]
    return text

def main() -> None:
    parser = argparse.ArgumentParser(description="Count words in a text file.")
    parser.add_argument("filepath", help="path to the text file")
    parser.add_argument("--stopwords", action="store_true", help="exclude common words like 'the' and 'and'")
    args = parser.parse_args()
    try:
        with open(args.filepath) as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{args.filepath}' not found.")
        sys.exit(1)

    words = clean_words(text)
    if args.stopwords:
        words = remove_stopwords(words)
    counts = Counter(words)

    print("Total number of words:", len(words))
    print("Top 10: ", counts.most_common(10))
    print("Average word length:", round(average_word_length(words), 2))

if __name__ == "__main__":
    main()
