# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["NewsListParams"]


class NewsListParams(TypedDict, total=False):
    cursor: str
    """Opaque continuation token from the previous response.

    Bound to the original filters and ordering.
    """

    format: Literal["json", "ndjson"]
    """Use `ndjson` for row-oriented streaming output."""

    limit: int
    """Maximum number of items to return"""

    topics: str
    """
    Comma-separated list of topics to filter by. Use `GET /news/feeds` to discover
    the current topic catalog. Default: crypto, geopolitics, macro, equities, ai,
    energy
    """
