# swagger_client.ProjectidsApi

All URIs are relative to */apiv2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_projects**](ProjectidsApi.md#get_user_projects) | **GET** /projectids | Get project ids of your created projects

# **get_user_projects**
> ProjectIds get_user_projects(apikey, projecttype=projecttype)

Get project ids of your created projects

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectidsApi()
apikey = 'apikey_example' # str | Your api key
projecttype = 56 # int | Type of project, as returned by create endpoint (optional)

try:
    # Get project ids of your created projects
    api_response = api_instance.get_user_projects(apikey, projecttype=projecttype)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectidsApi->get_user_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| Your api key | 
 **projecttype** | **int**| Type of project, as returned by create endpoint | [optional] 

### Return type

[**ProjectIds**](ProjectIds.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

