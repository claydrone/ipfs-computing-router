from dataset import Dataset
from file import File

files=[File('monkey','../input/bestsellers_with_categories.csv')]
print(Dataset("bestsellers_with_categories",files).title)
