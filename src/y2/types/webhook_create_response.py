# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebhookCreateResponse", "Data", "Meta"]


class Data(BaseModel):
    webhook_id: str = FieldInfo(alias="webhookId")
    """The ID of the newly created webhook configuration"""


class Meta(BaseModel):
    message: Optional[str] = None


class WebhookCreateResponse(BaseModel):
    data: Data

    meta: Meta
