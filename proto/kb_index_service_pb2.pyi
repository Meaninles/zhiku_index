from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class KBIndexReply(_message.Message):
    __slots__ = ["ok"]
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    def __init__(self, ok: bool = ...) -> None: ...

class KBIndexRequest(_message.Message):
    __slots__ = ["description", "id", "indexed", "kb_id", "key", "name", "tag", "url"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INDEXED_FIELD_NUMBER: _ClassVar[int]
    KB_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    description: str
    id: int
    indexed: int
    kb_id: str
    key: str
    name: str
    tag: str
    url: str
    def __init__(self, name: _Optional[str] = ..., url: _Optional[str] = ..., tag: _Optional[str] = ..., key: _Optional[str] = ..., description: _Optional[str] = ..., indexed: _Optional[int] = ..., kb_id: _Optional[str] = ..., id: _Optional[int] = ...) -> None: ...
