# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from y2 import Y2, AsyncY2
from y2.types import SubscriptionUpdateDeliveryResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_delivery(self, client: Y2) -> None:
        subscription = client.subscriptions.update_delivery(
            subscription_id="subscriptionId",
            delivery_method="email",
        )
        assert_matches_type(SubscriptionUpdateDeliveryResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_delivery_with_all_params(self, client: Y2) -> None:
        subscription = client.subscriptions.update_delivery(
            subscription_id="subscriptionId",
            delivery_method="email",
            webhook_config_id="webhookConfigId",
        )
        assert_matches_type(SubscriptionUpdateDeliveryResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_delivery(self, client: Y2) -> None:
        response = client.subscriptions.with_raw_response.update_delivery(
            subscription_id="subscriptionId",
            delivery_method="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionUpdateDeliveryResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_delivery(self, client: Y2) -> None:
        with client.subscriptions.with_streaming_response.update_delivery(
            subscription_id="subscriptionId",
            delivery_method="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionUpdateDeliveryResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_delivery(self, client: Y2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.subscriptions.with_raw_response.update_delivery(
                subscription_id="",
                delivery_method="email",
            )


class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_delivery(self, async_client: AsyncY2) -> None:
        subscription = await async_client.subscriptions.update_delivery(
            subscription_id="subscriptionId",
            delivery_method="email",
        )
        assert_matches_type(SubscriptionUpdateDeliveryResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_delivery_with_all_params(self, async_client: AsyncY2) -> None:
        subscription = await async_client.subscriptions.update_delivery(
            subscription_id="subscriptionId",
            delivery_method="email",
            webhook_config_id="webhookConfigId",
        )
        assert_matches_type(SubscriptionUpdateDeliveryResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_delivery(self, async_client: AsyncY2) -> None:
        response = await async_client.subscriptions.with_raw_response.update_delivery(
            subscription_id="subscriptionId",
            delivery_method="email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionUpdateDeliveryResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_delivery(self, async_client: AsyncY2) -> None:
        async with async_client.subscriptions.with_streaming_response.update_delivery(
            subscription_id="subscriptionId",
            delivery_method="email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionUpdateDeliveryResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_delivery(self, async_client: AsyncY2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.subscriptions.with_raw_response.update_delivery(
                subscription_id="",
                delivery_method="email",
            )
