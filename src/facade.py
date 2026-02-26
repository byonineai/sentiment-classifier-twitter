from .strategies import SentimentStrategy
from .preprocessing import TextPreprocessor
from .io_utils import CSVReader, CSVWriter
from .plotting import Plotter

# The class that orchestrates the opera

class SentimentFacade:
    """
    Class: SentimentFacade
    Purpose: Coordinate the sentiment analysis workflow from input CSV to output CSV and graph.

    Author: Marcelo Salvador
    Date: 2026-02-26

    Dependencies:
    - SentimentStrategy
    - TextPreprocessor
    - CSVReader
    - CSVWriter
    - Plotter

    Output:
    - Writes sentiment results to a CSV file
    - Produces a scatterplot of Net Score vs Number of Retweets
    """

    def __init__(
        self,
        strategy: SentimentStrategy,
        preprocessor: TextPreprocessor,
        reader: CSVReader,
        writer: CSVWriter,
        plotter: Plotter,
    ):
        self.strategy = strategy
        self.preprocessor = preprocessor
        self.reader = reader
        self.writer = writer
        self.plotter = plotter

    def run_analysis(self, input_file: str, output_file: str) -> None:
        input_rows = self.reader.read_rows(input_file)
        output_rows = []

        for row in input_rows:
            tweet_text = row[0]
            retweets = int(row[1])
            replies = int(row[2])

            pos, neg, net = self.strategy.score(tweet_text)
            output_rows.append([retweets, replies, pos, neg, net])

        self.writer.write_results(output_file, output_rows)
        self.plotter.produce_graph(output_file)
