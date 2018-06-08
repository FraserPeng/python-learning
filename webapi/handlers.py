#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from coreweb import get
import math
import json


@get('/')
async def hello(request):
    return "hello world"


@get('/circle/{r}')
async def circle(r, request):
    try:
        R = int(r, 0)
        
        if isinstance(R, int):
            c = math.pi * pow(R, 2)
            return {
                "name": "半径为%s的圆面积" % R,
                "value": round(c,2)
            }
    except ValueError:
        raise ValueError("r 必须为整数")
