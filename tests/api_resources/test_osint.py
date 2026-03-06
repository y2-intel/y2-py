# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from y2 import Y2, AsyncY2
from y2.types import (
    OsintMapEventsResponse,
    OsintListEventsResponse,
    OsintListVesselsResponse,
    OsintListAircraftResponse,
    OsintGetGpsJammingZonesResponse,
    OsintGetMilitaryPostureResponse,
    OsintGetConflictIndicatorsResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOsint:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_conflict_indicators(self, client: Y2) -> None:
        osint = client.osint.get_conflict_indicators()
        assert_matches_type(OsintGetConflictIndicatorsResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_conflict_indicators_with_all_params(self, client: Y2) -> None:
        osint = client.osint.get_conflict_indicators(
            category="seismic",
            limit=1,
            region="mena",
        )
        assert_matches_type(OsintGetConflictIndicatorsResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_conflict_indicators(self, client: Y2) -> None:
        response = client.osint.with_raw_response.get_conflict_indicators()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        osint = response.parse()
        assert_matches_type(OsintGetConflictIndicatorsResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_conflict_indicators(self, client: Y2) -> None:
        with client.osint.with_streaming_response.get_conflict_indicators() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            osint = response.parse()
            assert_matches_type(OsintGetConflictIndicatorsResponse, osint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_gps_jamming_zones(self, client: Y2) -> None:
        osint = client.osint.get_gps_jamming_zones()
        assert_matches_type(OsintGetGpsJammingZonesResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_gps_jamming_zones_with_all_params(self, client: Y2) -> None:
        osint = client.osint.get_gps_jamming_zones(
            limit=1,
            severity="low",
        )
        assert_matches_type(OsintGetGpsJammingZonesResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_gps_jamming_zones(self, client: Y2) -> None:
        response = client.osint.with_raw_response.get_gps_jamming_zones()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        osint = response.parse()
        assert_matches_type(OsintGetGpsJammingZonesResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_gps_jamming_zones(self, client: Y2) -> None:
        with client.osint.with_streaming_response.get_gps_jamming_zones() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            osint = response.parse()
            assert_matches_type(OsintGetGpsJammingZonesResponse, osint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_military_posture(self, client: Y2) -> None:
        osint = client.osint.get_military_posture()
        assert_matches_type(OsintGetMilitaryPostureResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_military_posture_with_all_params(self, client: Y2) -> None:
        osint = client.osint.get_military_posture(
            limit=1,
        )
        assert_matches_type(OsintGetMilitaryPostureResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_military_posture(self, client: Y2) -> None:
        response = client.osint.with_raw_response.get_military_posture()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        osint = response.parse()
        assert_matches_type(OsintGetMilitaryPostureResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_military_posture(self, client: Y2) -> None:
        with client.osint.with_streaming_response.get_military_posture() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            osint = response.parse()
            assert_matches_type(OsintGetMilitaryPostureResponse, osint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_aircraft(self, client: Y2) -> None:
        osint = client.osint.list_aircraft()
        assert_matches_type(OsintListAircraftResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_aircraft_with_all_params(self, client: Y2) -> None:
        osint = client.osint.list_aircraft(
            limit=1,
            theater="theater",
        )
        assert_matches_type(OsintListAircraftResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_aircraft(self, client: Y2) -> None:
        response = client.osint.with_raw_response.list_aircraft()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        osint = response.parse()
        assert_matches_type(OsintListAircraftResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_aircraft(self, client: Y2) -> None:
        with client.osint.with_streaming_response.list_aircraft() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            osint = response.parse()
            assert_matches_type(OsintListAircraftResponse, osint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_events(self, client: Y2) -> None:
        osint = client.osint.list_events()
        assert_matches_type(OsintListEventsResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_events_with_all_params(self, client: Y2) -> None:
        osint = client.osint.list_events(
            category="seismic",
            limit=1,
            severity="low",
        )
        assert_matches_type(OsintListEventsResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_events(self, client: Y2) -> None:
        response = client.osint.with_raw_response.list_events()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        osint = response.parse()
        assert_matches_type(OsintListEventsResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_events(self, client: Y2) -> None:
        with client.osint.with_streaming_response.list_events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            osint = response.parse()
            assert_matches_type(OsintListEventsResponse, osint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_vessels(self, client: Y2) -> None:
        osint = client.osint.list_vessels()
        assert_matches_type(OsintListVesselsResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_vessels_with_all_params(self, client: Y2) -> None:
        osint = client.osint.list_vessels(
            limit=1,
            region="region",
        )
        assert_matches_type(OsintListVesselsResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_vessels(self, client: Y2) -> None:
        response = client.osint.with_raw_response.list_vessels()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        osint = response.parse()
        assert_matches_type(OsintListVesselsResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_vessels(self, client: Y2) -> None:
        with client.osint.with_streaming_response.list_vessels() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            osint = response.parse()
            assert_matches_type(OsintListVesselsResponse, osint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_map_events(self, client: Y2) -> None:
        osint = client.osint.map_events()
        assert_matches_type(OsintMapEventsResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_map_events_with_all_params(self, client: Y2) -> None:
        osint = client.osint.map_events(
            limit=1,
            region="mena",
        )
        assert_matches_type(OsintMapEventsResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_map_events(self, client: Y2) -> None:
        response = client.osint.with_raw_response.map_events()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        osint = response.parse()
        assert_matches_type(OsintMapEventsResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_map_events(self, client: Y2) -> None:
        with client.osint.with_streaming_response.map_events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            osint = response.parse()
            assert_matches_type(OsintMapEventsResponse, osint, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOsint:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_conflict_indicators(self, async_client: AsyncY2) -> None:
        osint = await async_client.osint.get_conflict_indicators()
        assert_matches_type(OsintGetConflictIndicatorsResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_conflict_indicators_with_all_params(self, async_client: AsyncY2) -> None:
        osint = await async_client.osint.get_conflict_indicators(
            category="seismic",
            limit=1,
            region="mena",
        )
        assert_matches_type(OsintGetConflictIndicatorsResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_conflict_indicators(self, async_client: AsyncY2) -> None:
        response = await async_client.osint.with_raw_response.get_conflict_indicators()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        osint = await response.parse()
        assert_matches_type(OsintGetConflictIndicatorsResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_conflict_indicators(self, async_client: AsyncY2) -> None:
        async with async_client.osint.with_streaming_response.get_conflict_indicators() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            osint = await response.parse()
            assert_matches_type(OsintGetConflictIndicatorsResponse, osint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_gps_jamming_zones(self, async_client: AsyncY2) -> None:
        osint = await async_client.osint.get_gps_jamming_zones()
        assert_matches_type(OsintGetGpsJammingZonesResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_gps_jamming_zones_with_all_params(self, async_client: AsyncY2) -> None:
        osint = await async_client.osint.get_gps_jamming_zones(
            limit=1,
            severity="low",
        )
        assert_matches_type(OsintGetGpsJammingZonesResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_gps_jamming_zones(self, async_client: AsyncY2) -> None:
        response = await async_client.osint.with_raw_response.get_gps_jamming_zones()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        osint = await response.parse()
        assert_matches_type(OsintGetGpsJammingZonesResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_gps_jamming_zones(self, async_client: AsyncY2) -> None:
        async with async_client.osint.with_streaming_response.get_gps_jamming_zones() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            osint = await response.parse()
            assert_matches_type(OsintGetGpsJammingZonesResponse, osint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_military_posture(self, async_client: AsyncY2) -> None:
        osint = await async_client.osint.get_military_posture()
        assert_matches_type(OsintGetMilitaryPostureResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_military_posture_with_all_params(self, async_client: AsyncY2) -> None:
        osint = await async_client.osint.get_military_posture(
            limit=1,
        )
        assert_matches_type(OsintGetMilitaryPostureResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_military_posture(self, async_client: AsyncY2) -> None:
        response = await async_client.osint.with_raw_response.get_military_posture()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        osint = await response.parse()
        assert_matches_type(OsintGetMilitaryPostureResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_military_posture(self, async_client: AsyncY2) -> None:
        async with async_client.osint.with_streaming_response.get_military_posture() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            osint = await response.parse()
            assert_matches_type(OsintGetMilitaryPostureResponse, osint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_aircraft(self, async_client: AsyncY2) -> None:
        osint = await async_client.osint.list_aircraft()
        assert_matches_type(OsintListAircraftResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_aircraft_with_all_params(self, async_client: AsyncY2) -> None:
        osint = await async_client.osint.list_aircraft(
            limit=1,
            theater="theater",
        )
        assert_matches_type(OsintListAircraftResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_aircraft(self, async_client: AsyncY2) -> None:
        response = await async_client.osint.with_raw_response.list_aircraft()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        osint = await response.parse()
        assert_matches_type(OsintListAircraftResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_aircraft(self, async_client: AsyncY2) -> None:
        async with async_client.osint.with_streaming_response.list_aircraft() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            osint = await response.parse()
            assert_matches_type(OsintListAircraftResponse, osint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_events(self, async_client: AsyncY2) -> None:
        osint = await async_client.osint.list_events()
        assert_matches_type(OsintListEventsResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_events_with_all_params(self, async_client: AsyncY2) -> None:
        osint = await async_client.osint.list_events(
            category="seismic",
            limit=1,
            severity="low",
        )
        assert_matches_type(OsintListEventsResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_events(self, async_client: AsyncY2) -> None:
        response = await async_client.osint.with_raw_response.list_events()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        osint = await response.parse()
        assert_matches_type(OsintListEventsResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_events(self, async_client: AsyncY2) -> None:
        async with async_client.osint.with_streaming_response.list_events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            osint = await response.parse()
            assert_matches_type(OsintListEventsResponse, osint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_vessels(self, async_client: AsyncY2) -> None:
        osint = await async_client.osint.list_vessels()
        assert_matches_type(OsintListVesselsResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_vessels_with_all_params(self, async_client: AsyncY2) -> None:
        osint = await async_client.osint.list_vessels(
            limit=1,
            region="region",
        )
        assert_matches_type(OsintListVesselsResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_vessels(self, async_client: AsyncY2) -> None:
        response = await async_client.osint.with_raw_response.list_vessels()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        osint = await response.parse()
        assert_matches_type(OsintListVesselsResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_vessels(self, async_client: AsyncY2) -> None:
        async with async_client.osint.with_streaming_response.list_vessels() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            osint = await response.parse()
            assert_matches_type(OsintListVesselsResponse, osint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_map_events(self, async_client: AsyncY2) -> None:
        osint = await async_client.osint.map_events()
        assert_matches_type(OsintMapEventsResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_map_events_with_all_params(self, async_client: AsyncY2) -> None:
        osint = await async_client.osint.map_events(
            limit=1,
            region="mena",
        )
        assert_matches_type(OsintMapEventsResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_map_events(self, async_client: AsyncY2) -> None:
        response = await async_client.osint.with_raw_response.map_events()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        osint = await response.parse()
        assert_matches_type(OsintMapEventsResponse, osint, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_map_events(self, async_client: AsyncY2) -> None:
        async with async_client.osint.with_streaming_response.map_events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            osint = await response.parse()
            assert_matches_type(OsintMapEventsResponse, osint, path=["response"])

        assert cast(Any, response.is_closed) is True
