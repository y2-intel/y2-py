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
    """Situation Room events, feeds, country data, and source health"""

    @cached_property
    def countries(self) -> CountriesResource:
        """Situation Room events, feeds, country data, and source health"""
        return CountriesResource(self._client)

    @cached_property
    def sources(self) -> SourcesResource:
        """Situation Room events, feeds, country data, and source health"""
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
        cursor: str | Omit = omit,
        format: Literal["json", "ndjson"] | Omit = omit,
        limit: int | Omit = omit,
        region: Literal["mena", "africa", "latam", "asiapac", "europe", "namerica"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OsintGetConflictIndicatorsResponse:
        """
        Lists Conflict Indicators Index (CII) values with 0–100 scores and recent-change
        deltas. Supports region and category filters.

        Supports x402 pay-per-request. Requests with a valid Bearer token use API-key
        authentication. Without a Bearer API key, start the x402 flow from the
        `402 Payment Required` response and `PAYMENT-REQUIRED` header; retry with
        `PAYMENT-SIGNATURE`.

        Args:
          category: Filter by event category

          cursor: Opaque continuation token from the previous response. Bound to the original
              filters and ordering.

          format: `json` uses the resource envelope; `ndjson` streams one canonical row per line.

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
                        "cursor": cursor,
                        "format": format,
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
        cursor: str | Omit = omit,
        format: Literal["json", "ndjson", "geojson"] | Omit = omit,
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
        Lists GPS interference zones inferred from ADS-B navigation-accuracy degradation
        and aggregated into H3 cells.

        Coverage spans 22 theaters on a tiered cadence within the shared Wingbits quota:

        | Tier      | Cadence   | Theaters                                                                                        |
        | --------- | --------- | ----------------------------------------------------------------------------------------------- |
        | Hot       | Hourly    | iran, blacksea, israelgaza, redsea, taiwan, scs                                                 |
        | Watch     | Every 3h  | emed, korea, caucasus, kaliningrad-tight, finland-russia, us-south, bashi-luzon, east-china-sea |
        | Perimeter | Every 6h  | us-pacom-west, us-northeast, aleutian-bering, baltic-south, giuk-greenland                      |
        | Daily     | Every 24h | baltic-north, us-north, arctic-greenland-pass                                                   |

        Records expire 30 minutes after fetch. Align polling with the theater's tier.

        Supports x402 pay-per-request. Requests with a valid Bearer token use API-key
        authentication. Without a Bearer API key, start the x402 flow from the
        `402 Payment Required` response and `PAYMENT-REQUIRED` header; retry with
        `PAYMENT-SIGNATURE`.

        Args:
          cursor: Opaque continuation token from the previous response. Bound to the original
              filters and ordering.

          format: Select the JSON resource envelope, row-oriented NDJSON, or an RFC 7946
              FeatureCollection.

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
                        "cursor": cursor,
                        "format": format,
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
        cursor: str | Omit = omit,
        format: Literal["json", "ndjson", "geojson"] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OsintGetMilitaryPostureResponse:
        """
        Lists theater posture assessments based on Wingbits ADS-B military aircraft
        activity. Each includes a `normal`, `elevated`, or `critical` posture and
        aircraft counts by type.

        > **Status:** Aircraft ingestion has been disabled since May 8, 2026, to reserve
        > the shared Wingbits quota for GPS interference detection. This endpoint may
        > return empty or stale results. `/osint/gps-jamming` is unaffected.

        Supports x402 pay-per-request. Requests with a valid Bearer token use API-key
        authentication. Without a Bearer API key, start the x402 flow from the
        `402 Payment Required` response and `PAYMENT-REQUIRED` header; retry with
        `PAYMENT-SIGNATURE`.

        Args:
          cursor: Opaque continuation token from the previous response. Bound to the original
              filters and ordering.

          format: Select the JSON resource envelope, row-oriented NDJSON, or an RFC 7946
              FeatureCollection.

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
                    {
                        "cursor": cursor,
                        "format": format,
                        "limit": limit,
                    },
                    osint_get_military_posture_params.OsintGetMilitaryPostureParams,
                ),
            ),
            cast_to=OsintGetMilitaryPostureResponse,
        )

    def list_aircraft(
        self,
        *,
        cursor: str | Omit = omit,
        format: Literal["json", "ndjson", "geojson"] | Omit = omit,
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
        Lists Wingbits ADS-B military aircraft positions, classified by type such as
        tanker, AWACS, or fighter.

        > **Status:** Aircraft ingestion has been disabled since May 8, 2026, to reserve
        > the shared Wingbits quota for GPS interference detection. This endpoint may
        > return empty or stale results. `/osint/gps-jamming` is unaffected.

        Supports x402 pay-per-request. Requests with a valid Bearer token use API-key
        authentication. Without a Bearer API key, start the x402 flow from the
        `402 Payment Required` response and `PAYMENT-REQUIRED` header; retry with
        `PAYMENT-SIGNATURE`.

        Args:
          cursor: Opaque continuation token from the previous response. Bound to the original
              filters and ordering.

          format: Select the JSON resource envelope, row-oriented NDJSON, or an RFC 7946
              FeatureCollection.

          limit: Maximum number of aircraft to return

          theater: Filter by theater ID (e.g. "iran", "taiwan", "blacksea", "scs")

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
                        "cursor": cursor,
                        "format": format,
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
        cursor: str | Omit = omit,
        format: Literal["json", "ndjson", "geojson"] | Omit = omit,
        limit: int | Omit = omit,
        severity: Literal["low", "medium", "high", "critical"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OsintListEventsResponse:
        """Lists Situation Room threat events.

        Supports category and severity filters.

        Supports x402 pay-per-request. Requests with a valid Bearer token use API-key
        authentication. Without a Bearer API key, start the x402 flow from the
        `402 Payment Required` response and `PAYMENT-REQUIRED` header; retry with
        `PAYMENT-SIGNATURE`.

        Args:
          category: Filter by event category

          cursor: Opaque continuation token from the previous response. Bound to the original
              filters and ordering.

          format: Select the JSON resource envelope, row-oriented NDJSON, or an RFC 7946
              FeatureCollection.

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
                        "cursor": cursor,
                        "format": format,
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
        cursor: str | Omit = omit,
        format: Literal["json", "ndjson", "geojson"] | Omit = omit,
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
        Lists USNI fleet-tracker positions for carrier strike groups and warships.

        Supports x402 pay-per-request. Requests with a valid Bearer token use API-key
        authentication. Without a Bearer API key, start the x402 flow from the
        `402 Payment Required` response and `PAYMENT-REQUIRED` header; retry with
        `PAYMENT-SIGNATURE`.

        Args:
          cursor: Opaque continuation token from the previous response. Bound to the original
              filters and ordering.

          format: Select the JSON resource envelope, row-oriented NDJSON, or an RFC 7946
              FeatureCollection.

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
                        "cursor": cursor,
                        "format": format,
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
        cursor: str | Omit = omit,
        format: Literal["json", "ndjson", "geojson"] | Omit = omit,
        limit: int | Omit = omit,
        region: Literal["mena", "africa", "latam", "asiapac", "europe", "namerica"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OsintMapEventsResponse:
        """Lists geolocated OSINT events for map display.

        Excludes events without
        coordinates.

        Supports x402 pay-per-request. Requests with a valid Bearer token use API-key
        authentication. Without a Bearer API key, start the x402 flow from the
        `402 Payment Required` response and `PAYMENT-REQUIRED` header; retry with
        `PAYMENT-SIGNATURE`.

        Args:
          cursor: Opaque continuation token from the previous response. Bound to the original
              filters and ordering.

          format: Select the JSON resource envelope, row-oriented NDJSON, or an RFC 7946
              FeatureCollection.

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
                        "cursor": cursor,
                        "format": format,
                        "limit": limit,
                        "region": region,
                    },
                    osint_map_events_params.OsintMapEventsParams,
                ),
            ),
            cast_to=OsintMapEventsResponse,
        )


