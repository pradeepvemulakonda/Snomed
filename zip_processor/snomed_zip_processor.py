import os
import shutil
import zipfile
from config.read_config import SnomedConfig
from load.base_processor import BaseProcessor

__author__ = 'pradeepv'


class SnomedArchiveProcessor(BaseProcessor):
    def __init__(self, snomed_zip_file):
        self.snomed_zip_file = snomed_zip_file

    def process(self):
        self.process_file(self.snomed_zip_file)

    def process_file(self, file):
        with zipfile.ZipFile(file) as zip_file:
            print(zip_file)
            for member in zip_file.namelist():
                filename = os.path.basename(member)
                full_file_path = os.path.join(os.path.dirname(self.snomed_zip_file), filename)
                # skip directories
                if not filename:
                    continue
                if filename.endswith(".zip"):
                    source = zip_file.open(member)
                    target = open(full_file_path, "wb")
                    with source, target:
                        shutil.copyfileobj(source, target)
                    self.process_file(full_file_path)
                elif filename.endswith(".txt") and '/Snapshot/Terminology' in member:
                    print(filename)
                    # copy file (taken from zipfile's extract)
                    source = zip_file.open(member)
                    sc = SnomedConfig().ConfigSectionMap("FileSection")
                    dir = os.path.dirname(os.path.dirname(__file__))
                    destinationFolder = os.path.join(dir, sc["snomedfiles"])
                    target = open(os.path.join(destinationFolder, filename), "wb")
                    with source, target:
                        shutil.copyfileobj(source, target)
                else:
                    continue
