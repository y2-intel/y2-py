# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OsintMapEventsResponse", "Data", "DataCoordinates", "Meta", "MetaFilters"]


class DataCoordinates(BaseModel):
    """
    Geographic coordinates (always present — events without coordinates are excluded)
    """

    lat: float
    """Latitude"""

    lon: float
    """Longitude"""


class Data(BaseModel):
    id: str
    """Event ID"""

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

    coordinates: DataCoordinates
    """
    Geographic coordinates (always present — events without coordinates are
    excluded)
    """

    event_time: int = FieldInfo(alias="eventTime")
    """Event time as Unix timestamp (milliseconds)"""

    severity: Literal["low", "medium", "high", "critical"]
    """Event severity level"""

    title: str
    """Event title/headline"""

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)
    """ISO alpha-2 country code"""

    description: Optional[str] = None
    """Detailed event description"""

    event_time_iso: Optional[datetime] = FieldInfo(alias="eventTimeISO", default=None)
    """Event time as ISO 8601 string"""

    location_name: Optional[str] = FieldInfo(alias="locationName", default=None)
    """Human-readable location name"""

    region: Optional[Literal["mena", "africa", "latam", "asiapac", "europe", "namerica"]] = None
    """Geographic region identifier"""

    source_type: Optional[str] = FieldInfo(alias="sourceType", default=None)
    """Data source type"""

    url: Optional[str] = None
    """Source URL for the event"""


class MetaFilters(BaseModel):
    region: Optional[str] = None


class Meta(BaseModel):
    count: Optional[int] = None

    filters: Optional[MetaFilters] = None

    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)
    """Whether more results are available beyond the current limit"""

    limit: Optional[int] = None


class OsintMapEventsResponse(BaseModel):
    data: List[Data]

    meta: Meta
