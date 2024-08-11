from concurrent import futures

import grpc

from pb.fileServer_pb2_grpc import FileServerPackageServicer, add_FileServerPackageServicer_to_server
from pb.fileServer_pb2 import InitServerRequest, InitServerResponse
import database as db
import r2.R2Wrapper as r2


class Service(FileServerPackageServicer):
    def InitializeFileServer(self, request: InitServerRequest, context):
        account_info = db.get_account_details(request.userAccount)
        r2.R2Wrapper().init_bucket(request.userAccount, account_info)
        board = db.create_bucket(request.userAccount)
        return InitServerResponse(id=board)

    def GetServerInfo(self, req, context):
        pass

    def ListFile(self, req, context):
        pass

    def PreSignedGet(self, req, context):
        pass

    def PreSignedDelete(self, req, context):
        pass

    def PreSignedPut(self, req, context):
        pass


if __name__ == "__main__":
    port = "4040"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_FileServerPackageServicer_to_server(Service(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()
