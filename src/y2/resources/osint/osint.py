# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import (
    osint_map_events_params,
    osint_list_events_params,
    osint_list_vessels_params,
    osint_list_aircraft_params,
    osint_get_military_posture_params,
    osint_get_gps_jamming_zones_params,
    osint_get_conflict_indicators_params,
)
from .sources import (
    SourcesResource,
    AsyncSourcesResource,
    SourcesResourceWithRawResponse,
    AsyncSourcesResourceWithRawResponse,
    SourcesResourceWithStreamingResponse,
    AsyncSourcesResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .countries import (
    CountriesResource,
    AsyncCountriesResource,
    CountriesResourceWithRawResponse,
    AsyncCountriesResourceWithRawResponse,
    CountriesResourceWithStreamingResponse,
    AsyncCountriesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.osint_map_events_response import OsintMapEventsResponse
from ...types.osint_list_events_response import OsintListEventsResponse
from ...types.osint_list_vessels_response import OsintListVesselsResponse
from ...types.osint_list_aircraft_response import OsintListAircraftResponse
from ...types.osint_get_military_posture_response import OsintGetMilitaryPostureResponse
from ...types.osint_get_gps_jamming_zones_response import OsintGetGpsJammingZonesResponse
from ...types.osint_get_conflict_indicators_response import OsintGetConflictIndicatorsResponse

__all__ = ["OsintResource", "AsyncOsintResource"]


class OsintResource(SyncAPIResource):
    """Situation Room OSINT intelligence operations"""

    @cached_property
    def countries(self) -> CountriesResource:
        """Situation Room OSINT intelligence operations"""
        return CountriesResource(self._client)

    @cached_property
    def sources(self) -> SourcesResource:
        """Situation Room OSINT intelligence operations"""
        return SourcesResource(self._client)

    @cached_property
    def with_raw_response(self) -> OsintResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/y2-intel/y2-py#accessing-raw-response-data-eg-headers
        """
        return OsintResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OsintResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/y2-intel/y2-py#with_streaming_response
        """
        return OsintResourceWithStreamingResponse(self)

    def get_conflict_indicators(
        self,
        *,
        category: Literal[
            "seismic",
            "conflict",
            "political",
            "economic",
            "weather",
            "health",
            "cyber",
            "maritime",
            "fire",
            "aviation",
            "other",
        ]
        | Omit = omit,
        limit: int | Omit = omit,
        region: Literal["mena", "africa", "latam", "asiapac", "europe", "namerica"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OsintGetConflictIndicatorsResponse:
        """Returns the Conflict Indicators Index (CII) values.

        Each item represents a
        conflict indicator with a score from 0-100 and a delta showing recent change.
        Supports filtering by region and category.

        Args:
          category: Filter by event category

          limit: Maximum number of items to return

          region: Filter by geographic region

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/osint/cii",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "limit": limit,
                        "region": region,
                    },
                    osint_get_conflict_indicators_params.OsintGetConflictIndicatorsParams,
                ),
            ),
            cast_to=OsintGetConflictIndicatorsResponse,
        )

    def get_gps_jamming_zones(
        self,
        *,
        limit: int | Omit = omit,
        severity: Literal["low", "moderate", "severe", "critical"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OsintGetGpsJammingZonesResponse:
        """
        Returns GPS interference zones detected via ADS-B navigation accuracy
        degradation analysis, aggregated into H3 hex cells.

        Args:
          limit: Maximum number of zones to return

          severity: Filter by interference severity

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/osint/gps-jamming",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "severity": severity,
                    },
                    osint_get_gps_jamming_zones_params.OsintGetGpsJammingZonesParams,
                ),
            ),
            cast_to=OsintGetGpsJammingZonesResponse,
        )

    def get_military_posture(
        self,
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OsintGetMilitaryPostureResponse:
        """
        Returns military posture assessments for monitored theaters, based on detected
        military aircraft activity from the OpenSky Network. Each theater has a posture
        level (normal, elevated, critical) and aircraft breakdown by type.

        Args:
          limit: Maximum number of items to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/osint/military-posture",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"limit": limit}, osint_get_military_posture_params.OsintGetMilitaryPostureParams
                ),
            ),
            cast_to=OsintGetMilitaryPostureResponse,
        )

    def list_aircraft(
        self,
        *,
        limit: int | Omit = omit,
        theater: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OsintListAircraftResponse:
        """
        Returns tracked military aircraft positions from the OpenSky Network, filtered
        and classified by type (tanker, AWACS, fighter, etc.).

        Args:
          limit: Maximum number of aircraft to return

          theater: Filter by theater ID (e.g. "iran", "taiwan", "baltic")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/osint/aircraft",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "theater": theater,
                    },
                    osint_list_aircraft_params.OsintListAircraftParams,
                ),
            ),
            cast_to=OsintListAircraftResponse,
        )

    def list_events(
        self,
        *,
        category: Literal[
            "seismic",
            "conflict",
            "political",
            "economic",
            "weather",
            "health",
            "cyber",
            "maritime",
            "fire",
            "aviation",
            "other",
        ]
        | Omit = omit,
        limit: int | Omit = omit,
        severity: Literal["low", "medium", "high", "critical"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OsintListEventsResponse:
        """Returns OSINT threat events from the Situation Room.

        Supports filtering by
        category, severity, region, and country.

        Args:
          category: Filter by event category

          limit: Maximum number of events to return

          severity: Filter by severity level

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/osint/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "limit": limit,
                        "severity": severity,
                    },
                    osint_list_events_params.OsintListEventsParams,
                ),
            ),
            cast_to=OsintListEventsResponse,
        )

    def list_vessels(
        self,
        *,
        limit: int | Omit = omit,
        region: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OsintListVesselsResponse:
        """
        Returns naval vessel positions sourced from USNI fleet tracker data, including
        carrier strike groups and individual warships.

        Args:
          limit: Maximum number of vessels to return

          region: Filter by region name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/osint/vessels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "region": region,
                    },
                    osint_list_vessels_params.OsintListVesselsParams,
                ),
            ),
            cast_to=OsintListVesselsResponse,
        )

    def map_events(
        self,
        *,
        limit: int | Omit = omit,
        region: Literal["mena", "africa", "latam", "asiapac", "europe", "namerica"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OsintMapEventsResponse:
        """Returns OSINT events with geographic coordinates for map display.

        Events without
        coordinates are excluded.

        Args:
          limit: Maximum number of events to return

          region: Filter by geographic region

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/osint/map",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "region": region,
                    },
                    osint_map_events_params.OsintMapEventsParams,
                ),
            ),
            cast_to=OsintMapEventsResponse,
        )


class AsyncOsintResource(AsyncAPIResource):
    """Situation Room OSINT intelligence operations"""

    @cached_property
    def countries(self) -> AsyncCountriesResource:
        """Situation Room OSINT intelligence operations"""
        return AsyncCountriesResource(self._client)

    @cached_property
    def sources(self) -> AsyncSourcesResource:
        """Situation Room OSINT intelligence operations"""
        return AsyncSourcesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOsintResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/y2-intel/y2-py#accessing-raw-response-data-eg-headers
        """
        return AsyncOsintResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOsintResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/y2-intel/y2-py#with_streaming_response
        """
        return AsyncOsintResourceWithStreamingResponse(self)

    async def get_conflict_indicators(
        self,
        *,
        category: Literal[
            "seismic",
            "conflict",
            "political",
            "economic",
            "weather",
            "health",
            "cyber",
            "maritime",
            "fire",
            "aviation",
            "other",
        ]
        | Omit = omit,
        limit: int | Omit = omit,
        region: Literal["mena", "africa", "latam", "asiapac", "europe", "namerica"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OsintGetConflictIndicatorsResponse:
        """Returns the Conflict Indicators Index (CII) values.

        Each item represents a
        conflict indicator with a score from 0-100 and a delta showing recent change.
        Supports filtering by region and category.

        Args:
          category: Filter by event category

          limit: Maximum number of items to return

          region: Filter by geographic region

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/osint/cii",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "category": category,
                        "limit": limit,
                        "region": region,
                    },
                    osint_get_conflict_indicators_params.OsintGetConflictIndicatorsParams,
                ),
            ),
            cast_to=OsintGetConflictIndicatorsResponse,
        )

    async def get_gps_jamming_zones(
        self,
        *,
        limit: int | Omit = omit,
        severity: Literal["low", "moderate", "severe", "critical"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OsintGetGpsJammingZonesResponse:
        """
        Returns GPS interference zones detected via ADS-B navigation accuracy
        degradation analysis, aggregated into H3 hex cells.

        Args:
          limit: Maximum number of zones to return

          severity: Filter by interference severity

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/osint/gps-jamming",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "severity": severity,
                    },
                    osint_get_gps_jamming_zones_params.OsintGetGpsJammingZonesParams,
                ),
            ),
            cast_to=OsintGetGpsJammingZonesResponse,
        )

    async def get_military_posture(
        self,
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OsintGetMilitaryPostureResponse:
        """
        Returns military posture assessments for monitored theaters, based on detected
        military aircraft activity from the OpenSky Network. Each theater has a posture
        level (normal, elevated, critical) and aircraft breakdown by type.

        Args:
          limit: Maximum number of items to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/osint/military-posture",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit}, osint_get_military_posture_params.OsintGetMilitaryPostureParams
                ),
            ),
            cast_to=OsintGetMilitaryPostureResponse,
        )

    async def list_aircraft(
        self,
        *,
        limit: int | Omit = omit,
        theater: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OsintListAircraftResponse:
        """
        Returns tracked military aircraft positions from the OpenSky Network, filtered
        and classified by type (tanker, AWACS, fighter, etc.).

        Args:
          limit: Maximum number of aircraft to return

          theater: Filter by theater ID (e.g. "iran", "taiwan", "baltic")

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/osint/aircraft",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "theater": theater,
                    },
                    osint_list_aircraft_params.OsintListAircraftParams,
                ),
            ),
            cast_to=OsintListAircraftResponse,
        )

    async def list_events(
        self,
        *,
        category: Literal[
            "seismic",
            "conflict",
            "political",
            "economic",
            "weather",
            "health",
            "cyber",
            "maritime",
            "fire",
            "aviation",
            "other",
        ]
        | Omit = omit,
        limit: int | Omit = omit,
        severity: Literal["low", "medium", "high", "critical"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OsintListEventsResponse:
        """Returns OSINT threat events from the Situation Room.

        Supports filtering by
        category, severity, region, and country.

        Args:
          category: Filter by event category

          limit: Maximum number of events to return

          severity: Filter by severity level

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/osint/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "category": category,
                        "limit": limit,
                        "severity": severity,
                    },
                    osint_list_events_params.OsintListEventsParams,
                ),
            ),
            cast_to=OsintListEventsResponse,
        )

    async def list_vessels(
        self,
        *,
        limit: int | Omit = omit,
        region: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OsintListVesselsResponse:
        """
        Returns naval vessel positions sourced from USNI fleet tracker data, including
        carrier strike groups and individual warships.

        Args:
          limit: Maximum number of vessels to return

          region: Filter by region name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/osint/vessels",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "region": region,
                    },
                    osint_list_vessels_params.OsintListVesselsParams,
                ),
            ),
            cast_to=OsintListVesselsResponse,
        )

    async def map_events(
        self,
        *,
        limit: int | Omit = omit,
        region: Literal["mena", "africa", "latam", "asiapac", "europe", "namerica"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OsintMapEventsResponse:
        """Returns OSINT events with geographic coordinates for map display.

        Events without
        coordinates are excluded.

        Args:
          limit: Maximum number of events to return

          region: Filter by geographic region

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/osint/map",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "region": region,
                    },
                    osint_map_events_params.OsintMapEventsParams,
                ),
            ),
            cast_to=OsintMapEventsResponse,
        )


