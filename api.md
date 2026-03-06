# Reports

Types:

```python
from y2.types import (
    AudioMetadata,
    ReportRetrieveResponse,
    ReportListResponse,
    ReportRetrieveAudioResponse,
)
```

Methods:

- <code title="get /reports/{reportId}">client.reports.<a href="./src/y2/resources/reports.py">retrieve</a>(report_id) -> <a href="./src/y2/types/report_retrieve_response.py">ReportRetrieveResponse</a></code>
- <code title="get /reports">client.reports.<a href="./src/y2/resources/reports.py">list</a>(\*\*<a href="src/y2/types/report_list_params.py">params</a>) -> <a href="./src/y2/types/report_list_response.py">ReportListResponse</a></code>
- <code title="get /reports/{reportId}/audio">client.reports.<a href="./src/y2/resources/reports.py">retrieve_audio</a>(report_id, \*\*<a href="src/y2/types/report_retrieve_audio_params.py">params</a>) -> <a href="./src/y2/types/report_retrieve_audio_response.py">ReportRetrieveAudioResponse</a></code>

# Profiles

Types:

```python
from y2.types import (
    ProfileCreateResponse,
    ProfileUpdateResponse,
    ProfileListResponse,
    ProfileDeleteResponse,
    ProfilePartialUpdateResponse,
)
```

Methods:

- <code title="post /profiles">client.profiles.<a href="./src/y2/resources/profiles.py">create</a>(\*\*<a href="src/y2/types/profile_create_params.py">params</a>) -> <a href="./src/y2/types/profile_create_response.py">ProfileCreateResponse</a></code>
- <code title="put /profiles/{profileId}">client.profiles.<a href="./src/y2/resources/profiles.py">update</a>(profile_id, \*\*<a href="src/y2/types/profile_update_params.py">params</a>) -> <a href="./src/y2/types/profile_update_response.py">ProfileUpdateResponse</a></code>
- <code title="get /profiles">client.profiles.<a href="./src/y2/resources/profiles.py">list</a>() -> <a href="./src/y2/types/profile_list_response.py">ProfileListResponse</a></code>
- <code title="delete /profiles/{profileId}">client.profiles.<a href="./src/y2/resources/profiles.py">delete</a>(profile_id) -> <a href="./src/y2/types/profile_delete_response.py">ProfileDeleteResponse</a></code>
- <code title="patch /profiles/{profileId}">client.profiles.<a href="./src/y2/resources/profiles.py">partial_update</a>(profile_id, \*\*<a href="src/y2/types/profile_partial_update_params.py">params</a>) -> <a href="./src/y2/types/profile_partial_update_response.py">ProfilePartialUpdateResponse</a></code>

# News

Types:

```python
from y2.types import (
    TimeframeEnum,
    TopicEnum,
    NewsListResponse,
    NewsGetRecapsResponse,
    NewsListFeedsResponse,
)
```

Methods:

- <code title="get /news">client.news.<a href="./src/y2/resources/news.py">list</a>(\*\*<a href="src/y2/types/news_list_params.py">params</a>) -> <a href="./src/y2/types/news_list_response.py">NewsListResponse</a></code>
- <code title="get /news/recaps">client.news.<a href="./src/y2/resources/news.py">get_recaps</a>(\*\*<a href="src/y2/types/news_get_recaps_params.py">params</a>) -> <a href="./src/y2/types/news_get_recaps_response.py">NewsGetRecapsResponse</a></code>
- <code title="get /news/feeds">client.news.<a href="./src/y2/resources/news.py">list_feeds</a>() -> <a href="./src/y2/types/news_list_feeds_response.py">NewsListFeedsResponse</a></code>

# Webhooks

Types:

```python
from y2.types import (
    WebhookCreateResponse,
    WebhookUpdateResponse,
    WebhookListResponse,
    WebhookDeleteResponse,
    WebhookTestResponse,
)
```

Methods:

- <code title="post /webhooks">client.webhooks.<a href="./src/y2/resources/webhooks.py">create</a>(\*\*<a href="src/y2/types/webhook_create_params.py">params</a>) -> <a href="./src/y2/types/webhook_create_response.py">WebhookCreateResponse</a></code>
- <code title="put /webhooks/{webhookId}">client.webhooks.<a href="./src/y2/resources/webhooks.py">update</a>(webhook_id, \*\*<a href="src/y2/types/webhook_update_params.py">params</a>) -> <a href="./src/y2/types/webhook_update_response.py">WebhookUpdateResponse</a></code>
- <code title="get /webhooks">client.webhooks.<a href="./src/y2/resources/webhooks.py">list</a>() -> <a href="./src/y2/types/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /webhooks/{webhookId}">client.webhooks.<a href="./src/y2/resources/webhooks.py">delete</a>(webhook_id) -> <a href="./src/y2/types/webhook_delete_response.py">WebhookDeleteResponse</a></code>
- <code title="post /webhooks/{webhookId}/test">client.webhooks.<a href="./src/y2/resources/webhooks.py">test</a>(webhook_id) -> <a href="./src/y2/types/webhook_test_response.py">WebhookTestResponse</a></code>

# Subscriptions

Types:

```python
from y2.types import SubscriptionUpdateDeliveryResponse
```

Methods:

