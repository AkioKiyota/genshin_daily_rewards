import asyncio
import genshin
import json
from win32api import MessageBox

f = open("data.json")
cookies = json.load(f)


async def main():
    client = genshin.Client(cookies=cookies, game=genshin.Game.GENSHIN)
    

    try:
        reward = await client.claim_daily_reward()
    except genshin.AlreadyClaimed:
        MessageBox(0, 'Already_Claimed', 'GayShit_Cumbag')
    else:
        MessageBox(0, f"Claimed {reward.amount}x {reward.name}", "GayShit_Cumbag")


asyncio.run(main())
