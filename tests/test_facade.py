from src.facade import SentimentFacade

class FakeStrategy:
  def score(self, text):
    return [2, 3, 3]

class FakeReader:
  def read_rows(self, input_file):
    return [
      ["tweeet one", "4", "2"],
      ["tweet three", "2", "2"]
    ]

class FakeWriter:
    def __init__(self):
      self.output_file = None
      self.rows = None

    def write_results(self, output_file, rows):
      self.output_file = output_file
      self.rows = rows


class FakePlotter:
    def __init__(self):
      self.called_with = None

    def produce_graph(self, output_file):
      self.called_with = output_file

class FakePreprocessor:
    pass

def test_facade_runs_analysis_and_writes_expected_rows():
    strategy = FakeStrategy()
    reader = FakeReader()
    writer = FakeWriter()
    plotter = FakePlotter()
    preprocessor = FakePreprocessor()

    app = SentimentFacade(
       strategy = strategy,
       preprocessor = preprocessor,
       reader = reader,
       writer = writer,
       plotter = plotter
    )

    app.run_analysis("input.csv","output.csv")

    assert writer.output_file == "output.csv"

    assert writer.rows == [
      [4, 2, 2, 3, 3],
      [2, 2, 2, 3, 3],
    ]

    assert plotter.called_with == 'output.csv'