class OsintResourceWithRawResponse:
    def __init__(self, osint: OsintResource) -> None:
        self._osint = osint

        self.get_conflict_indicators = to_raw_response_wrapper(
            osint.get_conflict_indicators,
        )
        self.get_gps_jamming_zones = to_raw_response_wrapper(
            osint.get_gps_jamming_zones,
        )
        self.get_military_posture = to_raw_response_wrapper(
            osint.get_military_posture,
        )
        self.list_aircraft = to_raw_response_wrapper(
            osint.list_aircraft,
        )
        self.list_events = to_raw_response_wrapper(
            osint.list_events,
        )
        self.list_vessels = to_raw_response_wrapper(
            osint.list_vessels,
        )
        self.map_events = to_raw_response_wrapper(
            osint.map_events,
        )

    @cached_property
    def countries(self) -> CountriesResourceWithRawResponse:
        """Situation Room OSINT intelligence operations"""
        return CountriesResourceWithRawResponse(self._osint.countries)

    @cached_property
    def sources(self) -> SourcesResourceWithRawResponse:
        """Situation Room OSINT intelligence operations"""
        return SourcesResourceWithRawResponse(self._osint.sources)


class AsyncOsintResourceWithRawResponse:
    def __init__(self, osint: AsyncOsintResource) -> None:
        self._osint = osint

        self.get_conflict_indicators = async_to_raw_response_wrapper(
            osint.get_conflict_indicators,
        )
        self.get_gps_jamming_zones = async_to_raw_response_wrapper(
            osint.get_gps_jamming_zones,
        )
        self.get_military_posture = async_to_raw_response_wrapper(
            osint.get_military_posture,
        )
        self.list_aircraft = async_to_raw_response_wrapper(
            osint.list_aircraft,
        )
        self.list_events = async_to_raw_response_wrapper(
            osint.list_events,
        )
        self.list_vessels = async_to_raw_response_wrapper(
            osint.list_vessels,
        )
        self.map_events = async_to_raw_response_wrapper(
            osint.map_events,
        )

    @cached_property
    def countries(self) -> AsyncCountriesResourceWithRawResponse:
        """Situation Room OSINT intelligence operations"""
        return AsyncCountriesResourceWithRawResponse(self._osint.countries)

    @cached_property
    def sources(self) -> AsyncSourcesResourceWithRawResponse:
        """Situation Room OSINT intelligence operations"""
        return AsyncSourcesResourceWithRawResponse(self._osint.sources)


