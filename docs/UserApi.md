# swagger_client.UserApi

All URIs are relative to */apiv2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_balance**](UserApi.md#get_user_balance) | **GET** /balance | Get your user balance

# **get_user_balance**
> get_user_balance(apikey)

Get your user balance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserApi()
apikey = 'apikey_example' # str | Your api key

try:
    # Get your user balance
    api_instance.get_user_balance(apikey)
except ApiException as e:
    print("Exception when calling UserApi->get_user_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| Your api key | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

