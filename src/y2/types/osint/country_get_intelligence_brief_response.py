# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CountryGetIntelligenceBriefResponse", "Data"]


class Data(BaseModel):
    brief_text: str = FieldInfo(alias="briefText")
    """AI-generated intelligence brief text"""

    generated_at: int = FieldInfo(alias="generatedAt")
    """Generation time as Unix timestamp (milliseconds)"""

    model: str
    """LLM model used for generation"""


class CountryGetIntelligenceBriefResponse(BaseModel):
    data: Data
