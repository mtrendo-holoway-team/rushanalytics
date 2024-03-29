# swagger_client.UpdateApi

All URIs are relative to */apiv2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_rpp_project**](UpdateApi.md#update_rpp_project) | **POST** /update/ranktracker | Update Rank Tracker project

# **update_rpp_project**
> CreateResponse update_rpp_project(body)

Update Rank Tracker project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UpdateApi()
body = swagger_client.UpdateRpp() # UpdateRpp | Project parameters

try:
    # Update Rank Tracker project
    api_response = api_instance.update_rpp_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpdateApi->update_rpp_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateRpp**](UpdateRpp.md)| Project parameters | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

