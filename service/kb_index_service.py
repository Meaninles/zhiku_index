from loguru import logger
from proto import kb_index_service_pb2, kb_index_service_pb2_grpc
from celery_service.kb_index import kbindex_task


# TODO
class KBIndexService(kb_index_service_pb2_grpc.KBIndexServiceServicer):
    def Create(self, request, context):
        print("KBIndexService creating")
        task_info = kbindex_task.delay("niubi")
        logger.info("索引任务已经提交，任务id：" + task_info.id)
        return kb_index_service_pb2.KBIndexReply(ok=True)

    def Modify(self, request, context):
        print("KBIndexService modify")
        return kb_index_service_pb2.KBIndexReply(ok=True)

    def Delete(self, request, context):
        print("KBIndexService delete")
        return kb_index_service_pb2.KBIndexReply(ok=True)
