import unittest
from unittest.mock import patch, Mock
from pyquantify.bert_summarizer import CustomSummarizer


class TestCustomSummarizer(unittest.TestCase):
    @patch("ppyquantify.bert_summarizer.Summarizer")
    def test_summarize_cached(self, mock_summarizer):
        # Mocking the Summarizer class
        mock_parser = Mock()
        mock_parser.return_value = "This is a cached summary."
        mock_summarizer.return_value = mock_parser

        # Creating an instance of CustomSummarizer
        summarizer = CustomSummarizer("Sample text")

        # Calling summarize method for the first time
        summary, _ = summarizer.summarize()

        # Checking if the summary is returned from cache
        self.assertEqual(summary, "This is a cached summary.")

    @patch("ppyquantify.bert_summarizer.Summarizer")
    @patch("ppyquantify.bert_summarizer.ExportManager")
    def test_summarize_export(self, mock_export_manager, mock_summarizer):
        # Mocking the Summarizer class
        mock_parser = Mock()
        mock_parser.return_value = "This is a summary to export."
        mock_summarizer.return_value = mock_parser

        # Mocking the ExportManager class
        mock_manager = Mock()
        mock_manager.export.return_value = "/path/to/summary.txt"
        mock_export_manager.return_value = mock_manager

        # Creating an instance of CustomSummarizer
        summarizer = CustomSummarizer("Sample text")

        # Calling summarize method with export location
        summary, dest = summarizer.summarize(loc="/output/path")

        # Checking if the summary and destination path are returned correctly
        self.assertEqual(summary, "This is a summary to export.")
        self.assertEqual(dest, "/path/to/summary.txt")


if __name__ == "__main__":
    unittest.main()
