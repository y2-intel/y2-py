# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CountryGetIntelligenceBriefResponse", "Data"]


class Data(BaseModel):
    brief_text: str = FieldInfo(alias="briefText")
    """AI-generated intelligence brief text"""

    generated_at: int = FieldInfo(alias="generatedAt")
    """Generation time as Unix timestamp (milliseconds)"""

    generated_at_iso: datetime = FieldInfo(alias="generatedAtISO")

    published_at: datetime = FieldInfo(alias="publishedAt")


class CountryGetIntelligenceBriefResponse(BaseModel):
    data: Data
