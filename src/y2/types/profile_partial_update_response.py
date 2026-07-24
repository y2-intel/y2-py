# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ProfilePartialUpdateResponse",
    "Data",
    "DataConfiguration",
    "DataConfigurationAudio",
    "DataLinks",
    "DataSchedule",
    "DataVisibility",
    "Meta",
]


class DataConfigurationAudio(BaseModel):
    enabled: bool

    instructions: Optional[str] = None

    speed: Optional[Literal["slow", "normal", "fast"]] = None


class DataConfiguration(BaseModel):
    audio: DataConfigurationAudio

    budget: Optional[object] = None

    freshness: Optional[object] = None

    model: Optional[object] = None

    recursion: Optional[object] = None

    search: Optional[object] = None

    tools: Optional[object] = None


class DataLinks(BaseModel):
    reports: str

    self: str


class DataSchedule(BaseModel):
    cron: str

    timezone: Literal["UTC"]


class DataVisibility(BaseModel):
    community: bool

    global_: bool = FieldInfo(alias="global")


class Data(BaseModel):
    id: str

    configuration: DataConfiguration

    created_at: datetime = FieldInfo(alias="createdAt")

    custom_instructions: Optional[str] = FieldInfo(alias="customInstructions", default=None)

    frequency: Optional[Literal["daily", "weekly", "biweekly", "monthly"]] = None
    """Report generation frequency"""

    last_delivered_at: Optional[datetime] = FieldInfo(alias="lastDeliveredAt", default=None)

    links: DataLinks

    name: str

    report_structure: Optional[str] = FieldInfo(alias="reportStructure", default=None)

    schedule: DataSchedule

    status: Literal["active", "paused", "cancelled"]
    """Profile status"""

    tags: List[str]

    topic: str

    type: Literal["profile"]

    visibility: DataVisibility


class Meta(BaseModel):
    message: Optional[str] = None


class ProfilePartialUpdateResponse(BaseModel):
    data: Data

    meta: Meta
