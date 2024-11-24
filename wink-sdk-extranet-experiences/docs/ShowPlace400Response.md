# ShowPlace400Response


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
from wink_sdk_extranet_experiences.models.show_place400_response import ShowPlace400Response

# TODO update the JSON string below
json = "{}"
# create an instance of ShowPlace400Response from a JSON string
show_place400_response_instance = ShowPlace400Response.from_json(json)
# print the JSON string representation of the object
print(ShowPlace400Response.to_json())

# convert the object into a dict
show_place400_response_dict = show_place400_response_instance.to_dict()
# create an instance of ShowPlace400Response from a dict
show_place400_response_from_dict = ShowPlace400Response.from_dict(show_place400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


