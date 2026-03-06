# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.osint.source_get_data_source_health_response import SourceGetDataSourceHealthResponse

__all__ = ["SourcesResource", "AsyncSourcesResource"]


class SourcesResource(SyncAPIResource):
    """Situation Room OSINT intelligence operations"""

    @cached_property
    def with_raw_response(self) -> SourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/y2-intel/y2-py#accessing-raw-response-data-eg-headers
        """
        return SourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/y2-intel/y2-py#with_streaming_response
        """
        return SourcesResourceWithStreamingResponse(self)

    def get_data_source_health(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceGetDataSourceHealthResponse:
        """
        Returns the health status of all OSINT data sources, including circuit breaker
        state and failure counts.
        """
        return self._get(
            "/osint/sources/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceGetDataSourceHealthResponse,
        )


class AsyncSourcesResource(AsyncAPIResource):
    """Situation Room OSINT intelligence operations"""

    @cached_property
    def with_raw_response(self) -> AsyncSourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/y2-intel/y2-py#accessing-raw-response-data-eg-headers
        """
        return AsyncSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/y2-intel/y2-py#with_streaming_response
        """
        return AsyncSourcesResourceWithStreamingResponse(self)

    async def get_data_source_health(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SourceGetDataSourceHealthResponse:
        """
        Returns the health status of all OSINT data sources, including circuit breaker
        state and failure counts.
        """
        return await self._get(
            "/osint/sources/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SourceGetDataSourceHealthResponse,
        )


class SourcesResourceWithRawResponse:
    def __init__(self, sources: SourcesResource) -> None:
        self._sources = sources

        self.get_data_source_health = to_raw_response_wrapper(
            sources.get_data_source_health,
        )


class AsyncSourcesResourceWithRawResponse:
    def __init__(self, sources: AsyncSourcesResource) -> None:
        self._sources = sources

        self.get_data_source_health = async_to_raw_response_wrapper(
            sources.get_data_source_health,
        )


class SourcesResourceWithStreamingResponse:
    def __init__(self, sources: SourcesResource) -> None:
        self._sources = sources

        self.get_data_source_health = to_streamed_response_wrapper(
            sources.get_data_source_health,
        )


class AsyncSourcesResourceWithStreamingResponse:
    def __init__(self, sources: AsyncSourcesResource) -> None:
        self._sources = sources

        self.get_data_source_health = async_to_streamed_response_wrapper(
            sources.get_data_source_health,
        )
