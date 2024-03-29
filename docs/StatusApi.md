# swagger_client.StatusApi

All URIs are relative to */apiv2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_project_status**](StatusApi.md#get_project_status) | **GET** /status/{projecttype}/{projectid} | Get status of your project

# **get_project_status**
> ProjectStatus get_project_status(projecttype, projectid, apikey)

Get status of your project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusApi()
projecttype = 56 # int | Type ID as returned by /create endpoint
projectid = 56 # int | Project ID as returned by /create endpoint
apikey = 'apikey_example' # str | Your api key

try:
    # Get status of your project
    api_response = api_instance.get_project_status(projecttype, projectid, apikey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusApi->get_project_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projecttype** | **int**| Type ID as returned by /create endpoint | 
 **projectid** | **int**| Project ID as returned by /create endpoint | 
 **apikey** | **str**| Your api key | 

### Return type

[**ProjectStatus**](ProjectStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

