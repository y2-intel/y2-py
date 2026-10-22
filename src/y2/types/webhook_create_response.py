# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebhookCreateResponse", "Data", "DataDeliveryHealth", "DataLinks", "DataSigning", "Meta"]


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


class Meta(BaseModel):
    message: Optional[str] = None


class WebhookCreateResponse(BaseModel):
    data: Data

    meta: Meta
