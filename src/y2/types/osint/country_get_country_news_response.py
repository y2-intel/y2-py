# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CountryGetCountryNewsResponse", "Data", "Meta"]


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

    event_time: int = FieldInfo(alias="eventTime")
    """Event time as Unix timestamp (milliseconds)"""

    severity: Literal["low", "medium", "high", "critical"]
    """Event severity level"""

    title: str
    """News headline"""

    description: Optional[str] = None
    """News description/summary"""

    source_type: Optional[str] = FieldInfo(alias="sourceType", default=None)
    """Data source type"""

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
