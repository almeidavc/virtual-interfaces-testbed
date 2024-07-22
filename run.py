import os

from pathlib import Path

from pyroute2 import NSPopen

from network.network import setup_tc
from network.network import clear_tc

CLIENT_PATH = '../moq-streaming-client/'
SERVER_PATH = '../moq-streaming-server/'


def iperf3test():
    setup_tc()
    server = NSPopen('ns1', ['cd', SERVER_PATH, '&&', "./dev/live-ingest.sh", "|", "live-streaming-server"])
    print('server process started')
    client = NSPopen('ns4', ['cd', CLIENT_PATH, '&&', "yarn test"])
    print('client process started')
    # print('done')
    # clear_tc()

