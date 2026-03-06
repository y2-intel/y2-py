# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OsintListAircraftResponse", "Data", "DataCoordinates", "Meta", "MetaFilters"]


class DataCoordinates(BaseModel):
    lat: float

    lon: float


class Data(BaseModel):
    id: str
    """Track ID"""

    callsign: str
    """Aircraft callsign"""

    coordinates: DataCoordinates

    icao24: str
    """ICAO 24-bit transponder address"""

    last_seen_at: int = FieldInfo(alias="lastSeenAt")
    """Last seen time as Unix timestamp (milliseconds)"""

    theater: str
    """Theater assignment"""

    aircraft_type: Optional[str] = FieldInfo(alias="aircraftType", default=None)
    """Classified aircraft type (tanker, awacs, fighter, recon, etc.)"""

    altitude: Optional[float] = None
    """Altitude in meters"""

    confidence: Optional[float] = None
    """Classification confidence score"""

    heading: Optional[float] = None
    """Heading in degrees"""

    is_interesting: Optional[bool] = FieldInfo(alias="isInteresting", default=None)
    """Whether flagged as operationally interesting"""

    last_seen_at_iso: Optional[datetime] = FieldInfo(alias="lastSeenAtISO", default=None)
    """Last seen time as ISO 8601 string"""

    operator: Optional[str] = None
    """Operating entity"""

    speed: Optional[float] = None
    """Ground speed in m/s"""


class MetaFilters(BaseModel):
    theater: Optional[str] = None


class Meta(BaseModel):
    count: Optional[int] = None

    filters: Optional[MetaFilters] = None

    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)
    """Whether more results are available beyond the current limit"""

    limit: Optional[int] = None


class OsintListAircraftResponse(BaseModel):
    data: List[Data]

    meta: Meta
