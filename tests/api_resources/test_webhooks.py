# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from y2 import Y2, AsyncY2
from y2.types import (
    WebhookListResponse,
    WebhookTestResponse,
    WebhookCreateResponse,
    WebhookUpdateResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Y2) -> None:
        webhook = client.webhooks.create(
            name="My Webhook",
            url="https://example.com/webhook",
        )
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Y2) -> None:
        webhook = client.webhooks.create(
            name="My Webhook",
            url="https://example.com/webhook",
            headers={"foo": "string"},
            secret="secret",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Y2) -> None:
        response = client.webhooks.with_raw_response.create(
            name="My Webhook",
            url="https://example.com/webhook",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Y2) -> None:
        with client.webhooks.with_streaming_response.create(
            name="My Webhook",
            url="https://example.com/webhook",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Y2) -> None:
        webhook = client.webhooks.update(
            webhook_id="whk_210b9798eb53baa4e69d31c1",
            name="My Webhook",
            url="https://example.com/webhook",
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Y2) -> None:
        webhook = client.webhooks.update(
            webhook_id="whk_210b9798eb53baa4e69d31c1",
            name="My Webhook",
            url="https://example.com/webhook",
            headers={"foo": "string"},
            is_active=True,
            secret="secret",
            if_match="If-Match",
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Y2) -> None:
        response = client.webhooks.with_raw_response.update(
            webhook_id="whk_210b9798eb53baa4e69d31c1",
            name="My Webhook",
            url="https://example.com/webhook",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Y2) -> None:
        with client.webhooks.with_streaming_response.update(
            webhook_id="whk_210b9798eb53baa4e69d31c1",
            name="My Webhook",
            url="https://example.com/webhook",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Y2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.webhooks.with_raw_response.update(
                webhook_id="",
                name="My Webhook",
                url="https://example.com/webhook",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Y2) -> None:
        webhook = client.webhooks.list()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Y2) -> None:
        response = client.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Y2) -> None:
        with client.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Y2) -> None:
        webhook = client.webhooks.delete(
            webhook_id="whk_210b9798eb53baa4e69d31c1",
        )
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Y2) -> None:
        webhook = client.webhooks.delete(
            webhook_id="whk_210b9798eb53baa4e69d31c1",
            if_match="If-Match",
        )
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Y2) -> None:
        response = client.webhooks.with_raw_response.delete(
            webhook_id="whk_210b9798eb53baa4e69d31c1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Y2) -> None:
        with client.webhooks.with_streaming_response.delete(
            webhook_id="whk_210b9798eb53baa4e69d31c1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Y2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.webhooks.with_raw_response.delete(
                webhook_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test(self, client: Y2) -> None:
        webhook = client.webhooks.test(
            "whk_210b9798eb53baa4e69d31c1",
        )
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_test(self, client: Y2) -> None:
        response = client.webhooks.with_raw_response.test(
            "whk_210b9798eb53baa4e69d31c1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_test(self, client: Y2) -> None:
        with client.webhooks.with_streaming_response.test(
            "whk_210b9798eb53baa4e69d31c1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookTestResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_test(self, client: Y2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.webhooks.with_raw_response.test(
                "",
            )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncY2) -> None:
        webhook = await async_client.webhooks.create(
            name="My Webhook",
            url="https://example.com/webhook",
        )
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncY2) -> None:
        webhook = await async_client.webhooks.create(
            name="My Webhook",
            url="https://example.com/webhook",
            headers={"foo": "string"},
            secret="secret",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncY2) -> None:
        response = await async_client.webhooks.with_raw_response.create(
            name="My Webhook",
            url="https://example.com/webhook",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncY2) -> None:
        async with async_client.webhooks.with_streaming_response.create(
            name="My Webhook",
            url="https://example.com/webhook",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookCreateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncY2) -> None:
        webhook = await async_client.webhooks.update(
            webhook_id="whk_210b9798eb53baa4e69d31c1",
            name="My Webhook",
            url="https://example.com/webhook",
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncY2) -> None:
        webhook = await async_client.webhooks.update(
            webhook_id="whk_210b9798eb53baa4e69d31c1",
            name="My Webhook",
            url="https://example.com/webhook",
            headers={"foo": "string"},
            is_active=True,
            secret="secret",
            if_match="If-Match",
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncY2) -> None:
        response = await async_client.webhooks.with_raw_response.update(
            webhook_id="whk_210b9798eb53baa4e69d31c1",
            name="My Webhook",
            url="https://example.com/webhook",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncY2) -> None:
        async with async_client.webhooks.with_streaming_response.update(
            webhook_id="whk_210b9798eb53baa4e69d31c1",
            name="My Webhook",
            url="https://example.com/webhook",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncY2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.webhooks.with_raw_response.update(
                webhook_id="",
                name="My Webhook",
                url="https://example.com/webhook",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncY2) -> None:
        webhook = await async_client.webhooks.list()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncY2) -> None:
        response = await async_client.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncY2) -> None:
        async with async_client.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncY2) -> None:
        webhook = await async_client.webhooks.delete(
            webhook_id="whk_210b9798eb53baa4e69d31c1",
        )
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncY2) -> None:
        webhook = await async_client.webhooks.delete(
            webhook_id="whk_210b9798eb53baa4e69d31c1",
            if_match="If-Match",
        )
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncY2) -> None:
        response = await async_client.webhooks.with_raw_response.delete(
            webhook_id="whk_210b9798eb53baa4e69d31c1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncY2) -> None:
        async with async_client.webhooks.with_streaming_response.delete(
            webhook_id="whk_210b9798eb53baa4e69d31c1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncY2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.webhooks.with_raw_response.delete(
                webhook_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test(self, async_client: AsyncY2) -> None:
        webhook = await async_client.webhooks.test(
            "whk_210b9798eb53baa4e69d31c1",
        )
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_test(self, async_client: AsyncY2) -> None:
        response = await async_client.webhooks.with_raw_response.test(
            "whk_210b9798eb53baa4e69d31c1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_test(self, async_client: AsyncY2) -> None:
        async with async_client.webhooks.with_streaming_response.test(
            "whk_210b9798eb53baa4e69d31c1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookTestResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_test(self, async_client: AsyncY2) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.webhooks.with_raw_response.test(
                "",
            )
