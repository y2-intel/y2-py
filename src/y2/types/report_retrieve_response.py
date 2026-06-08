# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .audio_metadata import AudioMetadata

__all__ = [
    "ReportRetrieveResponse",
    "Data",
    "DataContent",
    "DataIntelligence",
    "DataIntelligenceOntologyGraph",
    "DataIntelligenceOntologyGraphEdge",
    "DataIntelligenceOntologyGraphIncident",
    "DataIntelligenceOntologyGraphNode",
    "DataIntelligenceSigint",
    "DataIntelligenceSigintSignal",
    "DataIntelligenceSigintSignalSubject",
    "DataMetadata",
    "DataMetadataFreshnessMetadata",
    "DataMetadataRecursionMetadata",
]


class DataContent(BaseModel):
    html: Optional[str] = None
    """Full HTML content"""

    summary: Optional[str] = None
    """SMS-friendly summary"""


class DataIntelligenceOntologyGraphEdge(BaseModel):
    id: str
    """Report-local graph edge ID"""

    confidence: float

    from_: str = FieldInfo(alias="from")
    """Source report-local node ID"""

    from_label: str = FieldInfo(alias="fromLabel")

    kind: str

    to: str
    """Target report-local node ID"""

    to_label: str = FieldInfo(alias="toLabel")

    evidence_url: Optional[str] = FieldInfo(alias="evidenceUrl", default=None)


class DataIntelligenceOntologyGraphIncident(BaseModel):
    id: str
    """Report-local incident anchor ID"""

    category: str

    cited_urls: List[str] = FieldInfo(alias="citedUrls")

    event_time: int = FieldInfo(alias="eventTime")

    involved_node_ids: List[str] = FieldInfo(alias="involvedNodeIds")

    severity: str

    title: str

    incident_id: Optional[str] = FieldInfo(alias="incidentId", default=None)
    """Linked ontology incident ID, when resolved"""


class DataIntelligenceOntologyGraphNode(BaseModel):
    id: str
    """Report-local graph node ID"""

    evidence_urls: List[str] = FieldInfo(alias="evidenceUrls")

    kind: str

    label: str

    entity_id: Optional[str] = FieldInfo(alias="entityId", default=None)
    """Linked ontology entity ID, when resolved"""

    summary: Optional[str] = None


class DataIntelligenceOntologyGraph(BaseModel):
    citations: List[str]

    edges: List[DataIntelligenceOntologyGraphEdge]

    generated_at: int = FieldInfo(alias="generatedAt")
    """Graph extraction timestamp in milliseconds"""

    incidents: List[DataIntelligenceOntologyGraphIncident]

    nodes: List[DataIntelligenceOntologyGraphNode]

    source: Literal["y2_report_graph"]

    summary: str

    model: Optional[str] = None

    prompt_version: Optional[str] = FieldInfo(alias="promptVersion", default=None)

    topic: Optional[str] = None


class DataIntelligenceSigintSignalSubject(BaseModel):
    kind: Literal[
        "person",
        "organization",
        "country",
        "region",
        "vessel",
        "aircraft",
        "facility",
        "asset",
        "indicator",
        "cve",
        "malware_family",
        "threat_actor",
        "vendor",
        "software",
        "ai_model",
        "api_service",
        "protocol",
    ]

    label: str
    """Human-readable subject label"""

    normalized_key: str = FieldInfo(alias="normalizedKey")
    """Stable ontology subject key used for filtering"""

    entity_id: Optional[str] = FieldInfo(alias="entityId", default=None)
    """Linked ontology entity ID when resolved"""


