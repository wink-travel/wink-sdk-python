# PingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**creator** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**approved** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_channel_manager.models.ping_response import PingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PingResponse from a JSON string
ping_response_instance = PingResponse.from_json(json)
# print the JSON string representation of the object
print(PingResponse.to_json())

# convert the object into a dict
ping_response_dict = ping_response_instance.to_dict()
# create an instance of PingResponse from a dict
ping_response_from_dict = PingResponse.from_dict(ping_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


