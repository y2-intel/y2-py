# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .audio_metadata import AudioMetadata

__all__ = [
    "ReportRetrieveResponse",
    "Data",
    "DataAudio",
    "DataIntelligence",
    "DataIntelligenceGraph",
    "DataContent",
    "DataGraph",
    "DataGraphEdge",
    "DataGraphEdgeSource",
    "DataGraphIncident",
    "DataGraphIncidentSource",
    "DataGraphNode",
    "DataGraphNodeSource",
    "DataGraphSource",
    "DataProfile",
    "DataSignal",
    "DataSignalSource",
    "DataSignalSubject",
    "DataSource",
]


class DataAudio(BaseModel):
    duration_seconds: Optional[float] = FieldInfo(alias="durationSeconds", default=None)

    media_type: Optional[str] = FieldInfo(alias="mediaType", default=None)

    status: Literal["available", "unavailable"]


class DataIntelligenceGraph(BaseModel):
    edge_count: int = FieldInfo(alias="edgeCount")

    incident_count: int = FieldInfo(alias="incidentCount")

    node_count: int = FieldInfo(alias="nodeCount")


class DataIntelligence(BaseModel):
    graph: Optional[DataIntelligenceGraph] = None

    signal_count: int = FieldInfo(alias="signalCount")


class DataContent(BaseModel):
    markdown: str

    media_type: Literal["text/markdown"] = FieldInfo(alias="mediaType")


class DataGraphEdgeSource(BaseModel):
    id: str

    url: str


class DataGraphEdge(BaseModel):
    id: str

    confidence: float

    from_: str = FieldInfo(alias="from")

    source: Optional[DataGraphEdgeSource] = None

    to: str

    type: str


class DataGraphIncidentSource(BaseModel):
    id: str

    url: str


class DataGraphIncident(BaseModel):
    id: str

    category: str

    entity_ids: List[str] = FieldInfo(alias="entityIds")

    occurred_at: datetime = FieldInfo(alias="occurredAt")

    severity: str

    sources: List[DataGraphIncidentSource]

    title: str

    type: Literal["incident"]


class DataGraphNodeSource(BaseModel):
    id: str

    url: str


class DataGraphNode(BaseModel):
    id: str

    kind: str

    label: str

    sources: List[DataGraphNodeSource]

    summary: Optional[str] = None

    type: Literal["entity"]


class DataGraphSource(BaseModel):
    id: str

    url: str


class DataGraph(BaseModel):
    edges: List[DataGraphEdge]

    generated_at: datetime = FieldInfo(alias="generatedAt")

    incidents: List[DataGraphIncident]

    nodes: List[DataGraphNode]

    sources: List[DataGraphSource]

    summary: str


class DataProfile(BaseModel):
    id: str

    name: Optional[str] = None

    topic: Optional[str] = None


class DataSignalSource(BaseModel):
    id: str

    url: str


class DataSignalSubject(BaseModel):
    entity_id: Optional[str] = FieldInfo(alias="entityId", default=None)

    key: str

    kind: str

    label: str


class DataSignal(BaseModel):
    action_type: str = FieldInfo(alias="actionType")

    confidence: float

    decision: str

    domain: str

    inference_type: str = FieldInfo(alias="inferenceType")

    justification: str

    priority: str

    signal: str

    sources: List[DataSignalSource]

    subjects: List[DataSignalSubject]

    tags: List[str]

    time_horizon: str = FieldInfo(alias="timeHorizon")

    title: str


class DataSource(BaseModel):
    id: str

    language: Optional[str] = None

    published_at: Optional[datetime] = FieldInfo(alias="publishedAt", default=None)

    publisher: Optional[str] = None

    retrieved_at: datetime = FieldInfo(alias="retrievedAt")

    source_type: str = FieldInfo(alias="sourceType")

    title: Optional[str] = None

    url: str


class Data(BaseModel):
    id: str

    audio: DataAudio

    generated_at: datetime = FieldInfo(alias="generatedAt")

    intelligence: DataIntelligence

    language: str

    links: Dict[str, Optional[str]]

    profile_id: str = FieldInfo(alias="profileId")

    published_at: datetime = FieldInfo(alias="publishedAt")

    status: Literal["published"]

    summary: Optional[str] = None

    topic: Optional[str] = None

    type: Literal["report"]

    audio_representation: Optional[AudioMetadata] = FieldInfo(alias="audioRepresentation", default=None)

    content: Optional[DataContent] = None

    graph: Optional[DataGraph] = None

    profile: Optional[DataProfile] = None

    signals: Optional[List[DataSignal]] = None

    sources: Optional[List[DataSource]] = None


class ReportRetrieveResponse(BaseModel):
    data: Data
