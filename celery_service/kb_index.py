import openai
# TODO 换一个稳定的
openai.api_base = "https://yixin.cyou/v1"
import asyncio
import os.path
from celery_service import celery_service
from model.celery_model.kb_item import KBItemModel
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
from conf.config import KB_INDEX_JSON_DIR
from conf.api_key import OPENAI_API_KEY
from initial.initial import sql_session, kb_file_table
from model.db_model.exa_file_upload_and_downloads import ExaFileUploadAndDownloads
from loguru import logger


@celery_service.task
def kbindex_task(kb_item_json):
    return run_async(kbindex_task_txt_insert(kb_item_json))


async def kbindex_task_txt_insert(kb_item_json):
    try:
        os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
        kb_item = KBItemModel.parse_raw(kb_item_json)
        logger.info(kb_item.indexed)
        logger.info(kb_item)

        # TODO 改成使用对象存储保存index json文件
        logger.info("kb index json dir: " + KB_INDEX_JSON_DIR)
        index_json_path = KB_INDEX_JSON_DIR + kb_item.kb_id + '.json'
        docs = SimpleDirectoryReader(input_files=[kb_item.url]).load_data()
        if os.path.exists(index_json_path):
            index = GPTSimpleVectorIndex.load_from_disk(index_json_path)
        else:
            file_dir = os.path.split(index_json_path)[0]
            if not os.path.exists(file_dir):
                os.makedirs(file_dir)
            os.system(r'touch %s' % index_json_path)
            index = GPTSimpleVectorIndex([])
        logger.info("开始建立索引")
        # TODO index要消耗token，先注释掉
        # for doc in docs:
        #     index.insert(doc)
        index.save_to_disk(index_json_path)
        kb_file = sql_session.query(ExaFileUploadAndDownloads).filter_by(key=kb_item.key).first()
        kb_file.indexed = 1
        kb_file.doc_id = docs[0].get_doc_id()
        sql_session.commit()
        logger.info("结束建立索引")
        return "success"
    finally:
        logger.info("索引任务已经结束")


def run_async(coroutine):
    return asyncio.run(coroutine)