class DataIntelligenceSigintSignal(BaseModel):
    action_type: Literal[
        "invest", "patch", "upgrade", "strategy", "hedge", "monitor", "mitigate", "escalate", "defer", "allocate"
    ] = FieldInfo(alias="actionType")

    confidence: float

    decision: str
    """Candidate action or decision hypothesis"""

    domain: Literal[
        "cyber", "markets", "geopolitical", "operational", "supply_chain", "policy", "military", "technology", "other"
    ]

    entity_names: List[str] = FieldInfo(alias="entityNames")

    evidence_urls: List[str] = FieldInfo(alias="evidenceUrls")

    inference_type: Literal["observed", "inferred", "speculative"] = FieldInfo(alias="inferenceType")

    justification: str
    """Evidence-grounded rationale"""

    priority: Literal["low", "medium", "high", "critical"]

    signal: str
    """Concise statement of the inferred signal"""

    time_horizon: Literal["immediate", "near_term", "mid_term", "long_term"] = FieldInfo(alias="timeHorizon")

    title: str
    """Short signal title"""

    subjects: Optional[List[DataIntelligenceSigintSignalSubject]] = None
    """Ontology-aligned signal subjects"""

    tags: Optional[List[str]] = None
    """Lowercase filtering tokens for domains, actions, priorities, and subjects"""


class DataIntelligenceSigint(BaseModel):
    signals: List[DataIntelligenceSigintSignal]

    generated_at: Optional[int] = FieldInfo(alias="generatedAt", default=None)
    """Signal extraction timestamp in milliseconds"""

    summary: Optional[str] = None
    """One-sentence summary of the dominant emergent signal set"""


class DataIntelligence(BaseModel):
    ontology_graph: Optional[DataIntelligenceOntologyGraph] = FieldInfo(alias="ontologyGraph", default=None)

    sigint: Optional[DataIntelligenceSigint] = None


class DataMetadataFreshnessMetadata(BaseModel):
    """Source freshness validation results"""

    accessible_links: Optional[int] = FieldInfo(alias="accessibleLinks", default=None)

    average_age_ms: Optional[int] = FieldInfo(alias="averageAgeMs", default=None)
    """Average source age in milliseconds"""

    freshness_score: Optional[float] = FieldInfo(alias="freshnessScore", default=None)
    """Overall freshness score (higher = fresher)"""

    stale_sources_count: Optional[int] = FieldInfo(alias="staleSourcesCount", default=None)

    total_links: Optional[int] = FieldInfo(alias="totalLinks", default=None)

    validated_at: Optional[int] = FieldInfo(alias="validatedAt", default=None)


class DataMetadataRecursionMetadata(BaseModel):
    """Metadata about recursive research execution"""

    depth: Optional[int] = None
    """Recursion depth achieved (0 = standard report)"""

    fallback_reason: Optional[str] = FieldInfo(alias="fallbackReason", default=None)
    """Reason if fallback to standard generation occurred"""

    layers_processed: Optional[int] = FieldInfo(alias="layersProcessed", default=None)

    strategy: Optional[Literal["breadth-first", "depth-first", "hybrid"]] = None

    subtopics_generated: Optional[List[str]] = FieldInfo(alias="subtopicsGenerated", default=None)

    total_sources_collected: Optional[int] = FieldInfo(alias="totalSourcesCollected", default=None)

    total_time_ms: Optional[int] = FieldInfo(alias="totalTimeMs", default=None)

    unique_sources_aggregated: Optional[int] = FieldInfo(alias="uniqueSourcesAggregated", default=None)


class DataMetadata(BaseModel):
    freshness_metadata: Optional[DataMetadataFreshnessMetadata] = FieldInfo(alias="freshnessMetadata", default=None)
    """Source freshness validation results"""

    model: Optional[str] = None

    recursion_metadata: Optional[DataMetadataRecursionMetadata] = FieldInfo(alias="recursionMetadata", default=None)
    """Metadata about recursive research execution"""

    total_cost: Optional[float] = FieldInfo(alias="totalCost", default=None)


class Data(BaseModel):
    id: str

    content: DataContent

    generated_at: int = FieldInfo(alias="generatedAt")

    generated_at_iso: datetime = FieldInfo(alias="generatedAtISO")

    profile_id: str = FieldInfo(alias="profileId")

    audio: Optional[AudioMetadata] = None

    intelligence: Optional[DataIntelligence] = None

    metadata: Optional[DataMetadata] = None

    profile_name: Optional[str] = FieldInfo(alias="profileName", default=None)

    profile_topic: Optional[str] = FieldInfo(alias="profileTopic", default=None)

    sources: Optional[List[str]] = None

    topic: Optional[str] = None


class ReportRetrieveResponse(BaseModel):
    data: Data
