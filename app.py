from concurrent import futures

import grpc

from pb.fileServer_pb2_grpc import FileServerPackageServicer, add_FileServerPackageServicer_to_server
from pb.fileServer_pb2 import InitServerRequest, InitServerResponse, GetFileRequest, GetFileResponse, OkResponse
import database as db
import r2.R2Wrapper as r2


class Service(FileServerPackageServicer):

    def __init__(self):
        self.r2 = r2.R2Wrapper()

    def InitializeFileServer(self, request: InitServerRequest, context):
        account_info = db.get_account_details(request.userAccount)
        self.r2.init_bucket(request.userAccount, account_info)
        board = db.create_bucket(request.userAccount)
        return InitServerResponse(id=board)

    def GetServerInfo(self, req, context):
        pass

    def ListFile(self, req, context):
        pass

    def PreSignedGet(self, req: GetFileRequest, context):
        link = self.r2.pre_signed_get(req.userAccountId, req.path)
        return GetFileResponse(getUrl=link)

    def PreSignedDelete(self, req: GetFileRequest, context):
        self.r2.delete_object(req.userAccountId, req.path)
        return OkResponse()

    def PreSignedPut(self, req: GetFileRequest, context):
        resp = self.r2.pre_signed_put(req.userAccountId, req.path)
        return GetFileResponse(getUrl=resp)


if __name__ == "__main__":
    port = "4040"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_FileServerPackageServicer_to_server(Service(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()
