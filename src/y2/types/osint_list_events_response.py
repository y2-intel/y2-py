# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "OsintListEventsResponse",
    "Data",
    "DataCoordinates",
    "DataProvenance",
    "DataProvenanceEntity",
    "Meta",
    "MetaFilters",
]


class DataCoordinates(BaseModel):
    """Geographic coordinates (null if unavailable)"""

    lat: Optional[float] = None
    """Latitude"""

    lon: Optional[float] = None
    """Longitude"""


class DataProvenanceEntity(BaseModel):
    kind: Literal[
        "person",
        "organization",
        "country",
        "region",
        "vessel",
        "aircraft",
        "facility",
        "asset",
        "indicator",
        "cve",
        "malware_family",
        "threat_actor",
        "vendor",
        "software",
        "ai_model",
        "api_service",
        "protocol",
    ]
    """Entity type"""

    name: str
    """Entity name"""


class DataProvenance(BaseModel):
    """Extraction provenance metadata.

    Populated only when
    `sourceType === "y2_report"`; null for all other sources.
    Returned by `/osint/regional`.
    """

    source: Literal["y2_report"]
    """Source identifier (always "y2_report")"""

    classification: Optional[Literal["ongoing", "past", "forecast", "analysis"]] = None
    """Event temporal classification from GroundSource methodology"""

    confidence: Optional[float] = None
    """Extraction confidence score (0.5-1.0)"""

    entities: Optional[List[DataProvenanceEntity]] = None
    """Named entities extracted from the report"""


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

    event_time: int = FieldInfo(alias="eventTime")
    """Event time as Unix timestamp (milliseconds)"""

    severity: Literal["low", "medium", "high", "critical"]
    """Event severity level"""

    source_id: str = FieldInfo(alias="sourceId")
    """Source-specific event identifier"""

    source_type: str = FieldInfo(alias="sourceType")
    """Data source type"""

    title: str
    """Event title/headline"""

    coordinates: Optional[DataCoordinates] = None
    """Geographic coordinates (null if unavailable)"""

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)
    """ISO alpha-2 country code"""

    description: Optional[str] = None
    """Detailed event description"""

    event_time_iso: Optional[datetime] = FieldInfo(alias="eventTimeISO", default=None)
    """Event time as ISO 8601 string"""

    fetched_at: Optional[int] = FieldInfo(alias="fetchedAt", default=None)
    """Data fetch time as Unix timestamp (milliseconds), null if unavailable"""

    fetched_at_iso: Optional[datetime] = FieldInfo(alias="fetchedAtISO", default=None)
    """Data fetch time as ISO 8601 string, null if unavailable"""

    location_name: Optional[str] = FieldInfo(alias="locationName", default=None)
    """Human-readable location name"""

    provenance: Optional[DataProvenance] = None
    """Extraction provenance metadata.

    Populated only when `sourceType === "y2_report"`; null for all other sources.
    Returned by `/osint/regional`.
    """

    region: Optional[Literal["mena", "africa", "latam", "asiapac", "europe", "namerica"]] = None
    """Geographic region identifier"""

    url: Optional[str] = None
    """Source URL for the event"""


class MetaFilters(BaseModel):
    category: Optional[str] = None

    severity: Optional[str] = None


class Meta(BaseModel):
    count: Optional[int] = None

    filters: Optional[MetaFilters] = None

    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)
    """Whether more results are available beyond the current limit"""

    limit: Optional[int] = None


class OsintListEventsResponse(BaseModel):
    data: List[Data]

    meta: Meta
