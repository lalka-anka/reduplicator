#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main(site):
    contains = ''
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, site)
        contains += html
    with open('page_code.txt', 'w') as file:
        file.write(contains)


def get_page_code(site):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(site))
