# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProfileListResponse", "Data", "DataProfile", "Meta"]


class DataProfile(BaseModel):
    audio_enabled: Optional[bool] = FieldInfo(alias="audioEnabled", default=None)

    bluf_structure: Optional[str] = FieldInfo(alias="blufStructure", default=None)

    branding_template_id: Optional[str] = FieldInfo(alias="brandingTemplateId", default=None)

    budget_config: Optional[object] = FieldInfo(alias="budgetConfig", default=None)

    cron_config: Optional[object] = FieldInfo(alias="cronConfig", default=None)

    custom_prompt: Optional[str] = FieldInfo(alias="customPrompt", default=None)

    frequency: Optional[str] = None

    freshness_config: Optional[object] = FieldInfo(alias="freshnessConfig", default=None)

    is_community: Optional[bool] = FieldInfo(alias="isCommunity", default=None)

    is_global: Optional[bool] = FieldInfo(alias="isGlobal", default=None)

    api_model_config: Optional[object] = FieldInfo(alias="modelConfig", default=None)

    name: Optional[str] = None

    recursion_config: Optional[object] = FieldInfo(alias="recursionConfig", default=None)

    search_config: Optional[object] = FieldInfo(alias="searchConfig", default=None)

    status: Optional[str] = None

    tags: Optional[List[str]] = None

    tool_config: Optional[object] = FieldInfo(alias="toolConfig", default=None)

    topic: Optional[str] = None


class Data(BaseModel):
    delivery_method: Literal["email", "sms", "webhook", "both_email_sms"] = FieldInfo(alias="deliveryMethod")

    is_active: bool = FieldInfo(alias="isActive")

    profile_id: str = FieldInfo(alias="profileId")

    subscribed_at: int = FieldInfo(alias="subscribedAt")

    subscription_id: str = FieldInfo(alias="subscriptionId")

    profile: Optional[DataProfile] = None


class Meta(BaseModel):
    count: Optional[int] = None


class ProfileListResponse(BaseModel):
    data: List[Data]

    meta: Meta
