# DefaultHttpStatusCodeNonAuthenticatedEntity


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
from wink_sdk_affiliate_winklinks.models.default_http_status_code_non_authenticated_entity import DefaultHttpStatusCodeNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultHttpStatusCodeNonAuthenticatedEntity from a JSON string
default_http_status_code_non_authenticated_entity_instance = DefaultHttpStatusCodeNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(DefaultHttpStatusCodeNonAuthenticatedEntity.to_json())

# convert the object into a dict
default_http_status_code_non_authenticated_entity_dict = default_http_status_code_non_authenticated_entity_instance.to_dict()
# create an instance of DefaultHttpStatusCodeNonAuthenticatedEntity from a dict
default_http_status_code_non_authenticated_entity_from_dict = DefaultHttpStatusCodeNonAuthenticatedEntity.from_dict(default_http_status_code_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


