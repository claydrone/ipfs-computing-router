#  dataset task
from file import File


class Dataset:
    def __init__(self, title, files: list[File]):
        self.title = title
        self.files = files
