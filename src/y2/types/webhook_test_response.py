# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebhookTestResponse", "Data", "Meta"]


class Data(BaseModel):
    success: bool

    error: Optional[str] = None
    """Error message if the test failed"""

    response_time: Optional[int] = FieldInfo(alias="responseTime", default=None)
    """Response time in milliseconds"""

    status_code: Optional[int] = FieldInfo(alias="statusCode", default=None)
    """HTTP status code from the webhook endpoint"""


class Meta(BaseModel):
    message: Optional[str] = None


class WebhookTestResponse(BaseModel):
    data: Data

    meta: Meta
