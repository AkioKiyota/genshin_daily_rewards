import asyncio
import genshin
from win32api import MessageBox

cookies = genshin.utility.get_browser_cookies()
async def main():
    client = genshin.Client(cookies=cookies, game=genshin.Game.GENSHIN)
    

    try:
        reward = await client.claim_daily_reward()
    except genshin.AlreadyClaimed:
        MessageBox(0, 'Already_Claimed', 'Genshin_Impact')
    else:
        MessageBox(0, f"Claimed {reward.amount}x {reward.name}", "Genshin_Impact")


asyncio.run(main())
