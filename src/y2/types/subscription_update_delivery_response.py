# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SubscriptionUpdateDeliveryResponse", "Data", "DataDelivery", "DataLinks", "Meta"]


class DataDelivery(BaseModel):
    email_audience: Literal["individual", "workspace"] = FieldInfo(alias="emailAudience")
    """Email recipients for email-capable subscription delivery"""

    method: Literal["email", "sms", "webhook", "both_email_sms"]
    """Subscription delivery method"""

    webhook_id: Optional[str] = FieldInfo(alias="webhookId", default=None)


class DataLinks(BaseModel):
    delivery: str


class Data(BaseModel):
    id: str

    delivery: DataDelivery

    links: DataLinks

    type: Literal["subscription"]


class Meta(BaseModel):
    message: Optional[str] = None


class SubscriptionUpdateDeliveryResponse(BaseModel):
    data: Data

    meta: Meta
