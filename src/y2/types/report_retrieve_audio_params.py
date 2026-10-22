# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ReportRetrieveAudioParams"]


class ReportRetrieveAudioParams(TypedDict, total=False):
    redirect: bool
    """When true, redirects with `302` to the audio CDN URL"""
