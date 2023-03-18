from proto import kb_index_service_pb2, kb_index_service_pb2_grpc


# TODO
class KBIndexService(kb_index_service_pb2_grpc.KBIndexServiceServicer):
    def Create(self, request, context):
        print("create")
        return kb_index_service_pb2.KBIndexReply(ok=True)

    def Modify(self, request, context):
        print("modify")
        return kb_index_service_pb2.KBIndexReply(ok=True)

    def Delete(self, request, context):
        print("delete")
        return kb_index_service_pb2.KBIndexReply(ok=True)
