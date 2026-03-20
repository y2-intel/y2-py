# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import subscription_update_delivery_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.subscription_update_delivery_response import SubscriptionUpdateDeliveryResponse

__all__ = ["SubscriptionsResource", "AsyncSubscriptionsResource"]


class SubscriptionsResource(SyncAPIResource):
    """Subscription delivery management"""

    @cached_property
    def with_raw_response(self) -> SubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/y2-intel/y2-py#accessing-raw-response-data-eg-headers
        """
        return SubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/y2-intel/y2-py#with_streaming_response
        """
        return SubscriptionsResourceWithStreamingResponse(self)

    def update_delivery(
        self,
        subscription_id: str,
        *,
        delivery_method: Literal["email", "sms", "webhook", "both_email_sms"],
        webhook_config_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionUpdateDeliveryResponse:
        """Changes the delivery method for a subscription.

        When setting to `webhook`, a
        valid `webhookConfigId` must be provided. The webhook must be active.

        Args:
          delivery_method: Subscription delivery method

          webhook_config_id: Required when deliveryMethod is "webhook"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return self._patch(
            path_template("/subscriptions/{subscription_id}/delivery", subscription_id=subscription_id),
            body=maybe_transform(
                {
                    "delivery_method": delivery_method,
                    "webhook_config_id": webhook_config_id,
                },
                subscription_update_delivery_params.SubscriptionUpdateDeliveryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionUpdateDeliveryResponse,
        )


class AsyncSubscriptionsResource(AsyncAPIResource):
    """Subscription delivery management"""

    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/y2-intel/y2-py#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/y2-intel/y2-py#with_streaming_response
        """
        return AsyncSubscriptionsResourceWithStreamingResponse(self)

    async def update_delivery(
        self,
        subscription_id: str,
        *,
        delivery_method: Literal["email", "sms", "webhook", "both_email_sms"],
        webhook_config_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionUpdateDeliveryResponse:
        """Changes the delivery method for a subscription.

        When setting to `webhook`, a
        valid `webhookConfigId` must be provided. The webhook must be active.

        Args:
          delivery_method: Subscription delivery method

          webhook_config_id: Required when deliveryMethod is "webhook"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscription_id:
            raise ValueError(f"Expected a non-empty value for `subscription_id` but received {subscription_id!r}")
        return await self._patch(
            path_template("/subscriptions/{subscription_id}/delivery", subscription_id=subscription_id),
            body=await async_maybe_transform(
                {
                    "delivery_method": delivery_method,
                    "webhook_config_id": webhook_config_id,
                },
                subscription_update_delivery_params.SubscriptionUpdateDeliveryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionUpdateDeliveryResponse,
        )


class SubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.update_delivery = to_raw_response_wrapper(
            subscriptions.update_delivery,
        )


class AsyncSubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.update_delivery = async_to_raw_response_wrapper(
            subscriptions.update_delivery,
        )


class SubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.update_delivery = to_streamed_response_wrapper(
            subscriptions.update_delivery,
        )


class AsyncSubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.update_delivery = async_to_streamed_response_wrapper(
            subscriptions.update_delivery,
        )
