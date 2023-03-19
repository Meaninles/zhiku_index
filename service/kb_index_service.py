import sqlalchemy
from initial.initial import sql_engine
from loguru import logger
from proto import kb_index_service_pb2, kb_index_service_pb2_grpc
from celery_service.kb_index import kbindex_task
from model.celery_model.kb_item import KBItemModel


# TODO
class KBIndexService(kb_index_service_pb2_grpc.KBIndexServiceServicer):
    def Create(self, request, context):
        kb_item = KBItemModel(
            kb_id=request.kb_id,
            name=request.name,
            url=request.url,
            tag=request.tag,
            key=request.key,
            description=request.description,
            indexed=request.indexed,
            id=request.id,
        )
        task_info = kbindex_task.delay(kb_item.json())
        logger.info("索引任务已经提交，任务id：" + task_info.id)
        return kb_index_service_pb2.KBIndexReply(ok=True)

    def Modify(self, request, context):
        logger.info("KBIndexService modify")
        return kb_index_service_pb2.KBIndexReply(ok=True)

    def Delete(self, request, context):
        logger.info("KBIndexService delete")
        return kb_index_service_pb2.KBIndexReply(ok=True)
