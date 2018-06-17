#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: "fraser"
# Date: 2018-6-17
# 福利

import asyncio
import aiohttp
from aiohttp import web
import urllib.request as request
from bs4 import BeautifulSoup as bs
import json
import os
import uuid
import multiprocessing
import threading
from multiprocessing import Queue, Pool, Process

count = 1


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            else:
                raise Exception("这是一个错误")


class parseListPage():
    '''
    获取类型图片 一级页面
    '''

    def __init__(self, page_str):
        self.page_str = page_str

    def __enter__(self):
        page_str = self.page_str
        page = bs(page_str, 'html.parser')
        a = page.find('ul', attrs={'id': 'pins'}).find_all('li')
        images = []
        for child in a:
            obj = child.find_next('a')
            time = child.find_next('span', attrs={'class': 'time'}).text
            url = obj.get('href')
            images.append({'url': url, 'name': obj.find(
                'img').get('alt'), 'time': time})
        return images

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


async def praseImg(url, path):
    '''
    抓取图片
    '''
    try:
        
        html = await  fetch(url)
        page = bs(html, 'html.parser')
        print(url)
        img = page.find(
            'div', attrs={'class': 'main-image'}).find('img').get('src')
        await downImg(img, path)
    except Exception as e:
        print(e)
        raise Exception(e)


async def praseImgs(url):
    '''
    抓取二级页面网站
    '''
    try:
        imgs = []
        print('-------------- \033[1;35m 开始二级页面%s的抓取 \033[0m!' %  url)
        imgs.append(url)
        html = await  fetch(url)
        page = bs(html, 'html.parser')
        node = page.find('div', attrs={'class': 'pagenavi'}).find_all('a')
        if len(node)<4:
            return None
        a = node[-2].get('href').split('/')

        for i in range(2, int(a[-1])+1):
            imgs.append(url+'/'+str(i))
        print('-------------- \033[1;35m 完成二级页面%s的抓取 \033[0m!' % url)
        return {'folder': url.split('/')[-1], 'urls': imgs}
    except Exception as e:
        print(e)
        raise Exception(e)


async def downImg(url, path):
    global count
    count += 1
    print('-------------', path+'\\'+url.split('/')[-1])
    if os.path.exists(path+'\\'+url.split('/')[-1]):
        return
    header = {
        'Referer': url,
        'X-DevTools-Emulate-Network-Conditions-Client-Id': 'DB3AC464E06BFD77CD35121525D27455',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
    print('----------------- \033[1;35m 开始下载%s \033[0m!' % url)
    req = request.Request(url, headers=header)
    data = request.urlopen(req).read()
    print(' ---------------- \033[1;35m 完成下载%s \033[0m!' % url)
    with open(path+'\\'+url.split('/')[-1], 'wb') as f:
        print(count,'----',threading.current_thread())
        
        f.write(data)
        
        f.close()


async def main(url):
    # print(await praseImgs('http://www.mzitu.com/137510'))
    # await downImg('http://i.meizitu.net/2018/04/22b01.jpg', '11.jpg')
    # request.urlretrieve('http://i.meizitu.net/2018/06/13c02.jpg', '11.jpg')

    html = await fetch(url)
    print('开始%s页面的抓取' % url)
    with parseListPage(html) as tmp:
        print('完成%s页面的抓取' % url)
        for item in tmp:
            obj = await praseImgs(item['url'])
           
            if obj is None:
                continue
            o_path = 'd:\\work\\image\\%s' % item['time']
            path = o_path+'\\%s' % obj['folder']
            if os.path.exists(o_path) != True:
                os.mkdir(o_path)
            if os.path.exists(path) != True:
                os.mkdir(path)
            for str_url in obj['urls']:
                await praseImg(str_url, path)



def process_start(*pages):
    loop = asyncio.get_event_loop()
    tasks = [main(url) for url in pages]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
def task_start():
    pages = []
    # pages.append('http://www.mzitu.com')
    # p = Process(target=process_start, args=pages)
    # p.start()
    for page in range(20, 21):
        pages=[]
        pages.append("http://www.mzitu.com/page/%s" % page)
        p = Process(target=process_start, args=pages)
        p.start()


if __name__ == '__main__':
    task_start()


# loop = asyncio.get_event_loop()
# tasks = [main(url) for url in pages]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
