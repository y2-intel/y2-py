# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.osint import country_get_country_news_params, country_get_prediction_markets_params
from ..._base_client import make_request_options
from ...types.osint.country_get_country_news_response import CountryGetCountryNewsResponse
from ...types.osint.country_get_intelligence_brief_response import CountryGetIntelligenceBriefResponse
from ...types.osint.country_get_prediction_markets_response import CountryGetPredictionMarketsResponse
from ...types.osint.country_get_stock_market_index_response import CountryGetStockMarketIndexResponse
from ...types.osint.country_get_country_instability_index_response import CountryGetCountryInstabilityIndexResponse

__all__ = ["CountriesResource", "AsyncCountriesResource"]


class CountriesResource(SyncAPIResource):
    """Situation Room OSINT intelligence operations"""

    @cached_property
    def with_raw_response(self) -> CountriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/y2-intel/y2-py#accessing-raw-response-data-eg-headers
        """
        return CountriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CountriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/y2-intel/y2-py#with_streaming_response
        """
        return CountriesResourceWithStreamingResponse(self)

    def get_country_instability_index(
        self,
        country_code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CountryGetCountryInstabilityIndexResponse:
        """
        Returns the per-country Conflict Indicators Index (CII) score, including
        baseline, delta, and component breakdown.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not country_code:
            raise ValueError(f"Expected a non-empty value for `country_code` but received {country_code!r}")
        return self._get(
            path_template("/osint/countries/{country_code}/cii", country_code=country_code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CountryGetCountryInstabilityIndexResponse,
        )

    def get_country_news(
        self,
        country_code: str,
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CountryGetCountryNewsResponse:
        """
        Returns recent news items specific to a given country, sourced from the OSINT
        event pipeline.

        Args:
          limit: Maximum number of news items to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not country_code:
            raise ValueError(f"Expected a non-empty value for `country_code` but received {country_code!r}")
        return self._get(
            path_template("/osint/countries/{country_code}/news", country_code=country_code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit}, country_get_country_news_params.CountryGetCountryNewsParams),
            ),
            cast_to=CountryGetCountryNewsResponse,
        )

    def get_intelligence_brief(
        self,
        country_code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CountryGetIntelligenceBriefResponse:
        """Returns an AI-generated intelligence brief for a specific country.

        Briefs are
        generated periodically and cached.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not country_code:
            raise ValueError(f"Expected a non-empty value for `country_code` but received {country_code!r}")
        return self._get(
            path_template("/osint/countries/{country_code}/brief", country_code=country_code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CountryGetIntelligenceBriefResponse,
        )

    def get_prediction_markets(
        self,
        country_code: str,
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CountryGetPredictionMarketsResponse:
        """
        Returns prediction market data for a specific country, including probabilities
        and trading volumes.

        Args:
          limit: Maximum number of predictions to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not country_code:
            raise ValueError(f"Expected a non-empty value for `country_code` but received {country_code!r}")
        return self._get(
            path_template("/osint/countries/{country_code}/predictions", country_code=country_code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"limit": limit}, country_get_prediction_markets_params.CountryGetPredictionMarketsParams
                ),
            ),
            cast_to=CountryGetPredictionMarketsResponse,
        )

    def get_stock_market_index(
        self,
        country_code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CountryGetStockMarketIndexResponse:
        """
        Returns the primary stock market index data for a specific country, including
        weekly change and currency.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not country_code:
            raise ValueError(f"Expected a non-empty value for `country_code` but received {country_code!r}")
        return self._get(
            path_template("/osint/countries/{country_code}/markets", country_code=country_code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CountryGetStockMarketIndexResponse,
        )


class AsyncCountriesResource(AsyncAPIResource):
    """Situation Room OSINT intelligence operations"""

    @cached_property
    def with_raw_response(self) -> AsyncCountriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/y2-intel/y2-py#accessing-raw-response-data-eg-headers
        """
        return AsyncCountriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCountriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/y2-intel/y2-py#with_streaming_response
        """
        return AsyncCountriesResourceWithStreamingResponse(self)

    async def get_country_instability_index(
        self,
        country_code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CountryGetCountryInstabilityIndexResponse:
        """
        Returns the per-country Conflict Indicators Index (CII) score, including
        baseline, delta, and component breakdown.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not country_code:
            raise ValueError(f"Expected a non-empty value for `country_code` but received {country_code!r}")
        return await self._get(
            path_template("/osint/countries/{country_code}/cii", country_code=country_code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CountryGetCountryInstabilityIndexResponse,
        )

    async def get_country_news(
        self,
        country_code: str,
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CountryGetCountryNewsResponse:
        """
        Returns recent news items specific to a given country, sourced from the OSINT
        event pipeline.

        Args:
          limit: Maximum number of news items to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not country_code:
            raise ValueError(f"Expected a non-empty value for `country_code` but received {country_code!r}")
        return await self._get(
            path_template("/osint/countries/{country_code}/news", country_code=country_code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit}, country_get_country_news_params.CountryGetCountryNewsParams
                ),
            ),
            cast_to=CountryGetCountryNewsResponse,
        )

    async def get_intelligence_brief(
        self,
        country_code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CountryGetIntelligenceBriefResponse:
        """Returns an AI-generated intelligence brief for a specific country.

        Briefs are
        generated periodically and cached.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not country_code:
            raise ValueError(f"Expected a non-empty value for `country_code` but received {country_code!r}")
        return await self._get(
            path_template("/osint/countries/{country_code}/brief", country_code=country_code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CountryGetIntelligenceBriefResponse,
        )

    async def get_prediction_markets(
        self,
        country_code: str,
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CountryGetPredictionMarketsResponse:
        """
        Returns prediction market data for a specific country, including probabilities
        and trading volumes.

        Args:
          limit: Maximum number of predictions to return

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not country_code:
            raise ValueError(f"Expected a non-empty value for `country_code` but received {country_code!r}")
        return await self._get(
            path_template("/osint/countries/{country_code}/predictions", country_code=country_code),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit}, country_get_prediction_markets_params.CountryGetPredictionMarketsParams
                ),
            ),
            cast_to=CountryGetPredictionMarketsResponse,
        )

    async def get_stock_market_index(
        self,
        country_code: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CountryGetStockMarketIndexResponse:
        """
        Returns the primary stock market index data for a specific country, including
        weekly change and currency.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not country_code:
            raise ValueError(f"Expected a non-empty value for `country_code` but received {country_code!r}")
        return await self._get(
            path_template("/osint/countries/{country_code}/markets", country_code=country_code),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CountryGetStockMarketIndexResponse,
        )


class CountriesResourceWithRawResponse:
    def __init__(self, countries: CountriesResource) -> None:
        self._countries = countries

        self.get_country_instability_index = to_raw_response_wrapper(
            countries.get_country_instability_index,
        )
        self.get_country_news = to_raw_response_wrapper(
            countries.get_country_news,
        )
        self.get_intelligence_brief = to_raw_response_wrapper(
            countries.get_intelligence_brief,
        )
        self.get_prediction_markets = to_raw_response_wrapper(
            countries.get_prediction_markets,
        )
        self.get_stock_market_index = to_raw_response_wrapper(
            countries.get_stock_market_index,
        )


class AsyncCountriesResourceWithRawResponse:
    def __init__(self, countries: AsyncCountriesResource) -> None:
        self._countries = countries

        self.get_country_instability_index = async_to_raw_response_wrapper(
            countries.get_country_instability_index,
        )
        self.get_country_news = async_to_raw_response_wrapper(
            countries.get_country_news,
        )
        self.get_intelligence_brief = async_to_raw_response_wrapper(
            countries.get_intelligence_brief,
        )
        self.get_prediction_markets = async_to_raw_response_wrapper(
            countries.get_prediction_markets,
        )
        self.get_stock_market_index = async_to_raw_response_wrapper(
            countries.get_stock_market_index,
        )


class CountriesResourceWithStreamingResponse:
    def __init__(self, countries: CountriesResource) -> None:
        self._countries = countries

        self.get_country_instability_index = to_streamed_response_wrapper(
            countries.get_country_instability_index,
        )
        self.get_country_news = to_streamed_response_wrapper(
            countries.get_country_news,
        )
        self.get_intelligence_brief = to_streamed_response_wrapper(
            countries.get_intelligence_brief,
        )
        self.get_prediction_markets = to_streamed_response_wrapper(
            countries.get_prediction_markets,
        )
        self.get_stock_market_index = to_streamed_response_wrapper(
            countries.get_stock_market_index,
        )


class AsyncCountriesResourceWithStreamingResponse:
    def __init__(self, countries: AsyncCountriesResource) -> None:
        self._countries = countries

        self.get_country_instability_index = async_to_streamed_response_wrapper(
            countries.get_country_instability_index,
        )
        self.get_country_news = async_to_streamed_response_wrapper(
            countries.get_country_news,
        )
        self.get_intelligence_brief = async_to_streamed_response_wrapper(
            countries.get_intelligence_brief,
        )
        self.get_prediction_markets = async_to_streamed_response_wrapper(
            countries.get_prediction_markets,
        )
        self.get_stock_market_index = async_to_streamed_response_wrapper(
            countries.get_stock_market_index,
        )
