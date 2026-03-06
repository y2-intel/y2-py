# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CountryGetCountryInstabilityIndexResponse", "Data", "DataComponents", "Meta"]


class DataComponents(BaseModel):
    """Breakdown of instability components"""

    event_counts: Optional[object] = FieldInfo(alias="eventCounts", default=None)

    info: Optional[float] = None

    multiplier: Optional[float] = None

    security: Optional[float] = None

    unrest: Optional[float] = None


class Data(BaseModel):
    baseline: float
    """Baseline instability score for this country"""

    computed_at: int = FieldInfo(alias="computedAt")
    """Computation time as Unix timestamp (milliseconds)"""

    country_code: str = FieldInfo(alias="countryCode")
    """ISO alpha-2 country code"""

    country_name: str = FieldInfo(alias="countryName")
    """Country display name"""

    delta: float
    """Change from baseline"""

    value: float
    """Current instability index (0-100)"""

    components: Optional[DataComponents] = None
    """Breakdown of instability components"""

    computed_at_iso: Optional[datetime] = FieldInfo(alias="computedAtISO", default=None)
    """Computation time as ISO 8601 string"""


class Meta(BaseModel):
    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)


class CountryGetCountryInstabilityIndexResponse(BaseModel):
    data: Data

    meta: Optional[Meta] = None
