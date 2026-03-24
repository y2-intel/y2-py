# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OsintGetMilitaryPostureResponse", "Data", "DataBreakdown", "Meta"]


class DataBreakdown(BaseModel):
    """Aircraft count by type"""

    awacs: Optional[int] = None

    bomber: Optional[int] = None

    drone: Optional[int] = None

    fighter: Optional[int] = None

    military_generic: Optional[int] = None

    recon: Optional[int] = None

    tanker: Optional[int] = None

    transport: Optional[int] = None


class Data(BaseModel):
    aircraft_count: int = FieldInfo(alias="aircraftCount")
    """Number of detected military aircraft"""

    computed_at: int = FieldInfo(alias="computedAt")
    """Assessment time as Unix timestamp (milliseconds)"""

    posture: Literal["normal", "elevated", "critical"]
    """Current military posture assessment"""

    theater: str
    """Theater name (e.g. "iran", "taiwan", "baltic")"""

    breakdown: Optional[DataBreakdown] = None
    """Aircraft count by type"""

    computed_at_iso: Optional[datetime] = FieldInfo(alias="computedAtISO", default=None)
    """Assessment time as ISO 8601 string"""


class Meta(BaseModel):
    count: Optional[int] = None

    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)
    """Whether more results are available beyond the current limit"""

    limit: Optional[int] = None


class OsintGetMilitaryPostureResponse(BaseModel):
    data: List[Data]

    meta: Meta
