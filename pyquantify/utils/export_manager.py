# import json
# import os
#
# __all__ = ['get_export_folder', 'ExportManager',]
#
#
def get_export_folder():
    if os.name == 'posix':  # Linux
        return os.path.expanduser("~/Documents/pyquantify")
    elif os.name == 'nt':  # Windows
        return os.path.expanduser("~\\Documents\\pyquantify")
    else:
        raise Exception("Unsupported operating system")
#
#
# class ExportManager:
#     def __init__(self, loc):
#         self.location = loc
#
#     def create_dir(self):
#         expanded_path = os.path.expanduser(self.location)
#
#         if not os.path.exists(expanded_path):
#             os.makedirs(expanded_path)
#             print(f"Directory '{expanded_path}' created successfully.")
#
#     def export(self, filename, data):
#         dest_name = self.generate_filename(filename)
#
#         self.create_dir()
#
#         if filename.endswith(".json"):
#             with open(dest_name, 'w') as export_json:
#                 json.dump(data, export_json, indent=2)
#         else:
#             with open(dest_name, 'w') as export_txt:
#                 export_txt.write(data)
#
#         return dest_name
#
#     def generate_filename(self, filename):
#         base, ext = os.path.splitext(filename)
#         counter = 1
#         unique_filename = filename
#
#         while os.path.exists(os.path.join(self.location, unique_filename)):
#             unique_filename = f"{base}_{counter}{ext}"
#             counter += 1
#
#         return os.path.join(self.location, unique_filename)

import json
import os
import asyncio
from concurrent.futures import ThreadPoolExecutor

class ExportManager:
    def __init__(self, loc):
        self.location = loc

    async def create_dir_async(self):
        expanded_path = os.path.expanduser(self.location)
        if not os.path.exists(expanded_path):
            os.makedirs(expanded_path)
            print(f"Directory '{expanded_path}' created successfully.")

    async def export_async(self, filename, data):
        await self.create_dir_async()
        dest_name = self.generate_filename(filename)

        # Construct full destination path
        dest_path = os.path.join(self.location, dest_name)

        # Write data to file
        with open(dest_path, 'w') as export_file:
            if filename.endswith(".json"):
                json.dump(data, export_file, indent=2)
            else:
                export_file.write(data)

        return dest_path

    async def generate_filename_async(self, filename):
        base, ext = os.path.splitext(filename)
        unique_filename = filename
        counter = 1

        # Check if the file already exists, if yes, append a counter to make it unique
        while os.path.exists(os.path.join(self.location, unique_filename)):
            unique_filename = f"{base}_{counter}{ext}"
            counter += 1

        return unique_filename

    async def export_multiple_async(self, file_data_mapping):
        await self.create_dir_async()

        with ThreadPoolExecutor(max_workers=os.cpu_count() or 1) as executor:
            loop = asyncio.get_event_loop()
            tasks = []
            for filename, data in file_data_mapping.items():
                tasks.append(loop.run_in_executor(executor, self._export_file, filename, data))
            return await asyncio.gather(*tasks)

    def _export_file(self, filename, data):
        dest_path = os.path.join(self.location, self.generate_filename(filename))

        with open(dest_path, 'w') as export_file:
            if filename.endswith(".json"):
                json.dump(data, export_file, indent=2)
            else:
                export_file.write(data)

        return dest_path

    def create_dir(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.create_dir_async())

    def export(self, filename, data):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self.export_async(filename, data))

    def generate_filename(self, filename):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self.generate_filename_async(filename))

    def export_multiple(self, file_data_mapping):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self.export_multiple_async(file_data_mapping))
