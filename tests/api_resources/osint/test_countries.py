# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from y2 import Y2, AsyncY2
from tests.utils import assert_matches_type
from y2.types.osint import (
    CountryGetCountryNewsResponse,
    CountryGetStockMarketIndexResponse,
    CountryGetIntelligenceBriefResponse,
    CountryGetPredictionMarketsResponse,
    CountryGetCountryInstabilityIndexResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCountries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_country_instability_index(self, client: Y2) -> None:
        country = client.osint.countries.get_country_instability_index(
            "UA",
        )
        assert_matches_type(CountryGetCountryInstabilityIndexResponse, country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_country_instability_index(self, client: Y2) -> None:
        response = client.osint.countries.with_raw_response.get_country_instability_index(
            "UA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = response.parse()
        assert_matches_type(CountryGetCountryInstabilityIndexResponse, country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_country_instability_index(self, client: Y2) -> None:
        with client.osint.countries.with_streaming_response.get_country_instability_index(
            "UA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = response.parse()
            assert_matches_type(CountryGetCountryInstabilityIndexResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_country_instability_index(self, client: Y2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country_code` but received ''"):
            client.osint.countries.with_raw_response.get_country_instability_index(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_country_news(self, client: Y2) -> None:
        country = client.osint.countries.get_country_news(
            country_code="US",
        )
        assert_matches_type(CountryGetCountryNewsResponse, country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_country_news_with_all_params(self, client: Y2) -> None:
        country = client.osint.countries.get_country_news(
            country_code="US",
            limit=1,
        )
        assert_matches_type(CountryGetCountryNewsResponse, country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_country_news(self, client: Y2) -> None:
        response = client.osint.countries.with_raw_response.get_country_news(
            country_code="US",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = response.parse()
        assert_matches_type(CountryGetCountryNewsResponse, country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_country_news(self, client: Y2) -> None:
        with client.osint.countries.with_streaming_response.get_country_news(
            country_code="US",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = response.parse()
            assert_matches_type(CountryGetCountryNewsResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_country_news(self, client: Y2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country_code` but received ''"):
            client.osint.countries.with_raw_response.get_country_news(
                country_code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_intelligence_brief(self, client: Y2) -> None:
        country = client.osint.countries.get_intelligence_brief(
            "US",
        )
        assert_matches_type(CountryGetIntelligenceBriefResponse, country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_intelligence_brief(self, client: Y2) -> None:
        response = client.osint.countries.with_raw_response.get_intelligence_brief(
            "US",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = response.parse()
        assert_matches_type(CountryGetIntelligenceBriefResponse, country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_intelligence_brief(self, client: Y2) -> None:
        with client.osint.countries.with_streaming_response.get_intelligence_brief(
            "US",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = response.parse()
            assert_matches_type(CountryGetIntelligenceBriefResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_intelligence_brief(self, client: Y2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country_code` but received ''"):
            client.osint.countries.with_raw_response.get_intelligence_brief(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_prediction_markets(self, client: Y2) -> None:
        country = client.osint.countries.get_prediction_markets(
            country_code="US",
        )
        assert_matches_type(CountryGetPredictionMarketsResponse, country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_prediction_markets_with_all_params(self, client: Y2) -> None:
        country = client.osint.countries.get_prediction_markets(
            country_code="US",
            limit=1,
        )
        assert_matches_type(CountryGetPredictionMarketsResponse, country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_prediction_markets(self, client: Y2) -> None:
        response = client.osint.countries.with_raw_response.get_prediction_markets(
            country_code="US",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = response.parse()
        assert_matches_type(CountryGetPredictionMarketsResponse, country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_prediction_markets(self, client: Y2) -> None:
        with client.osint.countries.with_streaming_response.get_prediction_markets(
            country_code="US",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = response.parse()
            assert_matches_type(CountryGetPredictionMarketsResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_prediction_markets(self, client: Y2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country_code` but received ''"):
            client.osint.countries.with_raw_response.get_prediction_markets(
                country_code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_stock_market_index(self, client: Y2) -> None:
        country = client.osint.countries.get_stock_market_index(
            "US",
        )
        assert_matches_type(CountryGetStockMarketIndexResponse, country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_stock_market_index(self, client: Y2) -> None:
        response = client.osint.countries.with_raw_response.get_stock_market_index(
            "US",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = response.parse()
        assert_matches_type(CountryGetStockMarketIndexResponse, country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_stock_market_index(self, client: Y2) -> None:
        with client.osint.countries.with_streaming_response.get_stock_market_index(
            "US",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = response.parse()
            assert_matches_type(CountryGetStockMarketIndexResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_stock_market_index(self, client: Y2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country_code` but received ''"):
            client.osint.countries.with_raw_response.get_stock_market_index(
                "",
            )


class TestAsyncCountries:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_country_instability_index(self, async_client: AsyncY2) -> None:
        country = await async_client.osint.countries.get_country_instability_index(
            "UA",
        )
        assert_matches_type(CountryGetCountryInstabilityIndexResponse, country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_country_instability_index(self, async_client: AsyncY2) -> None:
        response = await async_client.osint.countries.with_raw_response.get_country_instability_index(
            "UA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = await response.parse()
        assert_matches_type(CountryGetCountryInstabilityIndexResponse, country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_country_instability_index(self, async_client: AsyncY2) -> None:
        async with async_client.osint.countries.with_streaming_response.get_country_instability_index(
            "UA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = await response.parse()
            assert_matches_type(CountryGetCountryInstabilityIndexResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_country_instability_index(self, async_client: AsyncY2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country_code` but received ''"):
            await async_client.osint.countries.with_raw_response.get_country_instability_index(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_country_news(self, async_client: AsyncY2) -> None:
        country = await async_client.osint.countries.get_country_news(
            country_code="US",
        )
        assert_matches_type(CountryGetCountryNewsResponse, country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_country_news_with_all_params(self, async_client: AsyncY2) -> None:
        country = await async_client.osint.countries.get_country_news(
            country_code="US",
            limit=1,
        )
        assert_matches_type(CountryGetCountryNewsResponse, country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_country_news(self, async_client: AsyncY2) -> None:
        response = await async_client.osint.countries.with_raw_response.get_country_news(
            country_code="US",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = await response.parse()
        assert_matches_type(CountryGetCountryNewsResponse, country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_country_news(self, async_client: AsyncY2) -> None:
        async with async_client.osint.countries.with_streaming_response.get_country_news(
            country_code="US",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = await response.parse()
            assert_matches_type(CountryGetCountryNewsResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_country_news(self, async_client: AsyncY2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country_code` but received ''"):
            await async_client.osint.countries.with_raw_response.get_country_news(
                country_code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_intelligence_brief(self, async_client: AsyncY2) -> None:
        country = await async_client.osint.countries.get_intelligence_brief(
            "US",
        )
        assert_matches_type(CountryGetIntelligenceBriefResponse, country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_intelligence_brief(self, async_client: AsyncY2) -> None:
        response = await async_client.osint.countries.with_raw_response.get_intelligence_brief(
            "US",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = await response.parse()
        assert_matches_type(CountryGetIntelligenceBriefResponse, country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_intelligence_brief(self, async_client: AsyncY2) -> None:
        async with async_client.osint.countries.with_streaming_response.get_intelligence_brief(
            "US",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = await response.parse()
            assert_matches_type(CountryGetIntelligenceBriefResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_intelligence_brief(self, async_client: AsyncY2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country_code` but received ''"):
            await async_client.osint.countries.with_raw_response.get_intelligence_brief(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_prediction_markets(self, async_client: AsyncY2) -> None:
        country = await async_client.osint.countries.get_prediction_markets(
            country_code="US",
        )
        assert_matches_type(CountryGetPredictionMarketsResponse, country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_prediction_markets_with_all_params(self, async_client: AsyncY2) -> None:
        country = await async_client.osint.countries.get_prediction_markets(
            country_code="US",
            limit=1,
        )
        assert_matches_type(CountryGetPredictionMarketsResponse, country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_prediction_markets(self, async_client: AsyncY2) -> None:
        response = await async_client.osint.countries.with_raw_response.get_prediction_markets(
            country_code="US",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = await response.parse()
        assert_matches_type(CountryGetPredictionMarketsResponse, country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_prediction_markets(self, async_client: AsyncY2) -> None:
        async with async_client.osint.countries.with_streaming_response.get_prediction_markets(
            country_code="US",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = await response.parse()
            assert_matches_type(CountryGetPredictionMarketsResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_prediction_markets(self, async_client: AsyncY2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country_code` but received ''"):
            await async_client.osint.countries.with_raw_response.get_prediction_markets(
                country_code="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_stock_market_index(self, async_client: AsyncY2) -> None:
        country = await async_client.osint.countries.get_stock_market_index(
            "US",
        )
        assert_matches_type(CountryGetStockMarketIndexResponse, country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_stock_market_index(self, async_client: AsyncY2) -> None:
        response = await async_client.osint.countries.with_raw_response.get_stock_market_index(
            "US",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        country = await response.parse()
        assert_matches_type(CountryGetStockMarketIndexResponse, country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_stock_market_index(self, async_client: AsyncY2) -> None:
        async with async_client.osint.countries.with_streaming_response.get_stock_market_index(
            "US",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            country = await response.parse()
            assert_matches_type(CountryGetStockMarketIndexResponse, country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_stock_market_index(self, async_client: AsyncY2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country_code` but received ''"):
            await async_client.osint.countries.with_raw_response.get_stock_market_index(
                "",
            )
