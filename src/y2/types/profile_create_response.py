# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProfileCreateResponse", "Data", "Meta"]


class Data(BaseModel):
    profile_id: str = FieldInfo(alias="profileId")
    """The ID of the newly created profile"""


class Meta(BaseModel):
    message: Optional[str] = None


class ProfileCreateResponse(BaseModel):
    data: Data

    meta: Meta
