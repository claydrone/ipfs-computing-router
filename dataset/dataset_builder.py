from dataset import Dataset
from file import File

upload_file = File('monkey', '/home/ccao/Downloads/swan_provide_tool_20211006.mov')
upload_file.stream_upload()

print(Dataset("bestsellers_with_categories", upload_file).title)
