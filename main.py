import aiohttp
import asyncio
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

links = ['https://hands.ru/company/about',
         'https://repetitors.info/']


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    for link in links:
        async with aiohttp.ClientSession() as session:
            html = await fetch(session, link)
            print(html)


asyncio.run(main())
