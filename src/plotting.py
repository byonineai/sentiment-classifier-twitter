import csv
import matplotlib.pyplot as plt


class Plotter:
    """
    Class: Plotter
    Purpose: Generate a scatterplot from the sentiment analysis output CSV file.

    Author: Marcelo Salvador
    Date: 2026-02-26

    Output:
    - Displays a scatterplot of Net Score versus Number of Retweets
    """

    def produce_graph(self, output_file: str) -> None:
        """
        Method: produce_graph
        Purpose: Read the sentiment results CSV file and plot the data.

        Input:
        - output_file: path to the CSV file containing sentiment results

        Output:
        - Displays a scatterplot where:
          * x-axis = Net Score
          * y-axis = Number of Retweets
        """

        net_scores = []
        retweets = []

        with open(output_file, "r", encoding="utf-8", newline="") as infile:
            reader = csv.reader(infile)
            next(reader)  # Skip the header row

            for row in reader:
                retweets.append(int(row[0]))
                net_scores.append(int(row[4]))

        plt.figure(figsize=(8, 6))
        plt.scatter(net_scores, retweets)
        plt.xlabel("Net Score")
        plt.ylabel("Number of Retweets")
        plt.title("Net Score vs Number of Retweets")
        plt.show()