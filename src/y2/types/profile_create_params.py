# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "ProfileCreateParams",
    "AudioConfig",
    "BudgetConfig",
    "FreshnessConfig",
    "ModelConfig",
    "RecursionConfig",
    "SearchConfig",
]


class ProfileCreateParams(TypedDict, total=False):
    frequency: Required[Literal["daily", "weekly", "biweekly", "monthly"]]
    """Report generation frequency"""

    name: Required[str]
    """Profile display name"""

    schedule_time_of_day: Required[Annotated[str, PropertyInfo(alias="scheduleTimeOfDay")]]
    """Time of day for report generation (HH:mm, UTC)"""

    topic: Required[str]
    """Topic description for research"""

    audio_config: Annotated[AudioConfig, PropertyInfo(alias="audioConfig")]
    """Audio generation configuration"""

    bluf_structure: Annotated[str, PropertyInfo(alias="blufStructure")]
    """Custom BLUF report structure template"""

    branding_template_id: Annotated[str, PropertyInfo(alias="brandingTemplateId")]
    """Branding template ID (Pro feature)"""

    budget_config: Annotated[BudgetConfig, PropertyInfo(alias="budgetConfig")]
    """Cost budget configuration"""

    custom_prompt: Annotated[str, PropertyInfo(alias="customPrompt")]
    """Custom system prompt for the AI analyst"""

    freshness_config: Annotated[FreshnessConfig, PropertyInfo(alias="freshnessConfig")]
    """Source freshness configuration"""

    is_community: Annotated[bool, PropertyInfo(alias="isCommunity")]
    """Whether this is a community (public) profile"""

    model_config: Annotated[ModelConfig, PropertyInfo(alias="modelConfig")]
    """AI model configuration"""

    recursion_config: Annotated[RecursionConfig, PropertyInfo(alias="recursionConfig")]

    schedule_day_of_month: Annotated[str, PropertyInfo(alias="scheduleDayOfMonth")]
    """Day of month for monthly profiles"""

    schedule_day_of_week: Annotated[str, PropertyInfo(alias="scheduleDayOfWeek")]
    """Day of week for weekly/biweekly profiles"""

    search_config: Annotated[SearchConfig, PropertyInfo(alias="searchConfig")]
    """Web search configuration"""

    tags: SequenceNotStr[str]
    """Tags for categorization"""

    tool_config: Annotated[object, PropertyInfo(alias="toolConfig")]
    """Tool configuration for report generation"""


class AudioConfig(TypedDict, total=False):
    """Audio generation configuration"""

    enabled: bool

    speed: float

    voice_id: Annotated[str, PropertyInfo(alias="voiceId")]


class BudgetConfig(TypedDict, total=False):
    """Cost budget configuration"""

    alert_threshold: Annotated[float, PropertyInfo(alias="alertThreshold")]

    max_cost_per_report: Annotated[float, PropertyInfo(alias="maxCostPerReport")]


class FreshnessConfig(TypedDict, total=False):
    """Source freshness configuration"""

    enabled: bool

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]

    prefer_recent_sources: Annotated[bool, PropertyInfo(alias="preferRecentSources")]

    recency_weight: Annotated[float, PropertyInfo(alias="recencyWeight")]

    validate_links: Annotated[bool, PropertyInfo(alias="validateLinks")]


class ModelConfig(TypedDict, total=False):
    """AI model configuration"""

    max_output_tokens: Annotated[int, PropertyInfo(alias="maxOutputTokens")]

    model_id: Annotated[str, PropertyInfo(alias="modelId")]

    temperature: float


class RecursionConfig(TypedDict, total=False):
    enabled: Required[bool]

    max_depth: Required[Annotated[int, PropertyInfo(alias="maxDepth")]]

    strategy: Required[Literal["breadth-first", "depth-first", "hybrid"]]


class SearchConfig(TypedDict, total=False):
    """Web search configuration"""

    exclude_domains: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludeDomains")]

    include_domains: Annotated[SequenceNotStr[str], PropertyInfo(alias="includeDomains")]

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]

    search_depth: Annotated[Literal["basic", "advanced"], PropertyInfo(alias="searchDepth")]

    time_range: Annotated[str, PropertyInfo(alias="timeRange")]

    topic: str
