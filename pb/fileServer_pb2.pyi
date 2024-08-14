from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InitServerRequest(_message.Message):
    __slots__ = ["userAccount"]
    USERACCOUNT_FIELD_NUMBER: _ClassVar[int]
    userAccount: str
    def __init__(self, userAccount: _Optional[str] = ...) -> None: ...

class GetServerRequest(_message.Message):
    __slots__ = ["bucketId"]
    BUCKETID_FIELD_NUMBER: _ClassVar[int]
    bucketId: str
    def __init__(self, bucketId: _Optional[str] = ...) -> None: ...

class FileOperationRequest(_message.Message):
    __slots__ = ["path", "bucketId"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    BUCKETID_FIELD_NUMBER: _ClassVar[int]
    path: str
    bucketId: str
    def __init__(self, path: _Optional[str] = ..., bucketId: _Optional[str] = ...) -> None: ...

class ListFileRequest(_message.Message):
    __slots__ = ["bucketId", "path"]
    BUCKETID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    bucketId: str
    path: str
    def __init__(self, bucketId: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class GetFileRequest(_message.Message):
    __slots__ = ["userAccountId", "path"]
    USERACCOUNTID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    userAccountId: str
    path: str
    def __init__(self, userAccountId: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class GetFileResponse(_message.Message):
    __slots__ = ["getUrl"]
    GETURL_FIELD_NUMBER: _ClassVar[int]
    getUrl: str
    def __init__(self, getUrl: _Optional[str] = ...) -> None: ...

class InitServerResponse(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetServerResponse(_message.Message):
    __slots__ = ["bucketName", "metadata"]
    BUCKETNAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    bucketName: str
    metadata: BucketMetaData
    def __init__(self, bucketName: _Optional[str] = ..., metadata: _Optional[_Union[BucketMetaData, _Mapping]] = ...) -> None: ...

class BucketMetaData(_message.Message):
    __slots__ = ["size", "name", "creationDate", "count"]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATIONDATE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    size: str
    name: str
    creationDate: str
    count: int
    def __init__(self, size: _Optional[str] = ..., name: _Optional[str] = ..., creationDate: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class File(_message.Message):
    __slots__ = ["lastModified", "filename", "size"]
    LASTMODIFIED_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    lastModified: float
    filename: str
    size: str
    def __init__(self, lastModified: _Optional[float] = ..., filename: _Optional[str] = ..., size: _Optional[str] = ...) -> None: ...

class ListFileResponse(_message.Message):
    __slots__ = ["files", "folder"]
    FILES_FIELD_NUMBER: _ClassVar[int]
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[File]
    folder: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, files: _Optional[_Iterable[_Union[File, _Mapping]]] = ..., folder: _Optional[_Iterable[str]] = ...) -> None: ...

class OkResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...
