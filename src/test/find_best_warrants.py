import asyncio
import pprint
import json
import logging
from py_tr import TradeRepublicApi

tr = TradeRepublicApi()


def save_to_file(file, response):
    with open(file, 'w') as outfile:
        json.dump(response, outfile)


async def filter_derivative(results, option_type="call"):
    list = []
    for r in results:
        if r['optionType'] == "put" and r['strike'] > 200:
            # pprint.pprint(r)
            await tr.ticker(r['isin'], exchange="TUB")
            subscription_id, subscription, response = await tr.recv()
            logging.info(subscription)
            await tr.unsubscribe(subscription_id)
            # pprint.pprint(response)
            list.append(response)

    pprint.pprint(sorted(list, key=lambda x: (x['ask']['price'] - x['bid']['price']) / x['last']['price']))


async def my_loop():
    logging.info("async started")
    # underlying_isin = "US0378331005"  # AAPL
    underlying_isin = "US88160R1014"  # TSLA
    await tr.search_derivative(underlying_isin, option_type="PUT")
    # await tr.search("TSLA", asset_type="stock")
    # await tr.ticker("DE000TR3Y276", exchange="TUB")
    # await tr.instrument_details("DE000TT17QS7")
    # await tr.instrument_suitability("DE000TT0GQ58")
    # await tr.derivative_details("DE000TT0GQ58")
    # await tr.performance("DE000TT17QS7")
    # await tr.portfolio()

    # while True:
    subscription_id, subscription, response = await tr.recv()
    logging.info(subscription)
    # logging.info(response)
    # pprint.pprint(response)
    await tr.unsubscribe(subscription_id)
    await filter_derivative(response['results'])
    # save_to_file("portfolio.json", response)
    # with open('warrants_'+underlying_isin+'.json', 'w') as outfile:
    #     json.dump(response, outfile)


asyncio.get_event_loop().run_until_complete(my_loop())
