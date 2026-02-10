# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProfileUpdateResponse", "Data", "Meta"]


class Data(BaseModel):
    profile_id: str = FieldInfo(alias="profileId")

    success: bool


class Meta(BaseModel):
    message: Optional[str] = None


class ProfileUpdateResponse(BaseModel):
    data: Data

    meta: Meta
