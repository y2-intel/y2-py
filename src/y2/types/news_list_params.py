# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["NewsListParams"]


class NewsListParams(TypedDict, total=False):
    country_code: Annotated[str, PropertyInfo(alias="countryCode")]
    """Filter by canonical ISO 3166-1 alpha-2 country code.

    When supplied without `topics`, the query searches every News Terminal topic.
    """

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
