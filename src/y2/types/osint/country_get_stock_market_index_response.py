# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CountryGetStockMarketIndexResponse", "Data"]


class Data(BaseModel):
    currency: str
    """Currency code"""

    fetched_at: int = FieldInfo(alias="fetchedAt")
    """Data fetch time as Unix timestamp (milliseconds)"""

    index_name: str = FieldInfo(alias="indexName")
    """Human-readable index name"""

    ticker: str
    """Stock index ticker symbol"""

    weekly_change: float = FieldInfo(alias="weeklyChange")
    """Weekly change percentage"""

    current_price: Optional[float] = FieldInfo(alias="currentPrice", default=None)
    """Current index price/value"""

    fetched_at_iso: Optional[datetime] = FieldInfo(alias="fetchedAtISO", default=None)
    """Data fetch time as ISO 8601 string"""


class CountryGetStockMarketIndexResponse(BaseModel):
    data: Data
