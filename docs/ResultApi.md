# swagger_client.ResultApi

All URIs are relative to */apiv2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ad_words_results**](ResultApi.md#get_ad_words_results) | **GET** /result/adwords/{projectid} | Get results of your AdWords project
[**get_fpp_results**](ResultApi.md#get_fpp_results) | **GET** /result/fpp/{projectid} | Get results of your FPP project
[**get_indexation_results**](ResultApi.md#get_indexation_results) | **GET** /result/indexation/{projectid} | Get results of your Indexation project
[**get_suggest_results**](ResultApi.md#get_suggest_results) | **GET** /result/suggest/{projectid} | Get results of your Suggest project
[**get_top10_results**](ResultApi.md#get_top10_results) | **GET** /result/top10/{projectid} | Get results of your Top10 project
[**get_wordstat_results**](ResultApi.md#get_wordstat_results) | **GET** /result/wordstat/{projectid} | Get results of your Wordstat project

# **get_ad_words_results**
> AdWordsResult get_ad_words_results(projectid, apikey)

Get results of your AdWords project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResultApi()
projectid = 56 # int | Project ID as returned by /create endpoint
apikey = 'apikey_example' # str | Your api key

try:
    # Get results of your AdWords project
    api_response = api_instance.get_ad_words_results(projectid, apikey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultApi->get_ad_words_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectid** | **int**| Project ID as returned by /create endpoint | 
 **apikey** | **str**| Your api key | 

### Return type

[**AdWordsResult**](AdWordsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fpp_results**
> FppResult get_fpp_results(projectid, apikey)

Get results of your FPP project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResultApi()
projectid = 56 # int | Project ID as returned by /create endpoint
apikey = 'apikey_example' # str | Your api key

try:
    # Get results of your FPP project
    api_response = api_instance.get_fpp_results(projectid, apikey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultApi->get_fpp_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectid** | **int**| Project ID as returned by /create endpoint | 
 **apikey** | **str**| Your api key | 

### Return type

[**FppResult**](FppResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_indexation_results**
> IndexationResult get_indexation_results(projectid, apikey)

Get results of your Indexation project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResultApi()
projectid = 56 # int | Project ID as returned by /create endpoint
apikey = 'apikey_example' # str | Your api key

try:
    # Get results of your Indexation project
    api_response = api_instance.get_indexation_results(projectid, apikey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultApi->get_indexation_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectid** | **int**| Project ID as returned by /create endpoint | 
 **apikey** | **str**| Your api key | 

### Return type

[**IndexationResult**](IndexationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_suggest_results**
> SuggestResult get_suggest_results(projectid, apikey)

Get results of your Suggest project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResultApi()
projectid = 56 # int | Project ID as returned by /create endpoint
apikey = 'apikey_example' # str | Your api key

try:
    # Get results of your Suggest project
    api_response = api_instance.get_suggest_results(projectid, apikey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultApi->get_suggest_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectid** | **int**| Project ID as returned by /create endpoint | 
 **apikey** | **str**| Your api key | 

### Return type

[**SuggestResult**](SuggestResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_top10_results**
> Top10Result get_top10_results(projectid, apikey)

Get results of your Top10 project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResultApi()
projectid = 56 # int | Project ID as returned by /create endpoint
apikey = 'apikey_example' # str | Your api key

try:
    # Get results of your Top10 project
    api_response = api_instance.get_top10_results(projectid, apikey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultApi->get_top10_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectid** | **int**| Project ID as returned by /create endpoint | 
 **apikey** | **str**| Your api key | 

### Return type

[**Top10Result**](Top10Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wordstat_results**
> WordstatResult get_wordstat_results(projectid, apikey)

Get results of your Wordstat project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResultApi()
projectid = 56 # int | Project ID as returned by /create endpoint
apikey = 'apikey_example' # str | Your api key

try:
    # Get results of your Wordstat project
    api_response = api_instance.get_wordstat_results(projectid, apikey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResultApi->get_wordstat_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectid** | **int**| Project ID as returned by /create endpoint | 
 **apikey** | **str**| Your api key | 

### Return type

[**WordstatResult**](WordstatResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

