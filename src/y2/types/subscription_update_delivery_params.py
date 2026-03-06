# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SubscriptionUpdateDeliveryParams"]


class SubscriptionUpdateDeliveryParams(TypedDict, total=False):
    delivery_method: Required[
        Annotated[Literal["email", "sms", "webhook", "both_email_sms"], PropertyInfo(alias="deliveryMethod")]
    ]
    """Subscription delivery method"""

    webhook_config_id: Annotated[str, PropertyInfo(alias="webhookConfigId")]
    """Required when deliveryMethod is "webhook" """
