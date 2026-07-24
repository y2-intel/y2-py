# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["OsintGetGpsJammingZonesParams"]


class OsintGetGpsJammingZonesParams(TypedDict, total=False):
    cursor: str
    """Opaque continuation token from the previous response.

    Bound to the original filters and ordering.
    """

    format: Literal["json", "ndjson", "geojson"]
    """
    Select the JSON resource envelope, row-oriented NDJSON, or an RFC 7946
    FeatureCollection.
    """

    limit: int
    """Maximum number of zones to return"""

    severity: Literal["low", "moderate", "severe", "critical"]
    """Filter by interference severity"""
