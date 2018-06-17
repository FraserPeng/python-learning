#! /usr/bin/env python
# -*- coding:utf-8 -*-

import asyncio
import threading
import multiprocessing
from multiprocessing import Queue ,Pool,Process
#import aiohttp
import os

async def hello(name):
    print(" \033[1;35m hello %s %s**********%s \033[0m " % (name,os.getpid(),threading.current_thread()))
    #await asyncio.sleep(int(name))
    await asyncio.sleep(1)
    print('end:{}{}'.format(name,os.getpid()))

def process_start(*namelist):
    tasks=[]
    loop=asyncio.get_event_loop()
    for name in namelist:
        tasks.append(asyncio.ensure_future(hello(name)))
    loop.run_until_complete(asyncio.wait(tasks))

def task_start(namelist):
    i=0
    lst=[]
    flag=10
    while namelist:
        i+=1
        l=namelist.pop()
        lst.append(l)
        if i==flag:
            p=Process(target=process_start,args=lst)
            p.start()
            #p.join()
            lst=[]
            i=0
    if namelist!=[]:
        p=Process(target=process_start,args=lst)
        p.start()
        #p.join()
if __name__=='__main__':
    # namelist=list('0123456789'*10)
    # task_start(namelist)
    a =[1,2,None,4]
    for item in a:
        if item is None:
            continue
        print(item)


# loop=asyncio.get_event_loop()
# tasks=[]
# namelist=list('0123456789'*10)
# for i in namelist:
#     tasks.append(asyncio.ensure_future(hello(i)))
# loop.run_until_complete(asyncio.wait(tasks))
