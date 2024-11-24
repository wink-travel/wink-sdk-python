# ShowRecognition400Response


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
from wink_sdk_extranet_property.models.show_recognition400_response import ShowRecognition400Response

# TODO update the JSON string below
json = "{}"
# create an instance of ShowRecognition400Response from a JSON string
show_recognition400_response_instance = ShowRecognition400Response.from_json(json)
# print the JSON string representation of the object
print(ShowRecognition400Response.to_json())

# convert the object into a dict
show_recognition400_response_dict = show_recognition400_response_instance.to_dict()
# create an instance of ShowRecognition400Response from a dict
show_recognition400_response_from_dict = ShowRecognition400Response.from_dict(show_recognition400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


