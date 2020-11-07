import asyncio
import pprint
import json
import logging
from py_tr import TradeRepublicApi

tr = TradeRepublicApi()

async def my_loop():
    logging.info("async started")
    underlying_isin = "US0378331005"
    await tr.search_derivative(underlying_isin)
    # await tr.search("DE000TT0GR32", asset_type="derivative")

    while True:
        subscription_id, subscription, response = await tr.recv()
        pprint.pprint(response)
        with open('warrants_'+underlying_isin+'.txt', 'w') as outfile:
            json.dump(response, outfile)

asyncio.get_event_loop().run_until_complete(my_loop())
