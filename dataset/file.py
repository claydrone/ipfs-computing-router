import os

from dotenv import load_dotenv
from mcs.upload.mcs_upload import MCSUpload


class File:
    def __init__(self, filename, path):
        self.filename = filename
        self.path = path

    def upload_file_pay(self):
        load_dotenv("../.env")
        wallet_address = os.getenv('wallet_address')
        private_key = os.getenv('private_key')
        rpc_endpoint = os.getenv('rpc_endpoint')

        uploaded_file = MCSUpload("polygon.mainnet", wallet_address, private_key, rpc_endpoint, self.path)
        uploaded_file.approve_token(1)
        file_data, need_pay = uploaded_file.stream_upload()
        print(uploaded_file.upload_response)

        if need_pay:
            uploaded_file.pay()
            uploaded_file.mint('a_image')
