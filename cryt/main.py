import fire

from cryt.command import Get, Order, Cancel
import cryt.client

class CryptCli(object):
    def __init__(self, exchange: str="bitflyer", symbol="FX_BTC_JPY"):
        self.__exchange = exchange
        self.__client = cryt.client.Client.create(exchange, symbol) # .create(exchange)

        self.get = Get(self.__client)
        self.order = Order(self.__client)
        self.cancel = Cancel(self.__client)

    def test(self):
        print(self.exchange)

    def lob(self):
        pass


if __name__ == "__main__":
    fire.Fire(CryptCli)

