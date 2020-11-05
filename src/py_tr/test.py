from py_tr import TradeRepublicApi
tr = TradeRepublicApi()
# tr.initiate_device_reset()
# tr.complete_device_reset("4723") # Substitute the 2FA token that is sent to you via SMS.

import asyncio
import pprint

async def my_loop():
    print("async here")
    await tr.search_derivative("US0378331005")
    # await tr.search("DE000TT0GR32", asset_type="derivative")


    while True:
        print("while true")
        subscription_id, subscription, response = await tr.recv()
        pprint.pprint(response)

        # Or identify response by subscription type:
        # if subscription["type"] == "ticker":
        # print(f"Current tick for {subscription['id']} is {response}")

asyncio.get_event_loop().run_until_complete(my_loop())