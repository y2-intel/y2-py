# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OsintListVesselsResponse", "Data", "DataCoordinates", "Meta", "MetaFilters"]


class DataCoordinates(BaseModel):
    lat: float

    lon: float


class Data(BaseModel):
    id: str
    """Vessel ID"""

    coordinates: DataCoordinates

    name: str
    """Vessel name"""

    vessel_type: str = FieldInfo(alias="vesselType")
    """Vessel type classification"""

    confidence: Optional[float] = None
    """Position confidence"""

    fetched_at: Optional[int] = FieldInfo(alias="fetchedAt", default=None)
    """Fetch time as Unix timestamp (milliseconds)"""

    fetched_at_iso: Optional[datetime] = FieldInfo(alias="fetchedAtISO", default=None)
    """Fetch time as ISO 8601 string"""

    hull_number: Optional[str] = FieldInfo(alias="hullNumber", default=None)
    """Hull number designation"""

    operator: Optional[str] = None
    """Operating navy"""

    region: Optional[str] = None
    """Deployment region"""

    source: Optional[str] = None
    """Data source"""

    status: Optional[str] = None
    """Current operational status"""

    strike_group: Optional[str] = FieldInfo(alias="strikeGroup", default=None)
    """Strike group assignment"""


class MetaFilters(BaseModel):
    region: Optional[str] = None


class Meta(BaseModel):
    count: Optional[int] = None

    filters: Optional[MetaFilters] = None

    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)
    """Whether more results are available beyond the current limit"""

    limit: Optional[int] = None


class OsintListVesselsResponse(BaseModel):
    data: List[Data]

    meta: Meta
