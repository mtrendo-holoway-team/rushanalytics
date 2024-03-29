# swagger_client.GdsApi

All URIs are relative to */apiv2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gds_competitors_visibility**](GdsApi.md#gds_competitors_visibility) | **GET** /gds/competitors_visibility/{projectid} | Get competitors visibility data of your rank tracker project for Google Data Studio
[**gds_positions**](GdsApi.md#gds_positions) | **GET** /gds/positions/{projectid} | Get positions history of your rank tracker project for Google Data Studio
[**gds_schema**](GdsApi.md#gds_schema) | **GET** /gds/schema/{projectid} | Get schema of your rank tracker project for Google Data Studio
[**gds_tops**](GdsApi.md#gds_tops) | **GET** /gds/tops/{projectid} | Get tops (100,30,10,5,3) data of your rank tracker project for Google Data Studio
[**gds_visibility**](GdsApi.md#gds_visibility) | **GET** /gds/visibility/{projectid} | Get competitors visibility data of your rank tracker project for Google Data Studio

# **gds_competitors_visibility**
> GdsCompetitorsVisibility gds_competitors_visibility(projectid, apikey)

Get competitors visibility data of your rank tracker project for Google Data Studio

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GdsApi()
projectid = 56 # int | Project ID
apikey = 'apikey_example' # str | Your api key

try:
    # Get competitors visibility data of your rank tracker project for Google Data Studio
    api_response = api_instance.gds_competitors_visibility(projectid, apikey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GdsApi->gds_competitors_visibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectid** | **int**| Project ID | 
 **apikey** | **str**| Your api key | 

### Return type

[**GdsCompetitorsVisibility**](GdsCompetitorsVisibility.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gds_positions**
> GdsPositions gds_positions(projectid, apikey)

Get positions history of your rank tracker project for Google Data Studio

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GdsApi()
projectid = 56 # int | Project ID
apikey = 'apikey_example' # str | Your api key

try:
    # Get positions history of your rank tracker project for Google Data Studio
    api_response = api_instance.gds_positions(projectid, apikey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GdsApi->gds_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectid** | **int**| Project ID | 
 **apikey** | **str**| Your api key | 

### Return type

[**GdsPositions**](GdsPositions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gds_schema**
> GdsSchema gds_schema(projectid, apikey)

Get schema of your rank tracker project for Google Data Studio

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GdsApi()
projectid = 56 # int | Project ID
apikey = 'apikey_example' # str | Your api key

try:
    # Get schema of your rank tracker project for Google Data Studio
    api_response = api_instance.gds_schema(projectid, apikey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GdsApi->gds_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectid** | **int**| Project ID | 
 **apikey** | **str**| Your api key | 

### Return type

[**GdsSchema**](GdsSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gds_tops**
> GdsTops gds_tops(projectid, apikey)

Get tops (100,30,10,5,3) data of your rank tracker project for Google Data Studio

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GdsApi()
projectid = 56 # int | Project ID
apikey = 'apikey_example' # str | Your api key

try:
    # Get tops (100,30,10,5,3) data of your rank tracker project for Google Data Studio
    api_response = api_instance.gds_tops(projectid, apikey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GdsApi->gds_tops: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectid** | **int**| Project ID | 
 **apikey** | **str**| Your api key | 

### Return type

[**GdsTops**](GdsTops.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gds_visibility**
> GdsVisibility gds_visibility(projectid, apikey)

Get competitors visibility data of your rank tracker project for Google Data Studio

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GdsApi()
projectid = 56 # int | Project ID
apikey = 'apikey_example' # str | Your api key

try:
    # Get competitors visibility data of your rank tracker project for Google Data Studio
    api_response = api_instance.gds_visibility(projectid, apikey)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GdsApi->gds_visibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projectid** | **int**| Project ID | 
 **apikey** | **str**| Your api key | 

### Return type

[**GdsVisibility**](GdsVisibility.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

