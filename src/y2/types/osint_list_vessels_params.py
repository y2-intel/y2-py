# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["OsintListVesselsParams"]


class OsintListVesselsParams(TypedDict, total=False):
    limit: int
    """Maximum number of vessels to return"""

    region: str
    """Filter by region name"""
