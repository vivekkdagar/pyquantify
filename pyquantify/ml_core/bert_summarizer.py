from summarizer import Summarizer
from pyquantify.utils.export_manager import ExportManager


class CustomSummarizer:
    def __init__(self, text):
        self.export_path_txt = None
        self.text = text
        self.parser = Summarizer()

    def summarize(self, loc=None):
        summary = self.parser(self.text)
        dest = None
        if loc:
            manager = ExportManager(loc)
            dest = manager.export('summary.txt', summary)
        return [summary, dest]
