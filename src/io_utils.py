import csv


class CSVReader:
    """
    Class: CSVReader
    Purpose: Read tweet rows from an input CSV file.

    Author: Marcelo Salvador
    Date: 2026-02-26

    Output:
    - Returns all data rows from the CSV file after skipping the header row.
    """

    def read_rows(self, input_file: str) -> list[list[str]]:
        """
        Read all tweet rows from the input CSV file.

        Input:
        - input_file: path to the input CSV file

        Output:
        - A list of rows, where each row is a list of strings
        """
        with open(input_file, "r", encoding="utf-8", newline="") as infile:
            reader = csv.reader(infile)
            next(reader)
            return list(reader)


class CSVWriter:
    """
    Class: CSVWriter
    Purpose: Write sentiment analysis results to an output CSV file.

    Author: Marcelo Salvador
    Date: 2026-02-26

    Output:
    - Creates a CSV file containing retweets, replies, positive score,
      negative score, and net score.
    """

    def write_results(self, output_file: str, rows: list[list[int]]) -> None:
        """
        Write the sentiment analysis results to the output CSV file.

        Input:
        - output_file: path to the output CSV file
        - rows: list of result rows

        Output:
        - Writes a CSV file with a header row and all result rows
        """
        with open(output_file, "w", encoding="utf-8", newline="") as outfile:
            writer = csv.writer(outfile)
            writer.writerow([
                "Retweets",
                "Replies",
                "Positive Score",
                "Negative Score",
                "Net Score"
            ])
            writer.writerows(rows)