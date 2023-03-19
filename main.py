import grpc
from concurrent import futures
from proto import kb_index_service_pb2_grpc
from service.kb_index_service import KBIndexService


def serve():
    print(">>>>>>>>>>启动index rpc服务>>>>>>>>>>")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    kb_index_service_pb2_grpc.add_KBIndexServiceServicer_to_server(KBIndexService(), server)
    server.add_insecure_port('[::]:3743')
    server.start()
    server.wait_for_termination()


def init():
    print(">>>>>>>>>>初始化服务>>>>>>>>>>")


if __name__ == '__main__':
    init()
    serve()
