# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "ProfileUpdateParams",
    "AudioConfig",
    "BudgetConfig",
    "FreshnessConfig",
    "ModelConfig",
    "RecursionConfig",
    "SearchConfig",
]


class ProfileUpdateParams(TypedDict, total=False):
    audio_config: Annotated[AudioConfig, PropertyInfo(alias="audioConfig")]

    bluf_structure: Annotated[str, PropertyInfo(alias="blufStructure")]

    branding_template_id: Annotated[str, PropertyInfo(alias="brandingTemplateId")]
    """Branding template ID (Pro feature)"""

    budget_config: Annotated[BudgetConfig, PropertyInfo(alias="budgetConfig")]

    custom_prompt: Annotated[str, PropertyInfo(alias="customPrompt")]

    frequency: Literal["daily", "weekly", "biweekly", "monthly"]
    """Report generation frequency"""

    freshness_config: Annotated[FreshnessConfig, PropertyInfo(alias="freshnessConfig")]

    is_community: Annotated[bool, PropertyInfo(alias="isCommunity")]

    model_config: Annotated[ModelConfig, PropertyInfo(alias="modelConfig")]

    name: str

    recursion_config: Annotated[RecursionConfig, PropertyInfo(alias="recursionConfig")]

    schedule_day_of_month: Annotated[str, PropertyInfo(alias="scheduleDayOfMonth")]

    schedule_day_of_week: Annotated[str, PropertyInfo(alias="scheduleDayOfWeek")]

    schedule_time_of_day: Annotated[str, PropertyInfo(alias="scheduleTimeOfDay")]

    search_config: Annotated[SearchConfig, PropertyInfo(alias="searchConfig")]

    status: Literal["active", "paused", "cancelled"]
    """Profile status"""

    tags: SequenceNotStr[str]

    topic: str


class AudioConfig(TypedDict, total=False):
    enabled: bool

    speed: float

    voice_id: Annotated[str, PropertyInfo(alias="voiceId")]


class BudgetConfig(TypedDict, total=False):
    alert_threshold: Annotated[float, PropertyInfo(alias="alertThreshold")]

    max_cost_per_report: Annotated[float, PropertyInfo(alias="maxCostPerReport")]


class FreshnessConfig(TypedDict, total=False):
    enabled: bool

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]

    prefer_recent_sources: Annotated[bool, PropertyInfo(alias="preferRecentSources")]

    recency_weight: Annotated[float, PropertyInfo(alias="recencyWeight")]

    validate_links: Annotated[bool, PropertyInfo(alias="validateLinks")]


class ModelConfig(TypedDict, total=False):
    max_output_tokens: Annotated[int, PropertyInfo(alias="maxOutputTokens")]

    model_id: Annotated[str, PropertyInfo(alias="modelId")]

    temperature: float


class RecursionConfig(TypedDict, total=False):
    enabled: Required[bool]

    max_depth: Required[Annotated[int, PropertyInfo(alias="maxDepth")]]

    strategy: Required[Literal["breadth-first", "depth-first", "hybrid"]]


class SearchConfig(TypedDict, total=False):
    exclude_domains: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludeDomains")]

    include_domains: Annotated[SequenceNotStr[str], PropertyInfo(alias="includeDomains")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]

    search_depth: Annotated[Literal["basic", "advanced"], PropertyInfo(alias="searchDepth")]

    time_range: Annotated[str, PropertyInfo(alias="timeRange")]

    topic: str
