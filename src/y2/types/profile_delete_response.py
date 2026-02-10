# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProfileDeleteResponse", "Data", "Meta"]


class Data(BaseModel):
    deleted: bool

    profile_id: str = FieldInfo(alias="profileId")


class Meta(BaseModel):
    message: Optional[str] = None


class ProfileDeleteResponse(BaseModel):
    data: Data

    meta: Meta
