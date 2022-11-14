import os

from dotenv import load_dotenv
from mcs import McsAPI, ContractAPI
from mcs.common.params import Params


class File:
    def __init__(self, filename, file_path):
        load_dotenv("../.env")
        self.filename = filename
        self.chain_name = "polygon.mainnet"
        self.wallet_address = os.getenv('wallet_address')
        self.private_key = os.getenv('private_key')
        self.rpc_endpoint = os.getenv('rpc_endpoint')
        self.file_path = file_path
        self.upload_response = None
        self.payment_tx_hash = None
        self.api = McsAPI(Params(self.chain_name).MCS_API)
        self.api.get_jwt_token(self.wallet_address, self.private_key, self.chain_name)
        self.w3_api = ContractAPI(self.rpc_endpoint, self.chain_name)

    def stream_upload(self):
        upload_file = self.api.stream_upload_file(self.wallet_address, self.file_path)
        file_data = upload_file["data"]
        need_pay = 0
        if file_data["status"] == "Free":
            self.upload_response = file_data
        else:
            self.upload_response = file_data
            need_pay = 1
            return file_data, need_pay
