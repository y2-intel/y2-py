# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import profile_create_params, profile_update_params, profile_partial_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.profile_list_response import ProfileListResponse
from ..types.profile_create_response import ProfileCreateResponse
from ..types.profile_delete_response import ProfileDeleteResponse
from ..types.profile_update_response import ProfileUpdateResponse
from ..types.profile_partial_update_response import ProfilePartialUpdateResponse

__all__ = ["ProfilesResource", "AsyncProfilesResource"]


class ProfilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/y2-intel/y2-py#accessing-raw-response-data-eg-headers
        """
        return ProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/y2-intel/y2-py#with_streaming_response
        """
        return ProfilesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        frequency: Literal["daily", "weekly", "biweekly", "monthly"],
        name: str,
        schedule_time_of_day: str,
        topic: str,
        bluf_structure: str | Omit = omit,
        custom_prompt: str | Omit = omit,
        is_community: bool | Omit = omit,
        recursion_config: profile_create_params.RecursionConfig | Omit = omit,
        schedule_day_of_month: str | Omit = omit,
        schedule_day_of_week: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileCreateResponse:
        """Creates a new intelligence profile with the specified configuration.

        The profile
        will be owned by the authenticated user and start with `active` status.

        Args:
          frequency: Report generation frequency

          name: Profile display name

          schedule_time_of_day: Time of day for report generation (HH:mm, UTC)

          topic: Topic description for research

          bluf_structure: Custom BLUF report structure template

          custom_prompt: Custom system prompt for the AI analyst

          is_community: Whether this is a community (public) profile

          schedule_day_of_month: Day of month for monthly profiles

          schedule_day_of_week: Day of week for weekly/biweekly profiles

          tags: Tags for categorization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/profiles",
            body=maybe_transform(
                {
                    "frequency": frequency,
                    "name": name,
                    "schedule_time_of_day": schedule_time_of_day,
                    "topic": topic,
                    "bluf_structure": bluf_structure,
                    "custom_prompt": custom_prompt,
                    "is_community": is_community,
                    "recursion_config": recursion_config,
                    "schedule_day_of_month": schedule_day_of_month,
                    "schedule_day_of_week": schedule_day_of_week,
                    "tags": tags,
                },
                profile_create_params.ProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileCreateResponse,
        )

    def update(
        self,
        profile_id: str,
        *,
        audio_config: profile_update_params.AudioConfig | Omit = omit,
        bluf_structure: str | Omit = omit,
        branding_template_id: str | Omit = omit,
        budget_config: profile_update_params.BudgetConfig | Omit = omit,
        custom_prompt: str | Omit = omit,
        frequency: Literal["daily", "weekly", "biweekly", "monthly"] | Omit = omit,
        freshness_config: profile_update_params.FreshnessConfig | Omit = omit,
        is_community: bool | Omit = omit,
        model_config: profile_update_params.ModelConfig | Omit = omit,
        name: str | Omit = omit,
        recursion_config: profile_update_params.RecursionConfig | Omit = omit,
        schedule_day_of_month: str | Omit = omit,
        schedule_day_of_week: str | Omit = omit,
        schedule_time_of_day: str | Omit = omit,
        search_config: profile_update_params.SearchConfig | Omit = omit,
        status: Literal["active", "paused", "cancelled"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        topic: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileUpdateResponse:
        """Replaces all mutable fields of an existing intelligence profile.

        Only profiles
        owned by the authenticated user can be updated.

        Args:
          branding_template_id: Branding template ID (Pro feature)

          frequency: Report generation frequency

          status: Profile status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._put(
            f"/profiles/{profile_id}",
            body=maybe_transform(
                {
                    "audio_config": audio_config,
                    "bluf_structure": bluf_structure,
                    "branding_template_id": branding_template_id,
                    "budget_config": budget_config,
                    "custom_prompt": custom_prompt,
                    "frequency": frequency,
                    "freshness_config": freshness_config,
                    "is_community": is_community,
                    "model_config": model_config,
                    "name": name,
                    "recursion_config": recursion_config,
                    "schedule_day_of_month": schedule_day_of_month,
                    "schedule_day_of_week": schedule_day_of_week,
                    "schedule_time_of_day": schedule_time_of_day,
                    "search_config": search_config,
                    "status": status,
                    "tags": tags,
                    "topic": topic,
                },
                profile_update_params.ProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileUpdateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileListResponse:
        """
        Returns a list of intelligence profiles the user is subscribed to, including
        subscription status and delivery preferences.
        """
        return self._get(
            "/profiles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileListResponse,
        )

    def delete(
        self,
        profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileDeleteResponse:
        """
        Permanently deletes an intelligence profile and all associated subscriptions.
        Only profiles owned by the authenticated user can be deleted. This action cannot
        be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._delete(
            f"/profiles/{profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileDeleteResponse,
        )

    def partial_update(
        self,
        profile_id: str,
        *,
        audio_config: profile_partial_update_params.AudioConfig | Omit = omit,
        bluf_structure: str | Omit = omit,
        branding_template_id: str | Omit = omit,
        budget_config: profile_partial_update_params.BudgetConfig | Omit = omit,
        custom_prompt: str | Omit = omit,
        frequency: Literal["daily", "weekly", "biweekly", "monthly"] | Omit = omit,
        freshness_config: profile_partial_update_params.FreshnessConfig | Omit = omit,
        is_community: bool | Omit = omit,
        model_config: profile_partial_update_params.ModelConfig | Omit = omit,
        name: str | Omit = omit,
        recursion_config: profile_partial_update_params.RecursionConfig | Omit = omit,
        schedule_day_of_month: str | Omit = omit,
        schedule_day_of_week: str | Omit = omit,
        schedule_time_of_day: str | Omit = omit,
        search_config: profile_partial_update_params.SearchConfig | Omit = omit,
        status: Literal["active", "paused", "cancelled"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        topic: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfilePartialUpdateResponse:
        """Partially updates an existing intelligence profile.

        Only the fields included in
        the request body will be modified; all other fields remain unchanged. Only
        profiles owned by the authenticated user can be updated.

        Args:
          branding_template_id: Branding template ID (Pro feature)

          frequency: Report generation frequency

          status: Profile status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._patch(
            f"/profiles/{profile_id}",
            body=maybe_transform(
                {
                    "audio_config": audio_config,
                    "bluf_structure": bluf_structure,
                    "branding_template_id": branding_template_id,
                    "budget_config": budget_config,
                    "custom_prompt": custom_prompt,
                    "frequency": frequency,
                    "freshness_config": freshness_config,
                    "is_community": is_community,
                    "model_config": model_config,
                    "name": name,
                    "recursion_config": recursion_config,
                    "schedule_day_of_month": schedule_day_of_month,
                    "schedule_day_of_week": schedule_day_of_week,
                    "schedule_time_of_day": schedule_time_of_day,
                    "search_config": search_config,
                    "status": status,
                    "tags": tags,
                    "topic": topic,
                },
                profile_partial_update_params.ProfilePartialUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfilePartialUpdateResponse,
        )


class AsyncProfilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/y2-intel/y2-py#accessing-raw-response-data-eg-headers
        """
        return AsyncProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/y2-intel/y2-py#with_streaming_response
        """
        return AsyncProfilesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        frequency: Literal["daily", "weekly", "biweekly", "monthly"],
        name: str,
        schedule_time_of_day: str,
        topic: str,
        bluf_structure: str | Omit = omit,
        custom_prompt: str | Omit = omit,
        is_community: bool | Omit = omit,
        recursion_config: profile_create_params.RecursionConfig | Omit = omit,
        schedule_day_of_month: str | Omit = omit,
        schedule_day_of_week: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileCreateResponse:
        """Creates a new intelligence profile with the specified configuration.

        The profile
        will be owned by the authenticated user and start with `active` status.

        Args:
          frequency: Report generation frequency

          name: Profile display name

          schedule_time_of_day: Time of day for report generation (HH:mm, UTC)

          topic: Topic description for research

          bluf_structure: Custom BLUF report structure template

          custom_prompt: Custom system prompt for the AI analyst

          is_community: Whether this is a community (public) profile

          schedule_day_of_month: Day of month for monthly profiles

          schedule_day_of_week: Day of week for weekly/biweekly profiles

          tags: Tags for categorization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/profiles",
            body=await async_maybe_transform(
                {
                    "frequency": frequency,
                    "name": name,
                    "schedule_time_of_day": schedule_time_of_day,
                    "topic": topic,
                    "bluf_structure": bluf_structure,
                    "custom_prompt": custom_prompt,
                    "is_community": is_community,
                    "recursion_config": recursion_config,
                    "schedule_day_of_month": schedule_day_of_month,
                    "schedule_day_of_week": schedule_day_of_week,
                    "tags": tags,
                },
                profile_create_params.ProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileCreateResponse,
        )

    async def update(
        self,
        profile_id: str,
        *,
        audio_config: profile_update_params.AudioConfig | Omit = omit,
        bluf_structure: str | Omit = omit,
        branding_template_id: str | Omit = omit,
        budget_config: profile_update_params.BudgetConfig | Omit = omit,
        custom_prompt: str | Omit = omit,
        frequency: Literal["daily", "weekly", "biweekly", "monthly"] | Omit = omit,
        freshness_config: profile_update_params.FreshnessConfig | Omit = omit,
        is_community: bool | Omit = omit,
        model_config: profile_update_params.ModelConfig | Omit = omit,
        name: str | Omit = omit,
        recursion_config: profile_update_params.RecursionConfig | Omit = omit,
        schedule_day_of_month: str | Omit = omit,
        schedule_day_of_week: str | Omit = omit,
        schedule_time_of_day: str | Omit = omit,
        search_config: profile_update_params.SearchConfig | Omit = omit,
        status: Literal["active", "paused", "cancelled"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        topic: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileUpdateResponse:
        """Replaces all mutable fields of an existing intelligence profile.

        Only profiles
        owned by the authenticated user can be updated.

        Args:
          branding_template_id: Branding template ID (Pro feature)

          frequency: Report generation frequency

          status: Profile status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._put(
            f"/profiles/{profile_id}",
            body=await async_maybe_transform(
                {
                    "audio_config": audio_config,
                    "bluf_structure": bluf_structure,
                    "branding_template_id": branding_template_id,
                    "budget_config": budget_config,
                    "custom_prompt": custom_prompt,
                    "frequency": frequency,
                    "freshness_config": freshness_config,
                    "is_community": is_community,
                    "model_config": model_config,
                    "name": name,
                    "recursion_config": recursion_config,
                    "schedule_day_of_month": schedule_day_of_month,
                    "schedule_day_of_week": schedule_day_of_week,
                    "schedule_time_of_day": schedule_time_of_day,
                    "search_config": search_config,
                    "status": status,
                    "tags": tags,
                    "topic": topic,
                },
                profile_update_params.ProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileUpdateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileListResponse:
        """
        Returns a list of intelligence profiles the user is subscribed to, including
        subscription status and delivery preferences.
        """
        return await self._get(
            "/profiles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileListResponse,
        )

    async def delete(
        self,
        profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileDeleteResponse:
        """
        Permanently deletes an intelligence profile and all associated subscriptions.
        Only profiles owned by the authenticated user can be deleted. This action cannot
        be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._delete(
            f"/profiles/{profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileDeleteResponse,
        )

    async def partial_update(
        self,
        profile_id: str,
        *,
        audio_config: profile_partial_update_params.AudioConfig | Omit = omit,
        bluf_structure: str | Omit = omit,
        branding_template_id: str | Omit = omit,
        budget_config: profile_partial_update_params.BudgetConfig | Omit = omit,
        custom_prompt: str | Omit = omit,
        frequency: Literal["daily", "weekly", "biweekly", "monthly"] | Omit = omit,
        freshness_config: profile_partial_update_params.FreshnessConfig | Omit = omit,
        is_community: bool | Omit = omit,
        model_config: profile_partial_update_params.ModelConfig | Omit = omit,
        name: str | Omit = omit,
        recursion_config: profile_partial_update_params.RecursionConfig | Omit = omit,
        schedule_day_of_month: str | Omit = omit,
        schedule_day_of_week: str | Omit = omit,
        schedule_time_of_day: str | Omit = omit,
        search_config: profile_partial_update_params.SearchConfig | Omit = omit,
        status: Literal["active", "paused", "cancelled"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        topic: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfilePartialUpdateResponse:
        """Partially updates an existing intelligence profile.

        Only the fields included in
        the request body will be modified; all other fields remain unchanged. Only
        profiles owned by the authenticated user can be updated.

        Args:
          branding_template_id: Branding template ID (Pro feature)

          frequency: Report generation frequency

          status: Profile status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._patch(
            f"/profiles/{profile_id}",
            body=await async_maybe_transform(
                {
                    "audio_config": audio_config,
                    "bluf_structure": bluf_structure,
                    "branding_template_id": branding_template_id,
                    "budget_config": budget_config,
                    "custom_prompt": custom_prompt,
                    "frequency": frequency,
                    "freshness_config": freshness_config,
                    "is_community": is_community,
                    "model_config": model_config,
                    "name": name,
                    "recursion_config": recursion_config,
                    "schedule_day_of_month": schedule_day_of_month,
                    "schedule_day_of_week": schedule_day_of_week,
                    "schedule_time_of_day": schedule_time_of_day,
                    "search_config": search_config,
                    "status": status,
                    "tags": tags,
                    "topic": topic,
                },
                profile_partial_update_params.ProfilePartialUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfilePartialUpdateResponse,
        )


class ProfilesResourceWithRawResponse:
    def __init__(self, profiles: ProfilesResource) -> None:
        self._profiles = profiles

        self.create = to_raw_response_wrapper(
            profiles.create,
        )
        self.update = to_raw_response_wrapper(
            profiles.update,
        )
        self.list = to_raw_response_wrapper(
            profiles.list,
        )
        self.delete = to_raw_response_wrapper(
            profiles.delete,
        )
        self.partial_update = to_raw_response_wrapper(
            profiles.partial_update,
        )


class AsyncProfilesResourceWithRawResponse:
    def __init__(self, profiles: AsyncProfilesResource) -> None:
        self._profiles = profiles

        self.create = async_to_raw_response_wrapper(
            profiles.create,
        )
        self.update = async_to_raw_response_wrapper(
            profiles.update,
        )
        self.list = async_to_raw_response_wrapper(
            profiles.list,
        )
        self.delete = async_to_raw_response_wrapper(
            profiles.delete,
        )
        self.partial_update = async_to_raw_response_wrapper(
            profiles.partial_update,
        )


class ProfilesResourceWithStreamingResponse:
    def __init__(self, profiles: ProfilesResource) -> None:
        self._profiles = profiles

        self.create = to_streamed_response_wrapper(
            profiles.create,
        )
        self.update = to_streamed_response_wrapper(
            profiles.update,
        )
        self.list = to_streamed_response_wrapper(
            profiles.list,
        )
        self.delete = to_streamed_response_wrapper(
            profiles.delete,
        )
        self.partial_update = to_streamed_response_wrapper(
            profiles.partial_update,
        )


class AsyncProfilesResourceWithStreamingResponse:
    def __init__(self, profiles: AsyncProfilesResource) -> None:
        self._profiles = profiles

        self.create = async_to_streamed_response_wrapper(
            profiles.create,
        )
        self.update = async_to_streamed_response_wrapper(
            profiles.update,
        )
        self.list = async_to_streamed_response_wrapper(
            profiles.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            profiles.delete,
        )
        self.partial_update = async_to_streamed_response_wrapper(
            profiles.partial_update,
        )
