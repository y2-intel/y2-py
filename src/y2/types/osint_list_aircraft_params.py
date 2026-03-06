# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["OsintListAircraftParams"]


class OsintListAircraftParams(TypedDict, total=False):
    limit: int
    """Maximum number of aircraft to return"""

    theater: str
    """Filter by theater ID (e.g. "iran", "taiwan", "baltic")"""
