from pydantic import BaseModel


class KBItemModel(BaseModel):

    id: int = None
    name: str = None
    url: str = None
    tag: str = None
    key: str = None
    description: str = None
    kb_id: str = None
    indexed: int = None
