# swagger_client.CreateApi

All URIs are relative to */apiv2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ad_words_project**](CreateApi.md#create_ad_words_project) | **POST** /create/adwords | Create AdWords parsing project
[**create_fpp_project**](CreateApi.md#create_fpp_project) | **POST** /create/fpp | Create Fast Positions parsing project
[**create_indexation_project**](CreateApi.md#create_indexation_project) | **POST** /create/indexation | Create Indexation parsing project
[**create_rpp_project**](CreateApi.md#create_rpp_project) | **POST** /create/ranktracker | Create Rank Tracker project BETA
[**create_suggest_project**](CreateApi.md#create_suggest_project) | **POST** /create/suggest | Create Suggest parsing project
[**create_top10_project**](CreateApi.md#create_top10_project) | **POST** /create/top10 | Create Top 10 parsing project
[**create_wordstat_project**](CreateApi.md#create_wordstat_project) | **POST** /create/wordstat | Create Wordstat parsing project

# **create_ad_words_project**
> CreateResponse create_ad_words_project(body)

Create AdWords parsing project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateApi()
body = swagger_client.AdWordsParameters() # AdWordsParameters | Project parameters

try:
    # Create AdWords parsing project
    api_response = api_instance.create_ad_words_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateApi->create_ad_words_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdWordsParameters**](AdWordsParameters.md)| Project parameters | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fpp_project**
> CreateResponse create_fpp_project(body)

Create Fast Positions parsing project

At least one region is required. At least one keyword is required. Set region device to 1 for mobile parsing. To see available region parameters, view [List of languages](/apiLanguages.php), [List of region IDs in Google](/apiRegionsGoogle.php), [List of region IDs in Yandex](/apiRegionsYandex.php).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateApi()
body = swagger_client.CreateFpp() # CreateFpp | Project parameters

try:
    # Create Fast Positions parsing project
    api_response = api_instance.create_fpp_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateApi->create_fpp_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateFpp**](CreateFpp.md)| Project parameters | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_indexation_project**
> CreateResponse create_indexation_project(body)

Create Indexation parsing project

At least one searchEngine is required. At least one keyword is required.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateApi()
body = swagger_client.IndexationParameters() # IndexationParameters | Project parameters

try:
    # Create Indexation parsing project
    api_response = api_instance.create_indexation_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateApi->create_indexation_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IndexationParameters**](IndexationParameters.md)| Project parameters | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rpp_project**
> CreateResponse create_rpp_project(body)

Create Rank Tracker project BETA

At least one region is required. At least one keyword is required. Set region device to 1 for mobile parsing. To see available region parameters, view [List of languages](/apiLanguages.php), [List of region IDs in Google](/apiRegionsGoogle.php), [List of region IDs in Yandex](/apiRegionsYandex.php).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateApi()
body = swagger_client.CreateRpp() # CreateRpp | Project parameters

try:
    # Create Rank Tracker project BETA
    api_response = api_instance.create_rpp_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateApi->create_rpp_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRpp**](CreateRpp.md)| Project parameters | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_suggest_project**
> CreateResponse create_suggest_project(body)

Create Suggest parsing project

At least one region type is required. Depth can be 1-3.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateApi()
body = swagger_client.SuggestParameters() # SuggestParameters | Project parameters

try:
    # Create Suggest parsing project
    api_response = api_instance.create_suggest_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateApi->create_suggest_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SuggestParameters**](SuggestParameters.md)| Project parameters | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_top10_project**
> CreateResponse create_top10_project(body)

Create Top 10 parsing project

At least one keyword is required. Depth is optional parameter and can be 10-100, automatically rounded to next 10. To see available region parameters, view [List of languages](/apiLanguages.php), [List of region IDs in Google](/apiRegionsGoogle.php), [List of region IDs in Yandex](/apiRegionsYandex.php).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateApi()
body = swagger_client.Top10Parameters() # Top10Parameters | Project parameters

try:
    # Create Top 10 parsing project
    api_response = api_instance.create_top10_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateApi->create_top10_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Top10Parameters**](Top10Parameters.md)| Project parameters | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_wordstat_project**
> CreateResponse create_wordstat_project(body)

Create Wordstat parsing project

Valid inputs for pages are 1-10, maximum pages are collected if input is not specified or out of range. 'pages' parameter is valid for 'Keywords' project type. 'normal', 'parentheses', 'exclamation' and 'wordorder' parameters are valid for type 'SearchVolume'. 'minimumwordstat' is optional, defaults to 1.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreateApi()
body = swagger_client.WordstatParameters() # WordstatParameters | Project parameters

try:
    # Create Wordstat parsing project
    api_response = api_instance.create_wordstat_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreateApi->create_wordstat_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WordstatParameters**](WordstatParameters.md)| Project parameters | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