class AsyncOsintResource(AsyncAPIResource):
    """Situation Room events, feeds, country data, and source health"""

    @cached_property
    def countries(self) -> AsyncCountriesResource:
        """Situation Room events, feeds, country data, and source health"""
        return AsyncCountriesResource(self._client)

    @cached_property
    def sources(self) -> AsyncSourcesResource:
        """Situation Room events, feeds, country data, and source health"""
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
        cursor: str | Omit = omit,
        format: Literal["json", "ndjson"] | Omit = omit,
        limit: int | Omit = omit,
        region: Literal["mena", "africa", "latam", "asiapac", "europe", "namerica"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OsintGetConflictIndicatorsResponse:
        """
        Lists Conflict Indicators Index (CII) values with 0–100 scores and recent-change
        deltas. Supports region and category filters.

        Supports x402 pay-per-request. Requests with a valid Bearer token use API-key
        authentication. Without a Bearer API key, start the x402 flow from the
        `402 Payment Required` response and `PAYMENT-REQUIRED` header; retry with
        `PAYMENT-SIGNATURE`.

        Args:
          category: Filter by event category

          cursor: Opaque continuation token from the previous response. Bound to the original
              filters and ordering.

          format: `json` uses the resource envelope; `ndjson` streams one canonical row per line.

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
                        "cursor": cursor,
                        "format": format,
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
        cursor: str | Omit = omit,
        format: Literal["json", "ndjson", "geojson"] | Omit = omit,
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
        Lists GPS interference zones inferred from ADS-B navigation-accuracy degradation
        and aggregated into H3 cells.

        Coverage spans 22 theaters on a tiered cadence within the shared Wingbits quota:

        | Tier      | Cadence   | Theaters                                                                                        |
        | --------- | --------- | ----------------------------------------------------------------------------------------------- |
        | Hot       | Hourly    | iran, blacksea, israelgaza, redsea, taiwan, scs                                                 |
        | Watch     | Every 3h  | emed, korea, caucasus, kaliningrad-tight, finland-russia, us-south, bashi-luzon, east-china-sea |
        | Perimeter | Every 6h  | us-pacom-west, us-northeast, aleutian-bering, baltic-south, giuk-greenland                      |
        | Daily     | Every 24h | baltic-north, us-north, arctic-greenland-pass                                                   |

        Records expire 30 minutes after fetch. Align polling with the theater's tier.

        Supports x402 pay-per-request. Requests with a valid Bearer token use API-key
        authentication. Without a Bearer API key, start the x402 flow from the
        `402 Payment Required` response and `PAYMENT-REQUIRED` header; retry with
        `PAYMENT-SIGNATURE`.

        Args:
          cursor: Opaque continuation token from the previous response. Bound to the original
              filters and ordering.

          format: Select the JSON resource envelope, row-oriented NDJSON, or an RFC 7946
              FeatureCollection.

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
                        "cursor": cursor,
                        "format": format,
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
        cursor: str | Omit = omit,
        format: Literal["json", "ndjson", "geojson"] | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OsintGetMilitaryPostureResponse:
        """
        Lists theater posture assessments based on Wingbits ADS-B military aircraft
        activity. Each includes a `normal`, `elevated`, or `critical` posture and
        aircraft counts by type.

        > **Status:** Aircraft ingestion has been disabled since May 8, 2026, to reserve
        > the shared Wingbits quota for GPS interference detection. This endpoint may
        > return empty or stale results. `/osint/gps-jamming` is unaffected.

        Supports x402 pay-per-request. Requests with a valid Bearer token use API-key
        authentication. Without a Bearer API key, start the x402 flow from the
        `402 Payment Required` response and `PAYMENT-REQUIRED` header; retry with
        `PAYMENT-SIGNATURE`.

        Args:
          cursor: Opaque continuation token from the previous response. Bound to the original
              filters and ordering.

          format: Select the JSON resource envelope, row-oriented NDJSON, or an RFC 7946
              FeatureCollection.

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
                    {
                        "cursor": cursor,
                        "format": format,
                        "limit": limit,
                    },
                    osint_get_military_posture_params.OsintGetMilitaryPostureParams,
                ),
            ),
            cast_to=OsintGetMilitaryPostureResponse,
        )

    async def list_aircraft(
        self,
        *,
        cursor: str | Omit = omit,
        format: Literal["json", "ndjson", "geojson"] | Omit = omit,
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
        Lists Wingbits ADS-B military aircraft positions, classified by type such as
        tanker, AWACS, or fighter.

        > **Status:** Aircraft ingestion has been disabled since May 8, 2026, to reserve
        > the shared Wingbits quota for GPS interference detection. This endpoint may
        > return empty or stale results. `/osint/gps-jamming` is unaffected.

        Supports x402 pay-per-request. Requests with a valid Bearer token use API-key
        authentication. Without a Bearer API key, start the x402 flow from the
        `402 Payment Required` response and `PAYMENT-REQUIRED` header; retry with
        `PAYMENT-SIGNATURE`.

        Args:
          cursor: Opaque continuation token from the previous response. Bound to the original
              filters and ordering.

          format: Select the JSON resource envelope, row-oriented NDJSON, or an RFC 7946
              FeatureCollection.

          limit: Maximum number of aircraft to return

          theater: Filter by theater ID (e.g. "iran", "taiwan", "blacksea", "scs")

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
                        "cursor": cursor,
                        "format": format,
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
        cursor: str | Omit = omit,
        format: Literal["json", "ndjson", "geojson"] | Omit = omit,
        limit: int | Omit = omit,
        severity: Literal["low", "medium", "high", "critical"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OsintListEventsResponse:
        """Lists Situation Room threat events.

        Supports category and severity filters.

        Supports x402 pay-per-request. Requests with a valid Bearer token use API-key
        authentication. Without a Bearer API key, start the x402 flow from the
        `402 Payment Required` response and `PAYMENT-REQUIRED` header; retry with
        `PAYMENT-SIGNATURE`.

        Args:
          category: Filter by event category

          cursor: Opaque continuation token from the previous response. Bound to the original
              filters and ordering.

          format: Select the JSON resource envelope, row-oriented NDJSON, or an RFC 7946
              FeatureCollection.

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
                        "cursor": cursor,
                        "format": format,
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
        cursor: str | Omit = omit,
        format: Literal["json", "ndjson", "geojson"] | Omit = omit,
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
        Lists USNI fleet-tracker positions for carrier strike groups and warships.

        Supports x402 pay-per-request. Requests with a valid Bearer token use API-key
        authentication. Without a Bearer API key, start the x402 flow from the
        `402 Payment Required` response and `PAYMENT-REQUIRED` header; retry with
        `PAYMENT-SIGNATURE`.

        Args:
          cursor: Opaque continuation token from the previous response. Bound to the original
              filters and ordering.

          format: Select the JSON resource envelope, row-oriented NDJSON, or an RFC 7946
              FeatureCollection.

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
                        "cursor": cursor,
                        "format": format,
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
        cursor: str | Omit = omit,
        format: Literal["json", "ndjson", "geojson"] | Omit = omit,
        limit: int | Omit = omit,
        region: Literal["mena", "africa", "latam", "asiapac", "europe", "namerica"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OsintMapEventsResponse:
        """Lists geolocated OSINT events for map display.

        Excludes events without
        coordinates.

        Supports x402 pay-per-request. Requests with a valid Bearer token use API-key
        authentication. Without a Bearer API key, start the x402 flow from the
        `402 Payment Required` response and `PAYMENT-REQUIRED` header; retry with
        `PAYMENT-SIGNATURE`.

        Args:
          cursor: Opaque continuation token from the previous response. Bound to the original
              filters and ordering.

          format: Select the JSON resource envelope, row-oriented NDJSON, or an RFC 7946
              FeatureCollection.

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
                        "cursor": cursor,
                        "format": format,
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
        """Situation Room events, feeds, country data, and source health"""
        return CountriesResourceWithRawResponse(self._osint.countries)

    @cached_property
    def sources(self) -> SourcesResourceWithRawResponse:
        """Situation Room events, feeds, country data, and source health"""
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
        """Situation Room events, feeds, country data, and source health"""
        return AsyncCountriesResourceWithRawResponse(self._osint.countries)

    @cached_property
    def sources(self) -> AsyncSourcesResourceWithRawResponse:
        """Situation Room events, feeds, country data, and source health"""
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
        """Situation Room events, feeds, country data, and source health"""
        return CountriesResourceWithStreamingResponse(self._osint.countries)

    @cached_property
    def sources(self) -> SourcesResourceWithStreamingResponse:
        """Situation Room events, feeds, country data, and source health"""
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
        """Situation Room events, feeds, country data, and source health"""
        return AsyncCountriesResourceWithStreamingResponse(self._osint.countries)

    @cached_property
    def sources(self) -> AsyncSourcesResourceWithStreamingResponse:
        """Situation Room events, feeds, country data, and source health"""
        return AsyncSourcesResourceWithStreamingResponse(self._osint.sources)
