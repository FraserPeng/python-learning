
# Author: fraser
# Date: 2018-6-20
# 抓取全国高铁动车运营时刻表
'''
由于抓取的城市列表太多，故 只取 省会城市和一些有高铁的重点城市
以其中一个城市为始发站，以其他城市为终点站，进行遍历，抓取数据
'''
import asyncio
import aiohttp
from aiohttp import web
import urllib.request as request
import json
import os
from multiprocessing import Queue, Pool, Process
import time


def loadCity():
    '''
    初始化城市数据
    '''
    with open('.\\reptile\\capital_code.json', 'r', encoding='UTF-8') as f:
        text = f.read()
        return text


class Station(object):

    def __init__(self):
        self.fileName = "station_name_code.json"

    async def fetch(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    print('获取url数据报错')

    async def save_station_code(self):
        data = []
        url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'
        result = await self.fetch(url)
        for each in result.split('=')[1].split('@'):
            name_code_dict = {}
            if each != "'":
                # 对读取的行都进行split操作,然后提取站点名和其代码
                name = each.split('|')[1]  # 站点名字
                code = each.split('|')[2]  # 每个站点对应的代码
                # 每个站点肯定都是唯一的
                name_code_dict['name'] = name
                name_code_dict['code'] = code
                data.append(name_code_dict)
        # 把name,code保存到本地文件中,方便以后使用
        with open('.\\reptile\\' + self.fileName, 'w', encoding='UTF-8') as f:
            # 不以ascii码编码的方式保存
            json.dump(data, f, ensure_ascii=False)

    async def query_ticket(self, from_station, to_station, train_date):
        '''
        查询高铁票
        '''
        query_param = 'leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT' % (
            train_date, from_station, to_station)

        url = 'https://kyfw.12306.cn/otn/leftTicket/query?%s' % query_param
        a = await self.fetch(url)

        if a.find('httpstatus') == -1:
            print('请求报错', url)
            return
        print(url)
        result = dict(json.loads(a))

        if result and result.get('data') and result.get('data').get('map'):
            train_info = result.get('data').get('result')
            for item in train_info:
                split_item = item.split('|')
                item_dict = {}
                # for index, item in enumerate(split_item, 0):
                #     print('{}:\t{}'.format(index, item))

                item_dict['train_name'] = split_item[3]  # 车次名
                item_dict['train_code'] = split_item[2]  # 车次编码
                item_dict['departure_station'] = split_item[4]  # 始发站
                item_dict['destination_station'] = split_item[5]  # 终点站
                # item_dict['arrive_time'] = split_item[9]  # 到站时间
                # item_dict['spend_time'] = split_item[10]  # 经历时长
                # item_dict['wz'] = split_item[29]  # 无座
                # item_dict['yz'] = split_item[28]  # 硬座
                # item_dict['yw'] = split_item[26]  # 硬卧
                # item_dict['rw'] = split_item[23]  # 软卧
                # item_dict['td'] = split_item[32]  # 特等座
                # item_dict['yd'] = split_item[31]  # 一等座
                # item_dict['ed'] = split_item[30]  # 二等座
                # item_dict['dw'] = split_item[33]  # 动卧
                if item_dict['train_name'][0] == 'G' or item_dict['train_name'][0] == 'C' or item_dict['train_name'][0] == 'D':
                    await self.quey_train(
                        item_dict['train_name'], item_dict['train_code'], item_dict['departure_station'], item_dict['destination_station'], train_date)

        else:
            print("从%s 到 %s 没有高铁" % (from_station, to_station))

    async def quey_train(self, trains_name, train_code, start_code, end_code, time):
        '''
        查询车次详情
        '''
        url = 'https://kyfw.12306.cn/otn/czxx/queryByTrainNo?train_no=%s&from_station_telecode=%s&to_station_telecode=%s&depart_date=%s' % (
            train_code, start_code, end_code, time)
        a = await self.fetch(url)
        result = dict(json.loads(a))
        if result.get('data').get('data'):
            train_info = result.get('data').get('data')
            with open('.\\reptile\\trains\\trains_' + trains_name + '.json', 'w+', encoding='UTF-8') as f:
                json.dump(train_info, f, ensure_ascii=False)
                f.close()


a = Station()
result = loadCity()
cities = json.loads(result)


def process_start(*cities):
    loop = asyncio.get_event_loop()
    # tasks = [a.query_ticket(cities[0], obj['code'], '2018-07-20')
    #          for obj in cities[1]]
    # loop.run_until_complete(asyncio.wait(tasks))
    # loop.close()


def task_start():
    for city in cities[:1]:
        p = Process(target=process_start, args=(
                    city['code'], cities[1:]))
        p.start()


if __name__ == '__main__':
    # task_start()
    result = loadCity()

    cities = json.loads(result)
    loop = asyncio.get_event_loop()
    # 31
    tasks = [a.query_ticket(cities[42]['code'], obj['code'],
                            '2018-07-01') for obj in cities[:97]]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    
    # rootdir = '.\\reptile\\trains'
    # list = os.listdir(rootdir)
    # for i in range(0, len(list)):
    #     path = os.path.join(rootdir, list[i])
    #     if os.path.isfile(path):
    #             print(path)

    # 生成省会城市代码
    # capital = ['北京', '天津', '沈阳', '长春', '哈尔滨', '石家庄', '呼和浩特', '包头', '郑州', '济南', '青岛', '南京', '上海', '杭州',
    #            '武汉', '南昌', '福州', '长沙', '广州', '深圳', '厦门', '珠海', '中山', '南宁', '昆明', '贵阳', '成都', '重庆', '西安',
    #             '拉萨', '西宁', '兰州','银川', '乌鲁木齐']
    # data=[]
    # for item in capital:
    #     for each in cities:
    #         if item in each['name']:
    #            data.append(each)
    # with open('.\\reptile\\capital_code.json','w',encoding='UTF-8') as f:
    #     json.dump(data, f, ensure_ascii=False)
    #     f.close()
