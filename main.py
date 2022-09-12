import os, time

from ip_location.ip_location import get_response_time
from mcs.contract import ContractAPI
from mcs.api import McsAPI
import requests
import socket
from dotenv import load_dotenv

load_dotenv()
web3_api = os.getenv('web3_api')
wallet_address = os.getenv('wallet_address')
private_key = os.getenv('private_key')


def upload_file_pay(filepath):
    w3_api = ContractAPI(web3_api)
    api = McsAPI()
    # upload file to mcs
    father_path = os.path.abspath(os.path.dirname(__file__))
    upload_file = api.upload_file(wallet_address, father_path + filepath)
    file_data = upload_file["data"]
    payload_cid, source_file_upload_id, nft_uri, file_size, w_cid = file_data['payload_cid'], file_data[
        'source_file_upload_id'], file_data['ipfs_url'], file_data['file_size'], file_data['w_cid']
    # get the global variable
    params = api.get_params()["data"]
    # get filcoin price
    rate = api.get_price_rate()["data"]
    # test upload_file_pay contract
    w3_api.upload_file_pay(wallet_address, private_key, file_size, w_cid, rate, params)


if __name__ == "__main__":
    mcs_url = 'mcs.filswan.com'
    ipfs_io_url = 'ipfs.io'
    mcs_response_time, mcs_city = get_response_time(mcs_url)
    ipfs_io_response_time, ipfs_city = get_response_time(ipfs_io_url)
    print(mcs_url, mcs_city, mcs_response_time)
    print(ipfs_io_url, ipfs_city, ipfs_io_response_time)

    if mcs_response_time < ipfs_io_response_time:
        print('Chose mcs gateway: Document upload starting....')
        upload_file_pay('/computing/image_classification.ipynb')
    else:
        print('Chose ipfs gateway')
