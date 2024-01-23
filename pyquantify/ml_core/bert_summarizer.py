from summarizer import Summarizer
from pyquantify.utils.export_manager import ExportManager


class CustomSummarizer:
    def __init__(self, text):
        self.export_path_txt = None
        self.text = text
        self.parser = Summarizer()

    def summarize(self, loc=None):
        summary = self.parser(self.text)
        if loc:
            manager = ExportManager(loc)
            self.export_path_txt = manager.generate_filename('summary.txt')
            manager.export(self.export_path_txt, summary)
        return summary
