# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "CountryGetPredictionMarketsResponse",
    "Data",
    "DataOutcome",
    "DataLiquidityMeasurement",
    "DataVolumeMeasurement",
    "Meta",
]


class DataOutcome(BaseModel):
    label: str

    probability: float


class DataLiquidityMeasurement(BaseModel):
    basis: Literal["provider_reported"]

    currency: Optional[str] = None
    """ISO 4217 code when the source identifies one; otherwise null."""

    value: Optional[float] = None


class DataVolumeMeasurement(BaseModel):
    basis: Literal["provider_reported"]

    currency: Optional[str] = None
    """ISO 4217 code when the source identifies one; otherwise null."""

    value: Optional[float] = None


class Data(BaseModel):
    """
    Polymarket-only prediction market shape returned by
    `/osint/countries/{countryCode}/predictions`. The unified
    Polymarket+Kalshi shape returned by `/osint/prediction-markets`
    is documented separately as `PredictionMarket`.
    """

    id: str

    market_id: str = FieldInfo(alias="marketId")
    """Prediction market identifier"""

    outcomes: List[DataOutcome]
    """Typed outcome labels with normalized fractional probabilities."""

    probability: float
    """Current probability (0-1)"""

    probability_basis: Literal["fraction_0_to_1"] = FieldInfo(alias="probabilityBasis")

    title: str
    """Market question/title"""

    type: Literal["prediction_market"]

    end_date: Optional[datetime] = FieldInfo(alias="endDate", default=None)
    """Market resolution date"""

    liquidity: Optional[float] = None
    """Market liquidity (null if unavailable)"""

    liquidity_measurement: Optional[DataLiquidityMeasurement] = FieldInfo(alias="liquidityMeasurement", default=None)

    polymarket_url: Optional[str] = FieldInfo(alias="polymarketUrl", default=None)
    """Polymarket URL for this market"""

    slug: Optional[str] = None
    """URL-friendly market slug (null if unavailable)"""

    volume: Optional[float] = None
    """Trading volume"""

    volume_measurement: Optional[DataVolumeMeasurement] = FieldInfo(alias="volumeMeasurement", default=None)


class Meta(BaseModel):
    count: Optional[int] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)
    """Whether more results are available beyond the current limit"""

    limit: Optional[int] = None


class CountryGetPredictionMarketsResponse(BaseModel):
    """
    Response wrapper for `/osint/countries/{countryCode}/predictions`.
    See `PredictionMarketListResponse` for the unified
    Polymarket+Kalshi response wrapper used by `/osint/prediction-markets`.
    """

    data: List[Data]

    meta: Meta
