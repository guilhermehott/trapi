import asyncio
import pprint
import json
import logging
from py_tr import TradeRepublicApi

tr = TradeRepublicApi()


def save_to_file(file, response):
    with open(file, 'a') as outfile:
        # json.dump(response+",\n", outfile)
        outfile.write(str(response)+",\n")


async def my_loop():
    logging.info("async started")
    # underlying_isin = "US0378331005"  # AAPL
    underlying_isin = "US88160R1014"  # TSLA
    # await tr.search_derivative(underlying_isin, option_type="PUT")
    # await tr.search("TSLA", asset_type="stock")
    await tr.ticker("DE000TT1Q936", exchange="TUB")
    # await tr.instrument_details("DE000TT17QS7")
    # await tr.instrument_suitability("DE000TT0GQ58")
    # await tr.derivative_details("DE000TT0GQ58")
    # await tr.performance("US88160R1014")
    # await tr.portfolio()
    # await tr.performance_history("DE000TT1Q936", "1d", exchange="TUB")

    while True:
        subscription_id, subscription, response = await tr.recv()
        logging.info(subscription)
        # logging.info(response)
        pprint.pprint(response)
        save_to_file("../tmp/history-DE000TT1Q936.json", response)
        # with open('warrants_'+underlying_isin+'.json', 'w') as outfile:
        #     json.dump(response, outfile)


asyncio.get_event_loop().run_until_complete(my_loop())
