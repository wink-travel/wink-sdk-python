# SortObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** |  | [optional] 
**null_handling** | **str** |  | [optional] 
**ascending** | **bool** |  | [optional] 
**var_property** | **str** |  | [optional] 
**ignore_case** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.sort_object import SortObject

# TODO update the JSON string below
json = "{}"
# create an instance of SortObject from a JSON string
sort_object_instance = SortObject.from_json(json)
# print the JSON string representation of the object
print(SortObject.to_json())

# convert the object into a dict
sort_object_dict = sort_object_instance.to_dict()
# create an instance of SortObject from a dict
sort_object_from_dict = SortObject.from_dict(sort_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


