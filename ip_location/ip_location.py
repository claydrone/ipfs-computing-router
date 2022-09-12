import requests
import socket

mcs_url = 'mcs.filswan.com'
mcs_ip = socket.gethostbyname(mcs_url)
mcs_response_time = requests.get('https://' + mcs_url).elapsed.total_seconds()
mcs_url_location = requests.get('https://ipinfo.io/' + mcs_ip)
# print(mcs_url, mcs_url_location.json())
print(mcs_url, mcs_url_location.json()['city'])

ipfs_io_url = 'ipfs.io'
ipfs_io_ip = socket.gethostbyname(ipfs_io_url)
ipfs_io_response_time = requests.get('https://' + mcs_url).elapsed.total_seconds()

ipfs_io_location = requests.get('https://ipinfo.io/' + ipfs_io_ip)
print(ipfs_io_url, ipfs_io_location.json()['city'])

print('ipfs_io_response_time', ipfs_io_response_time)
print('mcs_response_time', mcs_response_time)

if mcs_response_time < ipfs_io_response_time:
    print('Chose mcs gateway')
else:
    print('Chose ipfs gateway')
