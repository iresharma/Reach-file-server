# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import pb.fileServer_pb2 as fileServer__pb2

GRPC_GENERATED_VERSION = '1.65.4'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.66.0'
SCHEDULED_RELEASE_DATE = 'August 6, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in fileServer_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class FileServerPackageStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.InitializeFileServer = channel.unary_unary(
                '/file_server_package.FileServerPackage/InitializeFileServer',
                request_serializer=fileServer__pb2.InitServerRequest.SerializeToString,
                response_deserializer=fileServer__pb2.InitServerResponse.FromString,
                _registered_method=True)
        self.GetServerInfo = channel.unary_unary(
                '/file_server_package.FileServerPackage/GetServerInfo',
                request_serializer=fileServer__pb2.GetServerRequest.SerializeToString,
                response_deserializer=fileServer__pb2.GetServerResponse.FromString,
                _registered_method=True)
        self.ListFile = channel.unary_unary(
                '/file_server_package.FileServerPackage/ListFile',
                request_serializer=fileServer__pb2.ListFileRequest.SerializeToString,
                response_deserializer=fileServer__pb2.ListFileResponse.FromString,
                _registered_method=True)
        self.PreSignedGet = channel.unary_unary(
                '/file_server_package.FileServerPackage/PreSignedGet',
                request_serializer=fileServer__pb2.GetFileRequest.SerializeToString,
                response_deserializer=fileServer__pb2.GetFileResponse.FromString,
                _registered_method=True)
        self.PreSignedDelete = channel.unary_unary(
                '/file_server_package.FileServerPackage/PreSignedDelete',
                request_serializer=fileServer__pb2.FileOperationRequest.SerializeToString,
                response_deserializer=fileServer__pb2.OkResponse.FromString,
                _registered_method=True)
        self.PreSignedPut = channel.unary_unary(
                '/file_server_package.FileServerPackage/PreSignedPut',
                request_serializer=fileServer__pb2.FileOperationRequest.SerializeToString,
                response_deserializer=fileServer__pb2.OkResponse.FromString,
                _registered_method=True)


class FileServerPackageServicer(object):
    """Missing associated documentation comment in .proto file."""

    def InitializeFileServer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServerInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PreSignedGet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PreSignedDelete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PreSignedPut(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileServerPackageServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'InitializeFileServer': grpc.unary_unary_rpc_method_handler(
                    servicer.InitializeFileServer,
                    request_deserializer=fileServer__pb2.InitServerRequest.FromString,
                    response_serializer=fileServer__pb2.InitServerResponse.SerializeToString,
            ),
            'GetServerInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServerInfo,
                    request_deserializer=fileServer__pb2.GetServerRequest.FromString,
                    response_serializer=fileServer__pb2.GetServerResponse.SerializeToString,
            ),
            'ListFile': grpc.unary_unary_rpc_method_handler(
                    servicer.ListFile,
                    request_deserializer=fileServer__pb2.ListFileRequest.FromString,
                    response_serializer=fileServer__pb2.ListFileResponse.SerializeToString,
            ),
            'PreSignedGet': grpc.unary_unary_rpc_method_handler(
                    servicer.PreSignedGet,
                    request_deserializer=fileServer__pb2.GetFileRequest.FromString,
                    response_serializer=fileServer__pb2.GetFileResponse.SerializeToString,
            ),
            'PreSignedDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.PreSignedDelete,
                    request_deserializer=fileServer__pb2.FileOperationRequest.FromString,
                    response_serializer=fileServer__pb2.OkResponse.SerializeToString,
            ),
            'PreSignedPut': grpc.unary_unary_rpc_method_handler(
                    servicer.PreSignedPut,
                    request_deserializer=fileServer__pb2.FileOperationRequest.FromString,
                    response_serializer=fileServer__pb2.OkResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'file_server_package.FileServerPackage', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('file_server_package.FileServerPackage', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class FileServerPackage(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def InitializeFileServer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/file_server_package.FileServerPackage/InitializeFileServer',
            fileServer__pb2.InitServerRequest.SerializeToString,
            fileServer__pb2.InitServerResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetServerInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/file_server_package.FileServerPackage/GetServerInfo',
            fileServer__pb2.GetServerRequest.SerializeToString,
            fileServer__pb2.GetServerResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/file_server_package.FileServerPackage/ListFile',
            fileServer__pb2.ListFileRequest.SerializeToString,
            fileServer__pb2.ListFileResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PreSignedGet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/file_server_package.FileServerPackage/PreSignedGet',
            fileServer__pb2.GetFileRequest.SerializeToString,
            fileServer__pb2.GetFileResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PreSignedDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/file_server_package.FileServerPackage/PreSignedDelete',
            fileServer__pb2.FileOperationRequest.SerializeToString,
            fileServer__pb2.OkResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PreSignedPut(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/file_server_package.FileServerPackage/PreSignedPut',
            fileServer__pb2.FileOperationRequest.SerializeToString,
            fileServer__pb2.OkResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
