import os

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import aioredis
from conf.address import REDIS_ADDRESS
from conf.api_key import OPENAI_API_KEY
from model import Base


sql_engine = create_engine('mysql+pymysql://root:lvyang8288@127.0.0.1:3306/zhiku')
Session = sessionmaker(bind=sql_engine)
sql_session = Session()
redis_client = aioredis.from_url(REDIS_ADDRESS,
                              encoding="utf-8",
                              decode_responses=True)

kb_file_table = sqlalchemy.Table('exa_file_upload_and_downloads', sqlalchemy.MetaData(), autoload=True,
                                 autoload_with=sql_engine)


def init_sql_session():
    # global sql_engine, sql_session
    # sql_engine = create_engine('mysql+pymysql://root:lvyang8288@127.0.0.1:3306/zhiku')
    Base.metadata.create_all(sql_engine)
    # sql_session = sessionmaker(sql_engine)


def init_redis_pool():
    # 注意这个也是需要容器内才可以！---
    # redis = await aioredis.create_redis(address, password=password)
    # 会自动的复用链接，也就是自动的启用连接池
    # global redis_client
    redis_client = aioredis.from_url(REDIS_ADDRESS,
                              encoding="utf-8",
                              decode_responses=True)


def init_api_key():
    os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