- <code title="patch /subscriptions/{subscriptionId}/delivery">client.subscriptions.<a href="./src/y2/resources/subscriptions.py">update_delivery</a>(subscription_id, \*\*<a href="src/y2/types/subscription_update_delivery_params.py">params</a>) -> <a href="./src/y2/types/subscription_update_delivery_response.py">SubscriptionUpdateDeliveryResponse</a></code>

# Osint

Types:

```python
from y2.types import (
    OsintGetConflictIndicatorsResponse,
    OsintGetGpsJammingZonesResponse,
    OsintGetMilitaryPostureResponse,
    OsintListAircraftResponse,
    OsintListEventsResponse,
    OsintListVesselsResponse,
    OsintMapEventsResponse,
)
```

Methods:

- <code title="get /osint/cii">client.osint.<a href="./src/y2/resources/osint/osint.py">get_conflict_indicators</a>(\*\*<a href="src/y2/types/osint_get_conflict_indicators_params.py">params</a>) -> <a href="./src/y2/types/osint_get_conflict_indicators_response.py">OsintGetConflictIndicatorsResponse</a></code>
- <code title="get /osint/gps-jamming">client.osint.<a href="./src/y2/resources/osint/osint.py">get_gps_jamming_zones</a>(\*\*<a href="src/y2/types/osint_get_gps_jamming_zones_params.py">params</a>) -> <a href="./src/y2/types/osint_get_gps_jamming_zones_response.py">OsintGetGpsJammingZonesResponse</a></code>
- <code title="get /osint/military-posture">client.osint.<a href="./src/y2/resources/osint/osint.py">get_military_posture</a>(\*\*<a href="src/y2/types/osint_get_military_posture_params.py">params</a>) -> <a href="./src/y2/types/osint_get_military_posture_response.py">OsintGetMilitaryPostureResponse</a></code>
- <code title="get /osint/aircraft">client.osint.<a href="./src/y2/resources/osint/osint.py">list_aircraft</a>(\*\*<a href="src/y2/types/osint_list_aircraft_params.py">params</a>) -> <a href="./src/y2/types/osint_list_aircraft_response.py">OsintListAircraftResponse</a></code>
- <code title="get /osint/events">client.osint.<a href="./src/y2/resources/osint/osint.py">list_events</a>(\*\*<a href="src/y2/types/osint_list_events_params.py">params</a>) -> <a href="./src/y2/types/osint_list_events_response.py">OsintListEventsResponse</a></code>
- <code title="get /osint/vessels">client.osint.<a href="./src/y2/resources/osint/osint.py">list_vessels</a>(\*\*<a href="src/y2/types/osint_list_vessels_params.py">params</a>) -> <a href="./src/y2/types/osint_list_vessels_response.py">OsintListVesselsResponse</a></code>
- <code title="get /osint/map">client.osint.<a href="./src/y2/resources/osint/osint.py">map_events</a>(\*\*<a href="src/y2/types/osint_map_events_params.py">params</a>) -> <a href="./src/y2/types/osint_map_events_response.py">OsintMapEventsResponse</a></code>

## Countries

Types:

```python
from y2.types.osint import (
    CountryGetCountryInstabilityIndexResponse,
    CountryGetCountryNewsResponse,
    CountryGetIntelligenceBriefResponse,
    CountryGetPredictionMarketsResponse,
    CountryGetStockMarketIndexResponse,
)
```

Methods:

- <code title="get /osint/countries/{countryCode}/cii">client.osint.countries.<a href="./src/y2/resources/osint/countries.py">get_country_instability_index</a>(country_code) -> <a href="./src/y2/types/osint/country_get_country_instability_index_response.py">CountryGetCountryInstabilityIndexResponse</a></code>
- <code title="get /osint/countries/{countryCode}/news">client.osint.countries.<a href="./src/y2/resources/osint/countries.py">get_country_news</a>(country_code, \*\*<a href="src/y2/types/osint/country_get_country_news_params.py">params</a>) -> <a href="./src/y2/types/osint/country_get_country_news_response.py">CountryGetCountryNewsResponse</a></code>
- <code title="get /osint/countries/{countryCode}/brief">client.osint.countries.<a href="./src/y2/resources/osint/countries.py">get_intelligence_brief</a>(country_code) -> <a href="./src/y2/types/osint/country_get_intelligence_brief_response.py">CountryGetIntelligenceBriefResponse</a></code>
- <code title="get /osint/countries/{countryCode}/predictions">client.osint.countries.<a href="./src/y2/resources/osint/countries.py">get_prediction_markets</a>(country_code, \*\*<a href="src/y2/types/osint/country_get_prediction_markets_params.py">params</a>) -> <a href="./src/y2/types/osint/country_get_prediction_markets_response.py">CountryGetPredictionMarketsResponse</a></code>
- <code title="get /osint/countries/{countryCode}/markets">client.osint.countries.<a href="./src/y2/resources/osint/countries.py">get_stock_market_index</a>(country_code) -> <a href="./src/y2/types/osint/country_get_stock_market_index_response.py">CountryGetStockMarketIndexResponse</a></code>

## Sources

Types:

```python
from y2.types.osint import SourceGetDataSourceHealthResponse
```

Methods:

- <code title="get /osint/sources/status">client.osint.sources.<a href="./src/y2/resources/osint/sources.py">get_data_source_health</a>() -> <a href="./src/y2/types/osint/source_get_data_source_health_response.py">SourceGetDataSourceHealthResponse</a></code>
