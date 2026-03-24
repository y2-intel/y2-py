# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SubscriptionUpdateDeliveryResponse", "Data", "Meta"]


class Data(BaseModel):
    delivery_method: Literal["email", "sms", "webhook", "both_email_sms"] = FieldInfo(alias="deliveryMethod")
    """Subscription delivery method"""

    subscription_id: str = FieldInfo(alias="subscriptionId")

    success: bool


class Meta(BaseModel):
    message: Optional[str] = None


class SubscriptionUpdateDeliveryResponse(BaseModel):
    data: Data

    meta: Meta
