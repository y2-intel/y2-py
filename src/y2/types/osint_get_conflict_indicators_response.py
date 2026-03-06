# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OsintGetConflictIndicatorsResponse", "Data", "Meta", "MetaFilters"]


class Data(BaseModel):
    id: str
    """CII item ID"""

    category: str
    """Conflict indicator category"""

    computed_at: int = FieldInfo(alias="computedAt")
    """Computation time as Unix timestamp (milliseconds)"""

    delta: float
    """Recent change in value"""

    value: float
    """Conflict indicator value (0-100)"""

    components: Optional[Dict[str, object]] = None
    """Breakdown of indicator components"""

    computed_at_iso: Optional[datetime] = FieldInfo(alias="computedAtISO", default=None)
    """Computation time as ISO 8601 string"""

    region: Optional[Literal["mena", "africa", "latam", "asiapac", "europe", "namerica"]] = None
    """Geographic region identifier"""


class MetaFilters(BaseModel):
    category: Optional[str] = None

    region: Optional[str] = None


class Meta(BaseModel):
    count: Optional[int] = None

    filters: Optional[MetaFilters] = None

    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)
    """Whether more results are available beyond the current limit"""

    limit: Optional[int] = None


class OsintGetConflictIndicatorsResponse(BaseModel):
    data: List[Data]

    meta: Meta
