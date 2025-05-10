# HttpStatusCodeNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **bool** |  | [optional] 
**is2xx_successful** | **bool** |  | [optional] 
**is3xx_redirection** | **bool** |  | [optional] 
**is4xx_client_error** | **bool** |  | [optional] 
**is5xx_server_error** | **bool** |  | [optional] 
**is1xx_informational** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.http_status_code_non_authenticated_entity import HttpStatusCodeNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of HttpStatusCodeNonAuthenticatedEntity from a JSON string
http_status_code_non_authenticated_entity_instance = HttpStatusCodeNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(HttpStatusCodeNonAuthenticatedEntity.to_json())

# convert the object into a dict
http_status_code_non_authenticated_entity_dict = http_status_code_non_authenticated_entity_instance.to_dict()
# create an instance of HttpStatusCodeNonAuthenticatedEntity from a dict
http_status_code_non_authenticated_entity_from_dict = HttpStatusCodeNonAuthenticatedEntity.from_dict(http_status_code_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


