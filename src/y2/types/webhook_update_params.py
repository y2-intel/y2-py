# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    name: Required[str]
    """Webhook display name"""

    url: Required[str]
    """Webhook endpoint URL (must be HTTPS)"""

    headers: Dict[str, str]
    """Custom headers to include in webhook deliveries"""

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]

    secret: str
    """Shared secret for signature verification"""

    if_match: Annotated[str, PropertyInfo(alias="If-Match")]
