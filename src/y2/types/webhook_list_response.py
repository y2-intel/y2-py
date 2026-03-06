# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebhookListResponse", "Data", "Meta"]


class Data(BaseModel):
    id: str
    """Webhook configuration ID"""

    created_at: int = FieldInfo(alias="createdAt")
    """Creation timestamp (ms)"""

    failure_count: int = FieldInfo(alias="failureCount")
    """Consecutive failure count (auto-disabled at 5)"""

    has_secret: bool = FieldInfo(alias="hasSecret")
    """Whether a secret is configured (actual secret is never exposed)"""

    is_active: bool = FieldInfo(alias="isActive")
    """Whether the webhook is active"""

    name: str
    """Webhook display name"""

    url: str
    """Webhook endpoint URL"""

    last_used_at: Optional[int] = FieldInfo(alias="lastUsedAt", default=None)
    """Last delivery timestamp (ms)"""

    updated_at: Optional[int] = FieldInfo(alias="updatedAt", default=None)
    """Last update timestamp (ms)"""


class Meta(BaseModel):
    count: Optional[int] = None


class WebhookListResponse(BaseModel):
    data: List[Data]

    meta: Meta
