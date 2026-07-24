# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ReportListResponse",
    "Data",
    "DataAudio",
    "DataIntelligence",
    "DataIntelligenceGraph",
    "Links",
    "Meta",
    "MetaPage",
]


class DataAudio(BaseModel):
    duration_seconds: Optional[float] = FieldInfo(alias="durationSeconds", default=None)

    media_type: Optional[str] = FieldInfo(alias="mediaType", default=None)

    status: Literal["available", "unavailable"]


class DataIntelligenceGraph(BaseModel):
    edge_count: int = FieldInfo(alias="edgeCount")

    incident_count: int = FieldInfo(alias="incidentCount")

    node_count: int = FieldInfo(alias="nodeCount")


class DataIntelligence(BaseModel):
    graph: Optional[DataIntelligenceGraph] = None

    signal_count: int = FieldInfo(alias="signalCount")


class Data(BaseModel):
    id: str

    audio: DataAudio

    generated_at: datetime = FieldInfo(alias="generatedAt")

    intelligence: DataIntelligence

    language: str

    links: Dict[str, Optional[str]]

    profile_id: str = FieldInfo(alias="profileId")

    published_at: datetime = FieldInfo(alias="publishedAt")

    status: Literal["published"]

    summary: Optional[str] = None

    topic: Optional[str] = None

    type: Literal["report"]


class Links(BaseModel):
    next: Optional[str] = None

    self: str


class MetaPage(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")

    limit: int

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)


class Meta(BaseModel):
    as_of: datetime = FieldInfo(alias="asOf")

    count: int

    has_more: bool = FieldInfo(alias="hasMore")

    is_done: bool = FieldInfo(alias="isDone")

    limit: int

    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)

    page: MetaPage

    page_count: int = FieldInfo(alias="pageCount")


class ReportListResponse(BaseModel):
    data: List[Data]

    links: Links

    meta: Meta
