# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebhookUpdateResponse", "Data", "Meta"]


class Data(BaseModel):
    success: bool

    webhook_id: str = FieldInfo(alias="webhookId")


class Meta(BaseModel):
    message: Optional[str] = None


class WebhookUpdateResponse(BaseModel):
    data: Data

    meta: Meta
