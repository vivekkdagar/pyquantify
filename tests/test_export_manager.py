import unittest
import os
import shutil
from pyquantify.utils.export_manager import ExportManager


class TestExportManager(unittest.TestCase):
    def setUp(self):
        self.test_dir = os.path.join(os.path.expanduser("~"), "Documents", "test_ppyquantify")
        os.makedirs(self.test_dir, exist_ok=True)
        self.export_manager = ExportManager(self.test_dir)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_create_dir(self):
        # Test if directory is created successfully
        self.export_manager.create_dir()
        self.assertTrue(os.path.exists(self.test_dir))

        # Test if directory is not recreated if it already exists
        self.export_manager.create_dir()
        self.assertTrue(os.path.exists(self.test_dir))

    def test_generate_filename(self):
        # Test generating unique filename
        filename = self.export_manager.generate_filename("test.txt")
        self.assertEqual(filename, os.path.join(self.test_dir, "test.txt"))

        # Test generating unique filename with existing file
        with open(os.path.join(self.test_dir, "test.txt"), "w") as f:
            f.write("Test content")
        filename = self.export_manager.generate_filename("test.txt")
        self.assertTrue(filename.startswith(os.path.join(self.test_dir, "test_")))

    def test_export(self):
        # Test exporting data to a text file
        dest_file = self.export_manager.export("test.txt", "Hello, world!")
        self.assertTrue(os.path.exists(dest_file))
        with open(dest_file, "r") as f:
            self.assertEqual(f.read(), "Hello, world!")

        # Test exporting data to a JSON file
        dest_file = self.export_manager.export("test.json", {"key": "value"})
        self.assertTrue(os.path.exists(dest_file))
        with open(dest_file, "r") as f:
            self.assertEqual(f.read(), "{\n  \"key\": \"value\"\n}")

        # Test exporting data to a file with a duplicate filename
        dest_file = self.export_manager.export("test.txt", "Duplicate filename")
        self.assertTrue(os.path.exists(dest_file))
        with open(dest_file, "r") as f:
            self.assertEqual(f.read(), "Duplicate filename")
        self.assertTrue(dest_file.endswith("_1.txt"))  # Check if filename is modified


if __name__ == "__main__":
    unittest.main()
