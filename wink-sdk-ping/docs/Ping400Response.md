# Ping400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from wink_sdk_ping.models.ping400_response import Ping400Response

# TODO update the JSON string below
json = "{}"
# create an instance of Ping400Response from a JSON string
ping400_response_instance = Ping400Response.from_json(json)
# print the JSON string representation of the object
print(Ping400Response.to_json())

# convert the object into a dict
ping400_response_dict = ping400_response_instance.to_dict()
# create an instance of Ping400Response from a dict
ping400_response_from_dict = Ping400Response.from_dict(ping400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


