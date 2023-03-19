import grpc
from concurrent import futures
from proto import kb_index_service_pb2_grpc
from service.kb_index_service import KBIndexService
import initial.initial as initial
from loguru import logger


def serve():
    logger.info(">>>>>>>>>>启动index rpc服务>>>>>>>>>>")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    kb_index_service_pb2_grpc.add_KBIndexServiceServicer_to_server(KBIndexService(), server)
    server.add_insecure_port('[::]:3743')
    server.start()
    logger.info(">>>>>>>>>>index rpc服务启动成功>>>>>>>>>>")
    server.wait_for_termination()


def init():
    logger.info(">>>>>>>>>>初始化>>>>>>>>>>")
    initial.init_api_key()
    initial.init_redis_pool()
    initial.init_sql_session()


if __name__ == '__main__':
    init()
    serve()
