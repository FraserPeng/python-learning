# 经纬度
import asyncio
import aiohttp
from aiohttp import web
import urllib.request as request
import json
import os
import re


async def fetch():
    url = 'https://blog.csdn.net/cds86333774/article/details/51009057'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            else:
                print('获取url数据报错')


def match(html):
    pattern = re.compile(
        '</span>.*?</span>.*?  (.*?) 北纬(.*?) 东经(.*?)<span', re.S)
    items = re.findall(pattern, html)
    print(items)
    return items


def loadCity():
    '''
    初始化城市数据
    '''
    with open('.\\reptile\\station_name_code.json', 'r', encoding='UTF-8') as f:
        text = f.read()
        return text


def import_lon_lat(items):
    result = loadCity()
    cities = json.loads(result)
    for city in cities:
        for each in items:
            lon = each[2]
            lat = each[1]
            name = each[0].split(' ')[-1].replace('市', '')
            print(lon, lat, name)
            if city['name'].find(name) > -1:
                city['lon'] = lon
                city['lat'] = lat
                break
    with open(".\\reptile\\station_info.json", 'w', encoding='UTF-8') as f:
            # 不以ascii码编码的方式保存
        json.dump(cities, f, ensure_ascii=False)


async def main():
    html = await fetch()
    items = match(html)
    import_lon_lat(items)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [main()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
