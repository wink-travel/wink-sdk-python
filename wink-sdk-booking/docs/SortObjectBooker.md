# SortObjectBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sorted** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 
**unsorted** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_booking.models.sort_object_booker import SortObjectBooker

# TODO update the JSON string below
json = "{}"
# create an instance of SortObjectBooker from a JSON string
sort_object_booker_instance = SortObjectBooker.from_json(json)
# print the JSON string representation of the object
print(SortObjectBooker.to_json())

# convert the object into a dict
sort_object_booker_dict = sort_object_booker_instance.to_dict()
# create an instance of SortObjectBooker from a dict
sort_object_booker_from_dict = SortObjectBooker.from_dict(sort_object_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


