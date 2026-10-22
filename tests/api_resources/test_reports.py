# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from y2 import Y2, AsyncY2
from y2.types import (
    ReportListResponse,
    ReportRetrieveResponse,
    ReportRetrieveAudioResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Y2) -> None:
        report = client.reports.retrieve(
            report_id="rpt_0123456789abcdef01234567",
        )
        assert_matches_type(ReportRetrieveResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Y2) -> None:
        report = client.reports.retrieve(
            report_id="rpt_0123456789abcdef01234567",
            format="markdown",
            include="include",
            view="agent",
        )
        assert_matches_type(ReportRetrieveResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Y2) -> None:
        response = client.reports.with_raw_response.retrieve(
            report_id="rpt_0123456789abcdef01234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportRetrieveResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Y2) -> None:
        with client.reports.with_streaming_response.retrieve(
            report_id="rpt_0123456789abcdef01234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportRetrieveResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Y2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            client.reports.with_raw_response.retrieve(
                report_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Y2) -> None:
        report = client.reports.list()
        assert_matches_type(ReportListResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Y2) -> None:
        report = client.reports.list(
            cursor="cursor",
            format="json",
            limit=1,
            profile_id="prf_0123456789abcdef01234567",
        )
        assert_matches_type(ReportListResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Y2) -> None:
        response = client.reports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportListResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Y2) -> None:
        with client.reports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportListResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_audio(self, client: Y2) -> None:
        report = client.reports.retrieve_audio(
            report_id="rpt_210b9798eb53baa4e69d31c1",
        )
        assert_matches_type(ReportRetrieveAudioResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_audio_with_all_params(self, client: Y2) -> None:
        report = client.reports.retrieve_audio(
            report_id="rpt_210b9798eb53baa4e69d31c1",
            redirect=True,
        )
        assert_matches_type(ReportRetrieveAudioResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_audio(self, client: Y2) -> None:
        response = client.reports.with_raw_response.retrieve_audio(
            report_id="rpt_210b9798eb53baa4e69d31c1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = response.parse()
        assert_matches_type(ReportRetrieveAudioResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_audio(self, client: Y2) -> None:
        with client.reports.with_streaming_response.retrieve_audio(
            report_id="rpt_210b9798eb53baa4e69d31c1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = response.parse()
            assert_matches_type(ReportRetrieveAudioResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_audio(self, client: Y2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            client.reports.with_raw_response.retrieve_audio(
                report_id="",
            )


class TestAsyncReports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncY2) -> None:
        report = await async_client.reports.retrieve(
            report_id="rpt_0123456789abcdef01234567",
        )
        assert_matches_type(ReportRetrieveResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncY2) -> None:
        report = await async_client.reports.retrieve(
            report_id="rpt_0123456789abcdef01234567",
            format="markdown",
            include="include",
            view="agent",
        )
        assert_matches_type(ReportRetrieveResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncY2) -> None:
        response = await async_client.reports.with_raw_response.retrieve(
            report_id="rpt_0123456789abcdef01234567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportRetrieveResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncY2) -> None:
        async with async_client.reports.with_streaming_response.retrieve(
            report_id="rpt_0123456789abcdef01234567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportRetrieveResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncY2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            await async_client.reports.with_raw_response.retrieve(
                report_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncY2) -> None:
        report = await async_client.reports.list()
        assert_matches_type(ReportListResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncY2) -> None:
        report = await async_client.reports.list(
            cursor="cursor",
            format="json",
            limit=1,
            profile_id="prf_0123456789abcdef01234567",
        )
        assert_matches_type(ReportListResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncY2) -> None:
        response = await async_client.reports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportListResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncY2) -> None:
        async with async_client.reports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportListResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_audio(self, async_client: AsyncY2) -> None:
        report = await async_client.reports.retrieve_audio(
            report_id="rpt_210b9798eb53baa4e69d31c1",
        )
        assert_matches_type(ReportRetrieveAudioResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_audio_with_all_params(self, async_client: AsyncY2) -> None:
        report = await async_client.reports.retrieve_audio(
            report_id="rpt_210b9798eb53baa4e69d31c1",
            redirect=True,
        )
        assert_matches_type(ReportRetrieveAudioResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_audio(self, async_client: AsyncY2) -> None:
        response = await async_client.reports.with_raw_response.retrieve_audio(
            report_id="rpt_210b9798eb53baa4e69d31c1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report = await response.parse()
        assert_matches_type(ReportRetrieveAudioResponse, report, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_audio(self, async_client: AsyncY2) -> None:
        async with async_client.reports.with_streaming_response.retrieve_audio(
            report_id="rpt_210b9798eb53baa4e69d31c1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report = await response.parse()
            assert_matches_type(ReportRetrieveAudioResponse, report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_audio(self, async_client: AsyncY2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            await async_client.reports.with_raw_response.retrieve_audio(
                report_id="",
            )
