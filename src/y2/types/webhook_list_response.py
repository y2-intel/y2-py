# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebhookListResponse", "Data", "DataDeliveryHealth", "DataLinks", "DataSigning", "Links", "Meta", "MetaPage"]


class DataDeliveryHealth(BaseModel):
    consecutive_failures: int = FieldInfo(alias="consecutiveFailures")

    last_used_at: Optional[datetime] = FieldInfo(alias="lastUsedAt", default=None)


class DataLinks(BaseModel):
    self: str

    test: str


class DataSigning(BaseModel):
    algorithm: Optional[Literal["hmac-sha256"]] = None

    configured: bool


class Data(BaseModel):
    id: str
    """Stable public webhook configuration ID"""

    created_at: datetime = FieldInfo(alias="createdAt")

    custom_headers: List[str] = FieldInfo(alias="customHeaders")
    """Configured header names; values are never returned."""

    delivery_health: DataDeliveryHealth = FieldInfo(alias="deliveryHealth")

    links: DataLinks

    name: str
    """Webhook display name"""

    signing: DataSigning

    status: Literal["active", "disabled"]

    type: Literal["webhook"]

    updated_at: datetime = FieldInfo(alias="updatedAt")

    url: str
    """Webhook endpoint URL"""


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


class WebhookListResponse(BaseModel):
    data: List[Data]

    links: Links

    meta: Meta
