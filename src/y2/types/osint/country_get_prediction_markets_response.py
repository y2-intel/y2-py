# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CountryGetPredictionMarketsResponse", "Data", "Meta"]


class Data(BaseModel):
    market_id: str = FieldInfo(alias="marketId")
    """Prediction market identifier"""

    probability: float
    """Current probability (0-1)"""

    title: str
    """Market question/title"""

    end_date: Optional[datetime] = FieldInfo(alias="endDate", default=None)
    """Market resolution date"""

    liquidity: Optional[float] = None
    """Market liquidity (null if unavailable)"""

    outcome_prices: Optional[List[str]] = FieldInfo(alias="outcomePrices", default=None)
    """Outcome prices corresponding to each outcome (null if unavailable)"""

    outcomes: Optional[List[str]] = None
    """Possible market outcomes"""

    polymarket_url: Optional[str] = FieldInfo(alias="polymarketUrl", default=None)
    """Polymarket URL for this market"""

    slug: Optional[str] = None
    """URL-friendly market slug (null if unavailable)"""

    volume: Optional[float] = None
    """Trading volume"""


class Meta(BaseModel):
    count: Optional[int] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)
    """Whether more results are available beyond the current limit"""

    limit: Optional[int] = None


class CountryGetPredictionMarketsResponse(BaseModel):
    data: List[Data]

    meta: Meta