class OsintResourceWithStreamingResponse:
    def __init__(self, osint: OsintResource) -> None:
        self._osint = osint

        self.get_conflict_indicators = to_streamed_response_wrapper(
            osint.get_conflict_indicators,
        )
        self.get_gps_jamming_zones = to_streamed_response_wrapper(
            osint.get_gps_jamming_zones,
        )
        self.get_military_posture = to_streamed_response_wrapper(
            osint.get_military_posture,
        )
        self.list_aircraft = to_streamed_response_wrapper(
            osint.list_aircraft,
        )
        self.list_events = to_streamed_response_wrapper(
            osint.list_events,
        )
        self.list_vessels = to_streamed_response_wrapper(
            osint.list_vessels,
        )
        self.map_events = to_streamed_response_wrapper(
            osint.map_events,
        )

    @cached_property
    def countries(self) -> CountriesResourceWithStreamingResponse:
        """Situation Room OSINT intelligence operations"""
        return CountriesResourceWithStreamingResponse(self._osint.countries)

    @cached_property
    def sources(self) -> SourcesResourceWithStreamingResponse:
        """Situation Room OSINT intelligence operations"""
        return SourcesResourceWithStreamingResponse(self._osint.sources)


class AsyncOsintResourceWithStreamingResponse:
    def __init__(self, osint: AsyncOsintResource) -> None:
        self._osint = osint

        self.get_conflict_indicators = async_to_streamed_response_wrapper(
            osint.get_conflict_indicators,
        )
        self.get_gps_jamming_zones = async_to_streamed_response_wrapper(
            osint.get_gps_jamming_zones,
        )
        self.get_military_posture = async_to_streamed_response_wrapper(
            osint.get_military_posture,
        )
        self.list_aircraft = async_to_streamed_response_wrapper(
            osint.list_aircraft,
        )
        self.list_events = async_to_streamed_response_wrapper(
            osint.list_events,
        )
        self.list_vessels = async_to_streamed_response_wrapper(
            osint.list_vessels,
        )
        self.map_events = async_to_streamed_response_wrapper(
            osint.map_events,
        )

    @cached_property
    def countries(self) -> AsyncCountriesResourceWithStreamingResponse:
        """Situation Room OSINT intelligence operations"""
        return AsyncCountriesResourceWithStreamingResponse(self._osint.countries)

    @cached_property
    def sources(self) -> AsyncSourcesResourceWithStreamingResponse:
        """Situation Room OSINT intelligence operations"""
        return AsyncSourcesResourceWithStreamingResponse(self._osint.sources)
