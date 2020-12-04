import asyncio
import pprint
import json
import logging
from py_tr import TradeRepublicApi

tr = TradeRepublicApi()


def save_to_file(file, response):
    with open(file, 'w') as outfile:
        json.dump(response, outfile)


async def find_best_warrants():
    logging.info("async started")
    underlying_isin = "US0378331005"  # AAPL
    # await tr.search_derivative(underlying_isin)
    # await tr.search("AAPL", asset_type="stock")
    # await tr.ticker("US0378331005", exchange="LSX")
    await tr.portfolio()
    # await tr.cash_available_for_order()
    # await tr.market_order('US0378331005', 'LSX', 'buy', 1, 'gfd', False)  # BUY 1 AAPL
    await tr.market_order('US0378331005', 'LSX', 'sell', 1, 'gfd', False)  # SELL 1 AAPL

    while True:
        subscription_id, subscription, response = await tr.recv()
        pprint.pprint(response)
        # save_to_file("portfolio.json", response)
        # with open('warrants_'+underlying_isin+'.json', 'w') as outfile:
        #     json.dump(response, outfile)


asyncio.get_event_loop().run_until_complete(find_best_warrants())
