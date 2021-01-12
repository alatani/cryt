from rich import print
from rich.console import Console
from rich.table import Table

from cryt.client import Client

class Get(object):
    def __init__(self, client: Client):
        self.__client = client

    def order(self):
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Type")
        table.add_column("Symbol")
        table.add_column("Side")
        table.add_column("Price")
        table.add_column("Size")

        for order in self.__client.get_orders():
            table.add_row(order['type'], order['symbol'], str(order['side']), str(order['price']), str(order['remaining']))
        console = Console()
        console.print(table)

    def position(self):
        positions = self.__client.get_positions()

        print(positions)
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Symbol")
        table.add_column("Side")
        table.add_column("Price")
        table.add_column("Size")
        table.add_column("Pnl")
        for position in positions:
            table.add_row(position['product_code'], position['side'], str(position['price']), str(position['size']), str(position['pnl']))
        console = Console()
        console.print(table)

    def ticker(self):
        res = self.__client.get_ticker()
        del res["info"]
        print(res)
