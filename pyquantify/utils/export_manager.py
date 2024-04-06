import json
import os

__all__ = ['get_export_folder', 'ExportManager', ]


def get_export_folder():
    """
        Returns the path to the export folder based on the operating system.

        Returns:
            str: Path to the export folder.

        Raises:
            Exception: If the operating system is not supported.
    """
    if os.name == 'posix':  # Linux
        return os.path.expanduser("~/Documents/pyquantify")
    elif os.name == 'nt':  # Windows
        return os.path.expanduser("~\\Documents\\pyquantify")
    raise Exception("Unsupported operating system")


class ExportManager:
    """
        A class to manage exporting data to files.
    """
    def __init__(self, loc):
        """
        Initializes the ExportManager with the given location.

        Args:
            loc (str): The location where files will be exported.
        """
        self.location = loc

    def create_dir(self):
        """
        Creates the export directory if it does not exist.
        """
        expanded_path = os.path.expanduser(self.location)

        if not os.path.exists(expanded_path):
            os.makedirs(expanded_path)
            print(f"Directory '{expanded_path}' created successfully.\n")

    def export(self, filename, data):
        """
        Exports the given data to a file with the specified filename.

        Args:
            filename (str): The name of the file to export to.
            data (object): The data to be exported.

        Returns:
            str: The path to the exported file.
        """
        dest_name = self.generate_filename(filename)

        self.create_dir()

        if filename.endswith(".json"):
            with open(dest_name, 'w') as export_json:
                json.dump(data, export_json, indent=2)
        else:
            with open(dest_name, 'w') as export_txt:
                export_txt.write(data)

        return dest_name

    def generate_filename(self, filename):
        """
        Generates a unique filename by appending a counter to the base filename if necessary.

        Args:
            filename (str): The base filename.

        Returns:
            str: A unique filename.
        """
        base, ext = os.path.splitext(filename)
        counter = 1
        unique_filename = filename

        while os.path.exists(os.path.join(self.location, unique_filename)):
            unique_filename = f"{base}_{counter}{ext}"
            counter += 1

        return os.path.join(self.location, unique_filename)
