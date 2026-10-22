# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CountryGetCountryNewsResponse", "Data", "DataCoordinates", "DataGeometry", "DataProvenance", "Meta"]


class DataCoordinates(BaseModel):
    lat: Optional[float] = None

    lon: Optional[float] = None


class DataGeometry(BaseModel):
    """WGS 84 point with longitude first, then latitude."""

    coordinates: List[object]

    type: Literal["Point"]


class DataProvenance(BaseModel):
    country_code_basis: Literal["resolved_geography", "indexed_observation"] = FieldInfo(alias="countryCodeBasis")

    geo_resolution: Optional[Dict[str, object]] = FieldInfo(alias="geoResolution", default=None)
    """Resolver method, confidence, version, and chokepoint context when available."""


class Data(BaseModel):
    id: str
    """News item ID"""

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
    """OSINT event category classification"""

    country_code: str = FieldInfo(alias="countryCode")
    """Canonical ISO 3166-1 alpha-2 country code used by the indexed query."""

    event_time: int = FieldInfo(alias="eventTime")
    """Event time as Unix timestamp (milliseconds)"""

    severity: Literal["low", "medium", "high", "critical"]
    """Event severity level"""

    source_type: str = FieldInfo(alias="sourceType")
    """Data source type"""

    title: str
    """News headline"""

    coordinates: Optional[DataCoordinates] = None

    description: Optional[str] = None
    """News description/summary"""

    event_time_iso: Optional[datetime] = FieldInfo(alias="eventTimeISO", default=None)

    fetched_at: Optional[int] = FieldInfo(alias="fetchedAt", default=None)

    fetched_at_iso: Optional[datetime] = FieldInfo(alias="fetchedAtISO", default=None)

    geometry: Optional[DataGeometry] = None
    """WGS 84 point with longitude first, then latitude."""

    location_name: Optional[str] = FieldInfo(alias="locationName", default=None)
    """Most specific resolved sovereign location, when known."""

    observed_at: Optional[datetime] = FieldInfo(alias="observedAt", default=None)

    occurred_at: Optional[datetime] = FieldInfo(alias="occurredAt", default=None)

    provenance: Optional[DataProvenance] = None

    region: Optional[str] = None
    """Normalized OSINT region, when known."""

    url: Optional[str] = None
    """Source URL"""


class Meta(BaseModel):
    count: Optional[int] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)
    """Whether more results are available beyond the current limit"""

    limit: Optional[int] = None


class CountryGetCountryNewsResponse(BaseModel):
    data: List[Data]

    meta: Meta
