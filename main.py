from src.lexicon_loader import load_word_set
from src.preprocessing import TextPreprocessor
from src.strategies import LexiconSentimentStrategy
from src.io_utils import CSVReader, CSVWriter
from src.plotting import Plotter
from src.facade import SentimentFacade


def main():
    """
    Function: main
    Purpose: Serve as the entry point for the sentiment classifier application.

    Author: Marcelo Salvador
    Date: 2026-02-26

    Input:
    - Reads sentiment word lists from the data folder
    - Reads tweet data from data/project_twitter_data.csv

    Output:
    - Writes sentiment analysis results to output/resulting_data.csv
    - Displays a scatterplot of Net Score versus Number of Retweets
    """

    # Load the positive and negative sentiment lexicons
    positive_words = load_word_set("data/positive_words.txt")
    negative_words = load_word_set("data/negative_words.txt")

    # Create the preprocessing and sentiment strategy objects
    preprocessor = TextPreprocessor()
    strategy = LexiconSentimentStrategy(
        positive_words,
        negative_words,
        preprocessor
    )

    # Create the input/output and plotting utilities
    reader = CSVReader()
    writer = CSVWriter()
    plotter = Plotter()

    # Create the facade that coordinates the workflow
    app = SentimentFacade(
        strategy=strategy,
        preprocessor=preprocessor,
        reader=reader,
        writer=writer,
        plotter=plotter
    )

    # Run the full sentiment analysis pipeline
    app.run_analysis(
        input_file="data/project_twitter_data.csv",
        output_file="output/resulting_data.csv"
    )


if __name__ == "__main__":
    main()