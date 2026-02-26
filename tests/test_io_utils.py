import csv
from src.io_utils import CSVReader, CSVWriter


def test_csv_reader_skips_header_and_reads_rows(tmp_path):
    input_file = tmp_path / "input.csv"
    input_file.write_text(
        "tweet,retweets,replies\nhello,5,2\nworld,3,1\n",
        encoding="utf-8"
    )

    reader = CSVReader()
    rows = reader.read_rows(str(input_file))

    assert rows == [["hello", "5", "2"], ["world", "3", "1"]]


def test_csv_writer_writes_header_and_rows(tmp_path):
    output_file = tmp_path / "output.csv"
    rows = [
        [5, 2, 1, 0, 1],
        [3, 1, 0, 1, -1],
    ]

    writer = CSVWriter()
    writer.write_results(str(output_file), rows)

    with open(output_file, "r", encoding="utf-8", newline="") as f:
        reader = list(csv.reader(f))

    assert reader[0] == [
        "Retweets",
        "Replies",
        "Positive Score",
        "Negative Score",
        "Net Score",
    ]
    assert reader[1] == ["5", "2", "1", "0", "1"]
    assert reader[2] == ["3", "1", "0", "1", "-1"]

 