import asyncio
import aiohttp

import phonenumbers

links = ['https://hands.ru/company/about',
         'https://repetitors.info/']


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    numbers = set()
    for link in links:
        async with aiohttp.ClientSession() as session:
            html = await fetch(session, link)
            for match in phonenumbers.PhoneNumberMatcher(html, 'RU'):
                phone_number = match.number
                numbers.add("8" + str(phone_number.national_number))
    numbers = list(numbers)

    print("Found numbers:")
    print(*numbers, sep='\n')


asyncio.run(main())
