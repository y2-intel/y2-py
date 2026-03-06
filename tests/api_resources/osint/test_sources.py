# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from y2 import Y2, AsyncY2
from tests.utils import assert_matches_type
from y2.types.osint import SourceGetDataSourceHealthResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSources:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_data_source_health(self, client: Y2) -> None:
        source = client.osint.sources.get_data_source_health()
        assert_matches_type(SourceGetDataSourceHealthResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_data_source_health(self, client: Y2) -> None:
        response = client.osint.sources.with_raw_response.get_data_source_health()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = response.parse()
        assert_matches_type(SourceGetDataSourceHealthResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_data_source_health(self, client: Y2) -> None:
        with client.osint.sources.with_streaming_response.get_data_source_health() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = response.parse()
            assert_matches_type(SourceGetDataSourceHealthResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSources:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_data_source_health(self, async_client: AsyncY2) -> None:
        source = await async_client.osint.sources.get_data_source_health()
        assert_matches_type(SourceGetDataSourceHealthResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_data_source_health(self, async_client: AsyncY2) -> None:
        response = await async_client.osint.sources.with_raw_response.get_data_source_health()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        source = await response.parse()
        assert_matches_type(SourceGetDataSourceHealthResponse, source, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_data_source_health(self, async_client: AsyncY2) -> None:
        async with async_client.osint.sources.with_streaming_response.get_data_source_health() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            source = await response.parse()
            assert_matches_type(SourceGetDataSourceHealthResponse, source, path=["response"])

        assert cast(Any, response.is_closed) is True
