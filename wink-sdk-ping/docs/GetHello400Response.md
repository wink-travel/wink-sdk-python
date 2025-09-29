# GetHello400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from wink_sdk_ping.models.get_hello400_response import GetHello400Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetHello400Response from a JSON string
get_hello400_response_instance = GetHello400Response.from_json(json)
# print the JSON string representation of the object
print(GetHello400Response.to_json())

# convert the object into a dict
get_hello400_response_dict = get_hello400_response_instance.to_dict()
# create an instance of GetHello400Response from a dict
get_hello400_response_from_dict = GetHello400Response.from_dict(get_hello400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


