# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SourceGetDataSourceHealthResponse", "Data", "Meta"]


class Data(BaseModel):
    failure_count: int = FieldInfo(alias="failureCount")
    """Number of consecutive failures"""

    source_type: str = FieldInfo(alias="sourceType")
    """Data source identifier"""

    state: Literal["closed", "open", "half_open"]
    """Circuit breaker state"""

    last_error: Optional[str] = FieldInfo(alias="lastError", default=None)
    """Most recent error message"""

    last_failure_at: Optional[int] = FieldInfo(alias="lastFailureAt", default=None)
    """Last failure time (milliseconds)"""

    last_failure_at_iso: Optional[datetime] = FieldInfo(alias="lastFailureAtISO", default=None)
    """Last failure time as ISO 8601 string"""

    last_success_at: Optional[int] = FieldInfo(alias="lastSuccessAt", default=None)
    """Last successful fetch time (milliseconds)"""

    last_success_at_iso: Optional[datetime] = FieldInfo(alias="lastSuccessAtISO", default=None)
    """Last successful fetch time as ISO 8601 string"""


class Meta(BaseModel):
    count: Optional[int] = None


class SourceGetDataSourceHealthResponse(BaseModel):
    data: List[Data]

    meta: Meta
