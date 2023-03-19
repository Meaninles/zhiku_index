from sqlalchemy import BIGINT, VARCHAR, Column, DATETIME
from initial.initial import Base


class ExaFileUploadAndDownloads(Base):
    __tablename__ = "exa_file_upload_and_downloads"
    id = Column(BIGINT, primary_key=True)
    created_at = Column(DATETIME)
    updated_at = Column(DATETIME)
    deleted_at = Column(DATETIME)
    name = Column(VARCHAR)
    url = Column(VARCHAR)
    tag = Column(VARCHAR)
    key = Column(VARCHAR)
    description = Column(VARCHAR)
    kb_id = Column(VARCHAR)
    indexed = Column(BIGINT)
    doc_id = Column(VARCHAR)
