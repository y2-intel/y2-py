# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ProfileListResponse",
    "Data",
    "DataProfile",
    "DataProfileConfiguration",
    "DataProfileConfigurationAudio",
    "DataProfileLinks",
    "DataProfileSchedule",
    "DataProfileVisibility",
    "DataSubscription",
    "DataSubscriptionDelivery",
    "DataSubscriptionLinks",
    "Links",
    "Meta",
    "MetaPage",
]


class DataProfileConfigurationAudio(BaseModel):
    enabled: bool

    instructions: Optional[str] = None

    speed: Optional[Literal["slow", "normal", "fast"]] = None


class DataProfileConfiguration(BaseModel):
    audio: DataProfileConfigurationAudio

    budget: Optional[object] = None

    freshness: Optional[object] = None

    model: Optional[object] = None

    recursion: Optional[object] = None

    search: Optional[object] = None

    tools: Optional[object] = None


class DataProfileLinks(BaseModel):
    reports: str

    self: str


class DataProfileSchedule(BaseModel):
    cron: str

    timezone: Literal["UTC"]


class DataProfileVisibility(BaseModel):
    community: bool

    global_: bool = FieldInfo(alias="global")


class DataProfile(BaseModel):
    id: str

    configuration: DataProfileConfiguration

    created_at: datetime = FieldInfo(alias="createdAt")

    custom_instructions: Optional[str] = FieldInfo(alias="customInstructions", default=None)

    frequency: Optional[Literal["daily", "weekly", "biweekly", "monthly"]] = None
    """Report generation frequency"""

    last_delivered_at: Optional[datetime] = FieldInfo(alias="lastDeliveredAt", default=None)

    links: DataProfileLinks

    name: str

    report_structure: Optional[str] = FieldInfo(alias="reportStructure", default=None)

    schedule: DataProfileSchedule

    status: Literal["active", "paused", "cancelled"]
    """Profile status"""

    tags: List[str]

    topic: str

    type: Literal["profile"]

    visibility: DataProfileVisibility


class DataSubscriptionDelivery(BaseModel):
    email_audience: Literal["individual", "workspace"] = FieldInfo(alias="emailAudience")
    """Email recipients for email-capable subscription delivery"""

    method: Literal["email", "sms", "webhook", "both_email_sms"]
    """Subscription delivery method"""

    webhook_id: Optional[str] = FieldInfo(alias="webhookId", default=None)


class DataSubscriptionLinks(BaseModel):
    delivery: str


class DataSubscription(BaseModel):
    id: str

    active: bool

    delivery: DataSubscriptionDelivery

    links: DataSubscriptionLinks

    profile_id: str = FieldInfo(alias="profileId")

    subscribed_at: datetime = FieldInfo(alias="subscribedAt")

    type: Literal["subscription"]


class Data(BaseModel):
    profile: Optional[DataProfile] = None

    subscription: DataSubscription


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


class ProfileListResponse(BaseModel):
    data: List[Data]

    links: Links

    meta: Meta
