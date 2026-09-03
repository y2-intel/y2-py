# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ReportRetrieveParams"]


class ReportRetrieveParams(TypedDict, total=False):
    format: Literal["markdown"]
    """Explicit representation override."""

    include: str
    """Comma-separated `content,sources,signals,graph,audio` expansions."""

    view: Literal["agent"]
    """Compact projection optimized for grounded agent context."""
