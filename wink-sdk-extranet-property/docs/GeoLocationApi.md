# wink_sdk_extranet_property.GeoLocationApi

All URIs are relative to *https://api.wink.travel*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_geo_location**](GeoLocationApi.md#update_geo_location) | **PATCH** /api/property/{propertyIdentifier}/location | Set Geo-Location


# **update_geo_location**
> PropertySupplier update_geo_location(property_identifier, update_location_request_supplier, wink_version=wink_version)

Set Geo-Location

Update property geo-location. Note: x = longitude, y = latitude, type = Point, coordinates = [longitude, latitude].

### Example

* OAuth Authentication (oauth2ClientCredentials):

```python
import wink_sdk_extranet_property
from wink_sdk_extranet_property.models.property_supplier import PropertySupplier
from wink_sdk_extranet_property.models.update_location_request_supplier import UpdateLocationRequestSupplier
from wink_sdk_extranet_property.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wink.travel
# See configuration.py for a list of all supported configuration parameters.
configuration = wink_sdk_extranet_property.Configuration(
    host = "https://api.wink.travel"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with wink_sdk_extranet_property.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wink_sdk_extranet_property.GeoLocationApi(api_client)
    property_identifier = 'hotel-1' # str | Update geo-location for this property identifier
    update_location_request_supplier = wink_sdk_extranet_property.UpdateLocationRequestSupplier() # UpdateLocationRequestSupplier | Update geo-location request body
    wink_version = 'wink_version_example' # str |  (optional)

    try:
        # Set Geo-Location
        api_response = api_instance.update_geo_location(property_identifier, update_location_request_supplier, wink_version=wink_version)
        print("The response of GeoLocationApi->update_geo_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeoLocationApi->update_geo_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_identifier** | **str**| Update geo-location for this property identifier | 
 **update_location_request_supplier** | [**UpdateLocationRequestSupplier**](UpdateLocationRequestSupplier.md)| Update geo-location request body | 
 **wink_version** | **str**|  | [optional] 

### Return type

[**PropertySupplier**](PropertySupplier.md)

### Authorization

[oauth2ClientCredentials](../README.md#oauth2ClientCredentials)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*, application/json, application/xml, text/xml, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Forbidden |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

