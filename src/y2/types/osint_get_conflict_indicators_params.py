# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["OsintGetConflictIndicatorsParams"]


class OsintGetConflictIndicatorsParams(TypedDict, total=False):
    category: Literal[
        "seismic",
        "conflict",
        "political",
        "economic",
        "weather",
        "health",
        "cyber",
        "maritime",
        "fire",
        "aviation",
        "other",
    ]
    """Filter by event category"""

    cursor: str
    """Opaque continuation token from the previous response.

    Bound to the original filters and ordering.
    """

    format: Literal["json", "ndjson"]
    """`json` uses the resource envelope; `ndjson` streams one canonical row per line."""

    limit: int
    """Maximum number of items to return"""

    region: Literal["mena", "africa", "latam", "asiapac", "europe", "namerica"]
    """Filter by geographic region"""
