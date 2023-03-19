import asyncio
import base64

from loguru import logger
from celery_service import celery_service
import requests
import json
import conf.address
import time
import aioredis
from conf.address import REDIS_ADDRESS


@celery_service.task
def kbindex_task(kbindex_info):
    return run_async(kbindex_task_txt(kbindex_info))


async def kbindex_task_txt(kbindex_info):
    # redis_cli = None
    try:
        # redis_cli = aioredis.from_url(REDIS_ADDRESS,
        #                               encoding="utf-8",
        #                               decode_responses=True)
        # if not await redis_cli.exists(task_id):
        #     logger.info("has no such task: " + task_id + ", stop upload")
        #     return "failed"
        # user_id = await redis_cli.get(task_id)
        # if user_id is None or user_id == '':
        #     logger.info("user_id is none, no need to upload pic")
        #     return "failed"
        # TODO 实现txt index逻辑，index将会异步进行
        print("索引任务已经启动, info: " + kbindex_info)
        time.sleep(8)
        return "success"
    finally:
        print("索引任务已经结束")
        # delete task_id from redis when exit
        # if redis_cli is None:
        #     logger.error("redis_cli init failed")
        #     return "failed"
        # await redis_cli.delete(task_id)
        # await redis_cli.close()



def run_async(coroutine):
    return asyncio.run(coroutine)
