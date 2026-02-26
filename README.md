# Sentiment Classifier Twitter

A Python project that analyzes tweet sentiment using a lexicon-based strategy, writes the results to a CSV file, and produces a scatterplot of **Net Score vs Number of Retweets**.

## Project Overview

This project:

- Reads tweet data from a CSV file
- Loads positive and negative word lists
- Cleans and tokenizes tweet text
- Computes:
  - Retweets
  - Replies
  - Positive Score
  - Negative Score
  - Net Score
- Writes the results to an output CSV
- Creates a scatterplot of:
  - **X-axis:** Net Score
  - **Y-axis:** Number of Retweets

## Project Structure

```text
sentiment-classifier-twitter/
│
├── data/
│   ├── positive_words.txt
│   ├── negative_words.txt
│   └── project_twitter_data.csv
│
├── output/
│   └── resulting_data.csv
│
├── src/
│   ├── __init__.py
│   ├── facade.py
│   ├── io_utils.py
│   ├── lexicon_loader.py
│   ├── plotting.py
│   ├── preprocessing.py
│   └── strategies.py
│
├── tests/
│   ├── test_facade.py
│   ├── test_io_utils.py
│   ├── test_lexicon_loader.py
│   ├── test_preprocessing.py
│   └── test_strategies.py
│
├── docs/
│   ├── sentiment.pseudo
│   ├── flowchart.mmd
│   └── discrete-math-spec.qmd
│
├── main.py
├── requirements.txt
└── README.md
```

## **Requirements**

- Python 3.10+ (recommended)
- Git
- pip

## **How to Download from GitHub**

Clone the repository:

Go into the project folder:

cd sentiment-classifier-twitter

## **How to Create and Activate a Virtual Environment**

Create the virtual environment:

python3 -m venv .venv

Activate it on macOS/Linux:

source .venv/bin/activate

After activation, your terminal should show something li

(.venv)

## **How to Install Dependencies**

Install the required packages:

python -m pip install -r requirements.txt

If you do not yet have a **requirements.txt**, install manually:

python -m pip install matplotlib pytest

## **How to Run the Project**

From the project root, run:

python main.py

This will:

1. Load the positive and negative word lists from **data/**
2. **Read **data/project_twitter_data.csv
3. **Generate **output/resulting_data.csv
4. **Display a scatterplot of \*\***Net Score vs Number of Retweets\*\*

## **Output Files**

The project creates:

- output/resulting_data.csv

This file contains:

- Retweets
- Replies
- Positive Score
- Negative Score
- Net Score

## **How to Run Tests**

Run all tests:

python -m pytest

## **Common Issues**

### **1. ModuleNotFoundError**

If you see import errors, make sure:

- you are running **python main.py** from the project root
- src/**init**.py** exists**
- imports inside **src/** use relative imports like:

from .preprocessing import TextPreprocessor

### **2. FileNotFoundError**

Make sure these files exist:

- data/positive_words.txt
- data/negative_words.txt
- data/project_twitter_data.csv

### **3. matplotlib not found**

python -m pip install matplotlib

## **Design Patterns Used**

This project uses:

- **Strategy Pattern**
  - SentimentStrategy
  - LexiconSentimentStrategy
- **Facade Pattern**
  - SentimentFacade

## **Author**

Marcelo Domingos Salvador
