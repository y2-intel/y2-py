# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ProfileCreateParams", "RecursionConfig"]


class ProfileCreateParams(TypedDict, total=False):
    frequency: Required[Literal["daily", "weekly", "biweekly", "monthly"]]
    """Report generation frequency"""

    name: Required[str]
    """Profile display name"""

    schedule_time_of_day: Required[Annotated[str, PropertyInfo(alias="scheduleTimeOfDay")]]
    """Time of day for report generation (HH:mm, UTC)"""

    topic: Required[str]
    """Topic description for research"""

    bluf_structure: Annotated[str, PropertyInfo(alias="blufStructure")]
    """Custom BLUF report structure template"""

    custom_prompt: Annotated[str, PropertyInfo(alias="customPrompt")]
    """Custom system prompt for the AI analyst"""

    is_community: Annotated[bool, PropertyInfo(alias="isCommunity")]
    """Whether this is a community (public) profile"""

    recursion_config: Annotated[RecursionConfig, PropertyInfo(alias="recursionConfig")]

    schedule_day_of_month: Annotated[str, PropertyInfo(alias="scheduleDayOfMonth")]
    """Day of month for monthly profiles"""

    schedule_day_of_week: Annotated[str, PropertyInfo(alias="scheduleDayOfWeek")]
    """Day of week for weekly/biweekly profiles"""

    tags: SequenceNotStr[str]
    """Tags for categorization"""


class RecursionConfig(TypedDict, total=False):
    enabled: Required[bool]

    max_depth: Required[Annotated[int, PropertyInfo(alias="maxDepth")]]

    strategy: Required[Literal["breadth-first", "depth-first", "hybrid"]]
