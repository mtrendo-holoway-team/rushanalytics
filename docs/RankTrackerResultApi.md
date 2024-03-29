# swagger_client.RankTrackerResultApi

All URIs are relative to */apiv2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_regions_list**](RankTrackerResultApi.md#get_regions_list) | **GET** /result/ranktracker/regions/{projectid}/{page} | Get regions list of your Rank Tracker project
[**get_rpp_competitors_list**](RankTrackerResultApi.md#get_rpp_competitors_list) | **GET** /result/ranktracker/competitors/{projectid}/{page} | Get Competitors list
[**get_rpp_results**](RankTrackerResultApi.md#get_rpp_results) | **GET** /result/ranktracker/dynamic/{projectid}/{page} | Get results of your Rank Tracker project - dynamic
[**get_rpp_results_compare_regions**](RankTrackerResultApi.md#get_rpp_results_compare_regions) | **GET** /result/ranktracker/compare_regions/{projectid}/{page} | Get results of your Rank Tracker project - compare regions
[**get_rpp_results_competitors_leaders**](RankTrackerResultApi.md#get_rpp_results_competitors_leaders) | **GET** /result/ranktracker/competitors_leaders/{projectid}/{page} | Get results of your Rank Tracker project - competitors leaders
[**get_rpp_results_competitors_positions**](RankTrackerResultApi.md#get_rpp_results_competitors_positions) | **GET** /result/ranktracker/competitors_positions/{projectid}/{page} | Get results of your Rank Tracker project - competitors positions
[**get_rpp_results_competitors_visibility**](RankTrackerResultApi.md#get_rpp_results_competitors_visibility) | **GET** /result/ranktracker/competitors_visibility/{projectid}/{page} | Get results of your Rank Tracker project - competitors visibility
[**get_rpp_results_positions_history**](RankTrackerResultApi.md#get_rpp_results_positions_history) | **GET** /result/ranktracker/positions_history/{projectid}/{page} | Get results of your Rank Tracker project - positions history
[**get_rpp_results_snippets_history**](RankTrackerResultApi.md#get_rpp_results_snippets_history) | **GET** /result/ranktracker/snippets_history/{projectid}/{page} | Get results of your Rank Tracker project - snippets history
[**get_rpp_results_urls_history**](RankTrackerResultApi.md#get_rpp_results_urls_history) | **GET** /result/ranktracker/urls_history/{projectid}/{page} | Get results of your Rank Tracker project - urls history
[**get_rpp_results_visibility**](RankTrackerResultApi.md#get_rpp_results_visibility) | **GET** /result/ranktracker/visibility/{projectid}/{page} | Get results of your Rank Tracker project - visibility

# **get_regions_list**
> RppRegionsList get_regions_list(projectid, page, apikey)

Get regions list of your Rank Tracker project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RankTrackerResultApi()
projectid = 56 # int | Project ID as returned by /create endpoint
page = 56 # int | Page of results
apikey = 'apikey_example' # str | Your api key

try:
    # Get regions list of your Rank Tracker project
    api_response = api_instance.get_regions_list(projectid, page, apikey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankTrackerResultApi->get_regions_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectid** | **int**| Project ID as returned by /create endpoint | 
 **page** | **int**| Page of results | 
 **apikey** | **str**| Your api key | 

### Return type

[**RppRegionsList**](RppRegionsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rpp_competitors_list**
> RppCompetitorsList get_rpp_competitors_list(projectid, page, apikey)

Get Competitors list

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RankTrackerResultApi()
projectid = 56 # int | Project ID as returned by /create endpoint
page = 56 # int | Page of results
apikey = 'apikey_example' # str | Your api key

try:
    # Get Competitors list
    api_response = api_instance.get_rpp_competitors_list(projectid, page, apikey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankTrackerResultApi->get_rpp_competitors_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectid** | **int**| Project ID as returned by /create endpoint | 
 **page** | **int**| Page of results | 
 **apikey** | **str**| Your api key | 

### Return type

[**RppCompetitorsList**](RppCompetitorsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rpp_results**
> RppResultDynamic get_rpp_results(projectid, page, apikey, period_start=period_start, period_end=period_end)

Get results of your Rank Tracker project - dynamic

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RankTrackerResultApi()
projectid = 56 # int | Project ID as returned by /create endpoint
page = 56 # int | Page of results
apikey = 'apikey_example' # str | Your api key
period_start = '2013-10-20' # date | Get results starting from this date (optional)
period_end = '2013-10-20' # date | Get results ending with this date (optional)

try:
    # Get results of your Rank Tracker project - dynamic
    api_response = api_instance.get_rpp_results(projectid, page, apikey, period_start=period_start, period_end=period_end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankTrackerResultApi->get_rpp_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectid** | **int**| Project ID as returned by /create endpoint | 
 **page** | **int**| Page of results | 
 **apikey** | **str**| Your api key | 
 **period_start** | **date**| Get results starting from this date | [optional] 
 **period_end** | **date**| Get results ending with this date | [optional] 

### Return type

[**RppResultDynamic**](RppResultDynamic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rpp_results_compare_regions**
> RppResultCompareRegions get_rpp_results_compare_regions(projectid, page, apikey, period_start=period_start, period_end=period_end)

Get results of your Rank Tracker project - compare regions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RankTrackerResultApi()
projectid = 56 # int | Project ID as returned by /create endpoint
page = 56 # int | Page of results
apikey = 'apikey_example' # str | Your api key
period_start = '2013-10-20' # date | Get results starting from this date (optional)
period_end = '2013-10-20' # date | Get results ending with this date (optional)

try:
    # Get results of your Rank Tracker project - compare regions
    api_response = api_instance.get_rpp_results_compare_regions(projectid, page, apikey, period_start=period_start, period_end=period_end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankTrackerResultApi->get_rpp_results_compare_regions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectid** | **int**| Project ID as returned by /create endpoint | 
 **page** | **int**| Page of results | 
 **apikey** | **str**| Your api key | 
 **period_start** | **date**| Get results starting from this date | [optional] 
 **period_end** | **date**| Get results ending with this date | [optional] 

### Return type

[**RppResultCompareRegions**](RppResultCompareRegions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rpp_results_competitors_leaders**
> RppResultCompetitorsLeaders get_rpp_results_competitors_leaders(projectid, page, apikey, period_start=period_start, period_end=period_end)

Get results of your Rank Tracker project - competitors leaders

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RankTrackerResultApi()
projectid = 56 # int | Project ID as returned by /create endpoint
page = 56 # int | Page of results
apikey = 'apikey_example' # str | Your api key
period_start = '2013-10-20' # date | Get results starting from this date (optional)
period_end = '2013-10-20' # date | Get results ending with this date (optional)

try:
    # Get results of your Rank Tracker project - competitors leaders
    api_response = api_instance.get_rpp_results_competitors_leaders(projectid, page, apikey, period_start=period_start, period_end=period_end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankTrackerResultApi->get_rpp_results_competitors_leaders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectid** | **int**| Project ID as returned by /create endpoint | 
 **page** | **int**| Page of results | 
 **apikey** | **str**| Your api key | 
 **period_start** | **date**| Get results starting from this date | [optional] 
 **period_end** | **date**| Get results ending with this date | [optional] 

### Return type

[**RppResultCompetitorsLeaders**](RppResultCompetitorsLeaders.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rpp_results_competitors_positions**
> RppResultCompetitorsPositions get_rpp_results_competitors_positions(projectid, page, competitor, apikey, period_start=period_start, period_end=period_end)

Get results of your Rank Tracker project - competitors positions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RankTrackerResultApi()
projectid = 56 # int | Project ID as returned by /create endpoint
page = 56 # int | Page of results
competitor = 'competitor_example' # str | Competitor domain - one from list returned by /result/ranktracker/competitors endpoint
apikey = 'apikey_example' # str | Your api key
period_start = '2013-10-20' # date | Get results starting from this date (optional)
period_end = '2013-10-20' # date | Get results ending with this date (optional)

try:
    # Get results of your Rank Tracker project - competitors positions
    api_response = api_instance.get_rpp_results_competitors_positions(projectid, page, competitor, apikey, period_start=period_start, period_end=period_end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankTrackerResultApi->get_rpp_results_competitors_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectid** | **int**| Project ID as returned by /create endpoint | 
 **page** | **int**| Page of results | 
 **competitor** | **str**| Competitor domain - one from list returned by /result/ranktracker/competitors endpoint | 
 **apikey** | **str**| Your api key | 
 **period_start** | **date**| Get results starting from this date | [optional] 
 **period_end** | **date**| Get results ending with this date | [optional] 

### Return type

[**RppResultCompetitorsPositions**](RppResultCompetitorsPositions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rpp_results_competitors_visibility**
> RppResultCompetitorsVisibility get_rpp_results_competitors_visibility(projectid, page, apikey, period_start=period_start, period_end=period_end)

Get results of your Rank Tracker project - competitors visibility

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RankTrackerResultApi()
projectid = 56 # int | Project ID as returned by /create endpoint
page = 56 # int | Page of results
apikey = 'apikey_example' # str | Your api key
period_start = '2013-10-20' # date | Get results starting from this date (optional)
period_end = '2013-10-20' # date | Get results ending with this date (optional)

try:
    # Get results of your Rank Tracker project - competitors visibility
    api_response = api_instance.get_rpp_results_competitors_visibility(projectid, page, apikey, period_start=period_start, period_end=period_end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankTrackerResultApi->get_rpp_results_competitors_visibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectid** | **int**| Project ID as returned by /create endpoint | 
 **page** | **int**| Page of results | 
 **apikey** | **str**| Your api key | 
 **period_start** | **date**| Get results starting from this date | [optional] 
 **period_end** | **date**| Get results ending with this date | [optional] 

### Return type

[**RppResultCompetitorsVisibility**](RppResultCompetitorsVisibility.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rpp_results_positions_history**
> RppResultPositionsHistory get_rpp_results_positions_history(projectid, page, apikey, period_start=period_start, period_end=period_end)

Get results of your Rank Tracker project - positions history

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RankTrackerResultApi()
projectid = 56 # int | Project ID as returned by /create endpoint
page = 56 # int | Page of results
apikey = 'apikey_example' # str | Your api key
period_start = '2013-10-20' # date | Get results starting from this date (optional)
period_end = '2013-10-20' # date | Get results ending with this date (optional)

try:
    # Get results of your Rank Tracker project - positions history
    api_response = api_instance.get_rpp_results_positions_history(projectid, page, apikey, period_start=period_start, period_end=period_end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankTrackerResultApi->get_rpp_results_positions_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectid** | **int**| Project ID as returned by /create endpoint | 
 **page** | **int**| Page of results | 
 **apikey** | **str**| Your api key | 
 **period_start** | **date**| Get results starting from this date | [optional] 
 **period_end** | **date**| Get results ending with this date | [optional] 

### Return type

[**RppResultPositionsHistory**](RppResultPositionsHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rpp_results_snippets_history**
> RppResultSnippetsHistory get_rpp_results_snippets_history(projectid, page, apikey, period_start=period_start, period_end=period_end)

Get results of your Rank Tracker project - snippets history

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RankTrackerResultApi()
projectid = 56 # int | Project ID as returned by /create endpoint
page = 56 # int | Page of results
apikey = 'apikey_example' # str | Your api key
period_start = '2013-10-20' # date | Get results starting from this date (optional)
period_end = '2013-10-20' # date | Get results ending with this date (optional)

try:
    # Get results of your Rank Tracker project - snippets history
    api_response = api_instance.get_rpp_results_snippets_history(projectid, page, apikey, period_start=period_start, period_end=period_end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankTrackerResultApi->get_rpp_results_snippets_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectid** | **int**| Project ID as returned by /create endpoint | 
 **page** | **int**| Page of results | 
 **apikey** | **str**| Your api key | 
 **period_start** | **date**| Get results starting from this date | [optional] 
 **period_end** | **date**| Get results ending with this date | [optional] 

### Return type

[**RppResultSnippetsHistory**](RppResultSnippetsHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rpp_results_urls_history**
> RppResultUrlsHistory get_rpp_results_urls_history(projectid, page, apikey, period_start=period_start, period_end=period_end)

Get results of your Rank Tracker project - urls history

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RankTrackerResultApi()
projectid = 56 # int | Project ID as returned by /create endpoint
page = 56 # int | Page of results
apikey = 'apikey_example' # str | Your api key
period_start = '2013-10-20' # date | Get results starting from this date (optional)
period_end = '2013-10-20' # date | Get results ending with this date (optional)

try:
    # Get results of your Rank Tracker project - urls history
    api_response = api_instance.get_rpp_results_urls_history(projectid, page, apikey, period_start=period_start, period_end=period_end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankTrackerResultApi->get_rpp_results_urls_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectid** | **int**| Project ID as returned by /create endpoint | 
 **page** | **int**| Page of results | 
 **apikey** | **str**| Your api key | 
 **period_start** | **date**| Get results starting from this date | [optional] 
 **period_end** | **date**| Get results ending with this date | [optional] 

### Return type

[**RppResultUrlsHistory**](RppResultUrlsHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rpp_results_visibility**
> RppResultVisibility get_rpp_results_visibility(projectid, page, apikey, period_start=period_start, period_end=period_end)

Get results of your Rank Tracker project - visibility

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RankTrackerResultApi()
projectid = 56 # int | Project ID as returned by /create endpoint
page = 56 # int | Page of results
apikey = 'apikey_example' # str | Your api key
period_start = '2013-10-20' # date | Get results starting from this date (optional)
period_end = '2013-10-20' # date | Get results ending with this date (optional)

try:
    # Get results of your Rank Tracker project - visibility
    api_response = api_instance.get_rpp_results_visibility(projectid, page, apikey, period_start=period_start, period_end=period_end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankTrackerResultApi->get_rpp_results_visibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectid** | **int**| Project ID as returned by /create endpoint | 
 **page** | **int**| Page of results | 
 **apikey** | **str**| Your api key | 
 **period_start** | **date**| Get results starting from this date | [optional] 
 **period_end** | **date**| Get results ending with this date | [optional] 

### Return type

[**RppResultVisibility**](RppResultVisibility.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

