#!/usr/bin/env python3
# coding:utf-8

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import json

app = FastAPI()


# @app.middleware("http")
# async def res(request: Request, call_next):
#     response = await call_next(request)
#     print(response)
#     return response


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/apis/get_apis")
async def get_apis(api_type: str | None = None):
    apis = [
        {
            "id": 1,
            "type": 'a',
            'name': 'xxx',
        },
        {
            "id": 2,
            'type': 'b',
            'name': 'yyy',
        }
    ]
    res = {
        'code': 0,
        'msg': 'success',
        'data': {},
    }
    if not api_type:
        res['data'] = apis
    else:
        res['data'] = list(filter(lambda x: x['type'] == api_type, apis))
    return res


@app.get("/apis/get_type")
async def get_apis(api_type: str | None = None):
    res = {
        'code': 0,
        'msg': 'success',
        'content': ['a', 'b'],
    }
    return res


if __name__ == '__main__':
    ...
