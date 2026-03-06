# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    headers: Dict[str, str]

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]

    name: str

    secret: str

    url: str
