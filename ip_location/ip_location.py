import requests
import socket

def get_response_time(hostname: str):
    mcs_ip = socket.gethostbyname(hostname)
    mcs_response_time = requests.get('https://' + hostname).elapsed.total_seconds()
    mcs_url_location = requests.get('https://ipinfo.io/' + mcs_ip)
    # print(url, mcs_url_location.json())
    return mcs_response_time, mcs_url_location.json()['city']


if __name__ == "__main__":
    print(get_response_time('mcs.filswan.com'))
