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

        up = MCSUpload("polygon.mainnet", wallet_address, private_key, rpc_endpoint, self.path)
        up.approve_token(1)
        file_data, need_pay = up.stream_upload()
        print(up.estimate_amount)

        if need_pay:
            up.pay()
            up.mint('a_image')



