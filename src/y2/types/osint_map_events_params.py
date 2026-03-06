# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["OsintMapEventsParams"]


class OsintMapEventsParams(TypedDict, total=False):
    limit: int
    """Maximum number of events to return"""

    region: Literal["mena", "africa", "latam", "asiapac", "europe", "namerica"]
    """Filter by geographic region"""
