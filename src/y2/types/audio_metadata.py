# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AudioMetadata"]


class AudioMetadata(BaseModel):
    duration: Optional[float] = None
    """Duration in seconds"""

    duration_formatted: Optional[str] = FieldInfo(alias="durationFormatted", default=None)
    """Duration as HH:MM:SS"""

    duration_seconds: Optional[float] = FieldInfo(alias="durationSeconds", default=None)
    """Canonical duration in seconds."""

    file_size_bytes: Optional[int] = FieldInfo(alias="fileSizeBytes", default=None)
    """File size in bytes."""

    format: Optional[Literal["mp3"]] = None

    mime_type: Optional[Literal["audio/mpeg"]] = FieldInfo(alias="mimeType", default=None)

    url: Optional[str] = None
    """CDN URL for audio file"""
