# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .topic_enum import TopicEnum

__all__ = ["NewsListFeedsResponse", "Data", "Meta"]


class Data(BaseModel):
    id: TopicEnum
    """Available Y2 News Terminal feed topics"""

    color: str
    """UI gradient classes associated with the feed"""

    description: str
    """Feed description"""

    group: str
    """Machine-readable topic group ID"""

    group_label: str = FieldInfo(alias="groupLabel")
    """Human-readable topic group name"""

    ingest_ontology: bool = FieldInfo(alias="ingestOntology")
    """Whether eligible signals can enter the OSINT ontology pipeline"""

    name: str
    """Human-readable name"""

    short_label: str = FieldInfo(alias="shortLabel")
    """Compact display name"""


class Meta(BaseModel):
    count: Optional[int] = None

    default_topics: Optional[List[TopicEnum]] = FieldInfo(alias="defaultTopics", default=None)


class NewsListFeedsResponse(BaseModel):
    data: List[Data]

    meta: Meta
