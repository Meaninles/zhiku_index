import aioredis
from conf.address import REDIS_ADDRESS


def get_redis_pool():
    # 注意这个也是需要容器内才可以！---
    # redis = await aioredis.create_redis(address, password=password)
    # 会自动的复用链接，也就是自动的启用连接池
    redis = aioredis.from_url(REDIS_ADDRESS,
                              encoding="utf-8",
                              decode_responses=True)
    return redis
