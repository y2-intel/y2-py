# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    name: Required[str]
    """Webhook display name"""

    url: Required[str]
    """Webhook endpoint URL (must be HTTPS)"""

    headers: Dict[str, str]
    """Custom headers to include in webhook deliveries"""

    secret: str
    """Shared secret for signature verification"""
