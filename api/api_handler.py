import sys
import asyncio
import aiohttp
import json

base_url = 'https://www.reddit.com/r/'


class ApiHandler:
    def __init__(self):
        print('created ')
        self.loop = asyncio.get_event_loop()
        self.client = aiohttp.ClientSession(loop=self.loop)

    async def get_json(self, client, url):
        async with client.get(url) as response:
            assert response.status == 200
            return await response.read()

    async def get_reddit_top(self, sub_reddit):
        api = '/top.json?sort=top&t=day&limit=5'
        data1 = await self.get_json(self.client, base_url + sub_reddit + api)

        j = json.loads(data1.decode('utf-8'))
        for i in j['data']['children']:
            score = i['data']['score']
            title = i['data']['title']
            link = i['data']['url']
            print(str(score) + ': ' + title + ' (' + link + ')')

        print('Fetched:', sub_reddit + '\n')

    def signal_handler(self, frame, signal):
        print('loop should be stopped')
        self.loop.stop()
        self.client.close()
        sys.exit(0)

    def complete_loop(self, future):
        self.loop.run_until_complete(future)
