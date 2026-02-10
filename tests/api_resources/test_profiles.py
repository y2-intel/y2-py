# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from y2 import Y2, AsyncY2
from y2.types import (
    ProfileListResponse,
    ProfileCreateResponse,
    ProfileDeleteResponse,
    ProfileUpdateResponse,
    ProfilePartialUpdateResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Y2) -> None:
        profile = client.profiles.create(
            frequency="daily",
            name="Cybersecurity Weekly",
            schedule_time_of_day="09:00",
            topic="Cybersecurity threats, vulnerabilities, and defense strategies",
        )
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Y2) -> None:
        profile = client.profiles.create(
            frequency="daily",
            name="Cybersecurity Weekly",
            schedule_time_of_day="09:00",
            topic="Cybersecurity threats, vulnerabilities, and defense strategies",
            bluf_structure="blufStructure",
            custom_prompt="customPrompt",
            is_community=True,
            recursion_config={
                "enabled": True,
                "max_depth": 1,
                "strategy": "breadth-first",
            },
            schedule_day_of_month="1",
            schedule_day_of_week="monday",
            tags=["string"],
        )
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Y2) -> None:
        response = client.profiles.with_raw_response.create(
            frequency="daily",
            name="Cybersecurity Weekly",
            schedule_time_of_day="09:00",
            topic="Cybersecurity threats, vulnerabilities, and defense strategies",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Y2) -> None:
        with client.profiles.with_streaming_response.create(
            frequency="daily",
            name="Cybersecurity Weekly",
            schedule_time_of_day="09:00",
            topic="Cybersecurity threats, vulnerabilities, and defense strategies",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileCreateResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Y2) -> None:
        profile = client.profiles.update(
            profile_id="k57abc123def456",
        )
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Y2) -> None:
        profile = client.profiles.update(
            profile_id="k57abc123def456",
            audio_config={
                "enabled": True,
                "speed": 0,
                "voice_id": "voiceId",
            },
            bluf_structure="blufStructure",
            branding_template_id="brandingTemplateId",
            budget_config={
                "alert_threshold": 0,
                "max_cost_per_report": 0,
            },
            custom_prompt="customPrompt",
            frequency="daily",
            freshness_config={
                "enabled": True,
                "max_age_ms": 0,
                "prefer_recent_sources": True,
                "recency_weight": 0,
                "validate_links": True,
            },
            is_community=True,
            model_config={
                "max_output_tokens": 0,
                "model_id": "modelId",
                "temperature": 0,
            },
            name="name",
            recursion_config={
                "enabled": True,
                "max_depth": 1,
                "strategy": "breadth-first",
            },
            schedule_day_of_month="scheduleDayOfMonth",
            schedule_day_of_week="scheduleDayOfWeek",
            schedule_time_of_day="73:16",
            search_config={
                "exclude_domains": ["string"],
                "include_domains": ["string"],
                "max_results": 0,
                "search_depth": "basic",
                "time_range": "timeRange",
                "topic": "topic",
            },
            status="active",
            tags=["string"],
            topic="topic",
        )
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Y2) -> None:
        response = client.profiles.with_raw_response.update(
            profile_id="k57abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Y2) -> None:
        with client.profiles.with_streaming_response.update(
            profile_id="k57abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Y2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.profiles.with_raw_response.update(
                profile_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Y2) -> None:
        profile = client.profiles.list()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Y2) -> None:
        response = client.profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Y2) -> None:
        with client.profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileListResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Y2) -> None:
        profile = client.profiles.delete(
            "k57abc123def456",
        )
        assert_matches_type(ProfileDeleteResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Y2) -> None:
        response = client.profiles.with_raw_response.delete(
            "k57abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileDeleteResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Y2) -> None:
        with client.profiles.with_streaming_response.delete(
            "k57abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileDeleteResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Y2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.profiles.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_partial_update(self, client: Y2) -> None:
        profile = client.profiles.partial_update(
            profile_id="k57abc123def456",
        )
        assert_matches_type(ProfilePartialUpdateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_partial_update_with_all_params(self, client: Y2) -> None:
        profile = client.profiles.partial_update(
            profile_id="k57abc123def456",
            audio_config={
                "enabled": True,
                "speed": 0,
                "voice_id": "voiceId",
            },
            bluf_structure="blufStructure",
            branding_template_id="brandingTemplateId",
            budget_config={
                "alert_threshold": 0,
                "max_cost_per_report": 0,
            },
            custom_prompt="customPrompt",
            frequency="daily",
            freshness_config={
                "enabled": True,
                "max_age_ms": 0,
                "prefer_recent_sources": True,
                "recency_weight": 0,
                "validate_links": True,
            },
            is_community=True,
            model_config={
                "max_output_tokens": 0,
                "model_id": "modelId",
                "temperature": 0,
            },
            name="name",
            recursion_config={
                "enabled": True,
                "max_depth": 1,
                "strategy": "breadth-first",
            },
            schedule_day_of_month="scheduleDayOfMonth",
            schedule_day_of_week="scheduleDayOfWeek",
            schedule_time_of_day="73:16",
            search_config={
                "exclude_domains": ["string"],
                "include_domains": ["string"],
                "max_results": 0,
                "search_depth": "basic",
                "time_range": "timeRange",
                "topic": "topic",
            },
            status="active",
            tags=["string"],
            topic="topic",
        )
        assert_matches_type(ProfilePartialUpdateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_partial_update(self, client: Y2) -> None:
        response = client.profiles.with_raw_response.partial_update(
            profile_id="k57abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfilePartialUpdateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_partial_update(self, client: Y2) -> None:
        with client.profiles.with_streaming_response.partial_update(
            profile_id="k57abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfilePartialUpdateResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_partial_update(self, client: Y2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.profiles.with_raw_response.partial_update(
                profile_id="",
            )


class TestAsyncProfiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncY2) -> None:
        profile = await async_client.profiles.create(
            frequency="daily",
            name="Cybersecurity Weekly",
            schedule_time_of_day="09:00",
            topic="Cybersecurity threats, vulnerabilities, and defense strategies",
        )
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncY2) -> None:
        profile = await async_client.profiles.create(
            frequency="daily",
            name="Cybersecurity Weekly",
            schedule_time_of_day="09:00",
            topic="Cybersecurity threats, vulnerabilities, and defense strategies",
            bluf_structure="blufStructure",
            custom_prompt="customPrompt",
            is_community=True,
            recursion_config={
                "enabled": True,
                "max_depth": 1,
                "strategy": "breadth-first",
            },
            schedule_day_of_month="1",
            schedule_day_of_week="monday",
            tags=["string"],
        )
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncY2) -> None:
        response = await async_client.profiles.with_raw_response.create(
            frequency="daily",
            name="Cybersecurity Weekly",
            schedule_time_of_day="09:00",
            topic="Cybersecurity threats, vulnerabilities, and defense strategies",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncY2) -> None:
        async with async_client.profiles.with_streaming_response.create(
            frequency="daily",
            name="Cybersecurity Weekly",
            schedule_time_of_day="09:00",
            topic="Cybersecurity threats, vulnerabilities, and defense strategies",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileCreateResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncY2) -> None:
        profile = await async_client.profiles.update(
            profile_id="k57abc123def456",
        )
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncY2) -> None:
        profile = await async_client.profiles.update(
            profile_id="k57abc123def456",
            audio_config={
                "enabled": True,
                "speed": 0,
                "voice_id": "voiceId",
            },
            bluf_structure="blufStructure",
            branding_template_id="brandingTemplateId",
            budget_config={
                "alert_threshold": 0,
                "max_cost_per_report": 0,
            },
            custom_prompt="customPrompt",
            frequency="daily",
            freshness_config={
                "enabled": True,
                "max_age_ms": 0,
                "prefer_recent_sources": True,
                "recency_weight": 0,
                "validate_links": True,
            },
            is_community=True,
            model_config={
                "max_output_tokens": 0,
                "model_id": "modelId",
                "temperature": 0,
            },
            name="name",
            recursion_config={
                "enabled": True,
                "max_depth": 1,
                "strategy": "breadth-first",
            },
            schedule_day_of_month="scheduleDayOfMonth",
            schedule_day_of_week="scheduleDayOfWeek",
            schedule_time_of_day="73:16",
            search_config={
                "exclude_domains": ["string"],
                "include_domains": ["string"],
                "max_results": 0,
                "search_depth": "basic",
                "time_range": "timeRange",
                "topic": "topic",
            },
            status="active",
            tags=["string"],
            topic="topic",
        )
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncY2) -> None:
        response = await async_client.profiles.with_raw_response.update(
            profile_id="k57abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncY2) -> None:
        async with async_client.profiles.with_streaming_response.update(
            profile_id="k57abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncY2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.profiles.with_raw_response.update(
                profile_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncY2) -> None:
        profile = await async_client.profiles.list()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncY2) -> None:
        response = await async_client.profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncY2) -> None:
        async with async_client.profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileListResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncY2) -> None:
        profile = await async_client.profiles.delete(
            "k57abc123def456",
        )
        assert_matches_type(ProfileDeleteResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncY2) -> None:
        response = await async_client.profiles.with_raw_response.delete(
            "k57abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileDeleteResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncY2) -> None:
        async with async_client.profiles.with_streaming_response.delete(
            "k57abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileDeleteResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncY2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.profiles.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_partial_update(self, async_client: AsyncY2) -> None:
        profile = await async_client.profiles.partial_update(
            profile_id="k57abc123def456",
        )
        assert_matches_type(ProfilePartialUpdateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_partial_update_with_all_params(self, async_client: AsyncY2) -> None:
        profile = await async_client.profiles.partial_update(
            profile_id="k57abc123def456",
            audio_config={
                "enabled": True,
                "speed": 0,
                "voice_id": "voiceId",
            },
            bluf_structure="blufStructure",
            branding_template_id="brandingTemplateId",
            budget_config={
                "alert_threshold": 0,
                "max_cost_per_report": 0,
            },
            custom_prompt="customPrompt",
            frequency="daily",
            freshness_config={
                "enabled": True,
                "max_age_ms": 0,
                "prefer_recent_sources": True,
                "recency_weight": 0,
                "validate_links": True,
            },
            is_community=True,
            model_config={
                "max_output_tokens": 0,
                "model_id": "modelId",
                "temperature": 0,
            },
            name="name",
            recursion_config={
                "enabled": True,
                "max_depth": 1,
                "strategy": "breadth-first",
            },
            schedule_day_of_month="scheduleDayOfMonth",
            schedule_day_of_week="scheduleDayOfWeek",
            schedule_time_of_day="73:16",
            search_config={
                "exclude_domains": ["string"],
                "include_domains": ["string"],
                "max_results": 0,
                "search_depth": "basic",
                "time_range": "timeRange",
                "topic": "topic",
            },
            status="active",
            tags=["string"],
            topic="topic",
        )
        assert_matches_type(ProfilePartialUpdateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_partial_update(self, async_client: AsyncY2) -> None:
        response = await async_client.profiles.with_raw_response.partial_update(
            profile_id="k57abc123def456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfilePartialUpdateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_partial_update(self, async_client: AsyncY2) -> None:
        async with async_client.profiles.with_streaming_response.partial_update(
            profile_id="k57abc123def456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfilePartialUpdateResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_partial_update(self, async_client: AsyncY2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.profiles.with_raw_response.partial_update(
                profile_id="",
            )
