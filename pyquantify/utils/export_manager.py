import json
import os

__all__ = ['get_export_folder', 'ExportManager',]


def get_export_folder():
    if os.name == 'posix':  # Linux
        return os.path.expanduser("~/Documents/pyquantify")
    elif os.name == 'nt':  # Windows
        return os.path.expanduser("~\\Documents\\pyquzantify")
    else:
        raise Exception("Unsupported operating system")


class ExportManager:
    def __init__(self, loc):
        self.location = loc

    def create_dir(self):
        expanded_path = os.path.expanduser(self.location)

        if not os.path.exists(expanded_path):
            os.makedirs(expanded_path)
            print(f"Directory '{expanded_path}' created successfully.")

    def export(self, filename, data):
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
        base, ext = os.path.splitext(filename)
        counter = 1
        unique_filename = filename

        while os.path.exists(os.path.join(self.location, unique_filename)):
            unique_filename = f"{base}_{counter}{ext}"
            counter += 1

        return os.path.join(self.location, unique_filename)
