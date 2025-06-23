# DefaultHttpStatusCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **bool** |  | [optional] 
**is4xx_client_error** | **bool** |  | [optional] 
**is5xx_server_error** | **bool** |  | [optional] 
**is1xx_informational** | **bool** |  | [optional] 
**is2xx_successful** | **bool** |  | [optional] 
**is3xx_redirection** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.default_http_status_code import DefaultHttpStatusCode

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultHttpStatusCode from a JSON string
default_http_status_code_instance = DefaultHttpStatusCode.from_json(json)
# print the JSON string representation of the object
print(DefaultHttpStatusCode.to_json())

# convert the object into a dict
default_http_status_code_dict = default_http_status_code_instance.to_dict()
# create an instance of DefaultHttpStatusCode from a dict
default_http_status_code_from_dict = DefaultHttpStatusCode.from_dict(default_http_status_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


