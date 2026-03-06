# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["OsintGetGpsJammingZonesParams"]


class OsintGetGpsJammingZonesParams(TypedDict, total=False):
    limit: int
    """Maximum number of zones to return"""

    severity: Literal["low", "moderate", "severe", "critical"]
    """Filter by interference severity"""
