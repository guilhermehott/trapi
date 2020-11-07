import asyncio
import pprint
import json
import logging
from py_tr import TradeRepublicApi

tr = TradeRepublicApi()


def save_to_file(file, response):
    with open(file, 'w') as outfile:
        json.dump(response, outfile)


async def my_loop():
    logging.info("async started")
    underlying_isin = "US0378331005"
    # await tr.search_derivative(underlying_isin)
    # await tr.search("AAPL", asset_type="stock")
    # await tr.ticker("DE000TT17QS7", exchange="LSX")
    await tr.instrument_details("DE000TT17QS7")
    # await tr.instrument_suitability("DE000TT0GQ58")
    # await tr.derivative_details("DE000TT0GQ58")
    # await tr.performance("DE000TT17QS7")
    # await tr.portfolio()

    while True:
        subscription_id, subscription, response = await tr.recv()
        pprint.pprint(response)
        # save_to_file("portfolio.json", response)
        # with open('warrants_'+underlying_isin+'.json', 'w') as outfile:
        #     json.dump(response, outfile)


asyncio.get_event_loop().run_until_complete(my_loop())
