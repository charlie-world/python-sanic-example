import asyncio
from concurrent.futures import ThreadPoolExecutor
from time import sleep

from sanic.blueprints import Blueprint
from sanic.request import Request
from sanic.response import json

app = Blueprint(  # pylint: disable=invalid-name
    'v1', version=1, strict_slashes=True
)


@app.get('/hello')
async def hello(request: Request):
    return json({'msg': 'hello'})


@app.get('/blocking-job')
async def blocking_job(request: Request):
    sleep(5)
    return json({'msg': 'blocking job was completed'})


@app.get('/blocking-job-with-thread-pool')
async def blocking_job_with_thread_pool(request: Request):
    with ThreadPoolExecutor() as pool:
        loop = asyncio.get_event_loop()

        def task():
            sleep(5)
            return json({'msg': 'blocking job with thread pool was completed'})

        return await loop.run_in_executor(pool, task)
