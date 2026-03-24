# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["OsintListEventsParams"]


class OsintListEventsParams(TypedDict, total=False):
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

    limit: int
    """Maximum number of events to return"""

    severity: Literal["low", "medium", "high", "critical"]
    """Filter by severity level"""
