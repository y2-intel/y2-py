# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .topic_enum import TopicEnum

__all__ = ["NewsListResponse", "Data", "DataLinks", "DataSentiment", "DataSource", "Links", "Meta", "MetaPage"]


class DataLinks(BaseModel):
    canonical: Optional[str] = None


class DataSentiment(BaseModel):
    label: Optional[Literal["bullish", "bearish", "neutral"]] = None
    """Sentiment classification for news items"""

    value: float


class DataSource(BaseModel):
    id: str

    language: Optional[str] = None

    published_at: datetime = FieldInfo(alias="publishedAt")

    publisher: Optional[str] = None

    retrieved_at: Optional[datetime] = FieldInfo(alias="retrievedAt", default=None)

    source_type: str = FieldInfo(alias="sourceType")

    title: Optional[str] = None

    url: Optional[str] = None


class Data(BaseModel):
    id: str

    author: Optional[str] = None

    content: str

    links: DataLinks

    published_at: datetime = FieldInfo(alias="publishedAt")

    sentiment: DataSentiment

    sources: List[DataSource]

    summary: str

    title: str

    topics: List[str]

    type: Literal["news"]


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

    topics: List[TopicEnum]


class NewsListResponse(BaseModel):
    data: List[Data]

    links: Links

    meta: Meta
