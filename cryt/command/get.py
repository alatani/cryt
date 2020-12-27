from rich import print
from cryt.client import Client

class Get(object):
    def __init__(self, client: Client):
        self.__client = client

    def order(self):
        print(self.__client.get_orders())

    def positions(self):
        positions = self.__client.get_positions()
        print(positions)

    def ticker(self):
        print(self.__client.get_ticker())
