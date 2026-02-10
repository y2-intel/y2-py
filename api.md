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
