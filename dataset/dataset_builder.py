from dataset import Dataset
from file import File

files=File('monkey','../input/bestsellers_with_categories.csv')
files.upload_file_pay()

print(Dataset("bestsellers_with_categories",files).title)
