# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OsintGetGpsJammingZonesResponse", "Data", "DataCoordinates", "Meta", "MetaFilters"]


class DataCoordinates(BaseModel):
    lat: float

    lon: float


class Data(BaseModel):
    id: str
    """Zone ID"""

    coordinates: DataCoordinates

    fetched_at: int = FieldInfo(alias="fetchedAt")
    """Fetch time as Unix timestamp (milliseconds)"""

    h3_index: str = FieldInfo(alias="h3Index")
    """H3 hexagonal cell index"""

    severity: str
    """Severity classification of interference"""

    aircraft_count: Optional[int] = FieldInfo(alias="aircraftCount", default=None)
    """Number of distinct aircraft reporting"""

    fetched_at_iso: Optional[datetime] = FieldInfo(alias="fetchedAtISO", default=None)
    """Fetch time as ISO 8601 string"""

    nav_accuracy_avg: Optional[float] = FieldInfo(alias="navAccuracyAvg", default=None)
    """Average navigation accuracy category"""

    sample_count: Optional[int] = FieldInfo(alias="sampleCount", default=None)
    """Number of ADS-B samples in this cell"""


class MetaFilters(BaseModel):
    severity: Optional[str] = None


class Meta(BaseModel):
    count: Optional[int] = None

    filters: Optional[MetaFilters] = None

    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)
    """Whether more results are available beyond the current limit"""

    limit: Optional[int] = None


class OsintGetGpsJammingZonesResponse(BaseModel):
    data: List[Data]

    meta: Meta
