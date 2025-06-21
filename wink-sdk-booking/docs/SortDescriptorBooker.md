# SortDescriptorBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dir** | **str** | Descriptors used for sorting result set | [optional] 
**var_field** | **str** | Data set field to sort on | [optional] 

## Example

```python
from wink_sdk_booking.models.sort_descriptor_booker import SortDescriptorBooker

# TODO update the JSON string below
json = "{}"
# create an instance of SortDescriptorBooker from a JSON string
sort_descriptor_booker_instance = SortDescriptorBooker.from_json(json)
# print the JSON string representation of the object
print(SortDescriptorBooker.to_json())

# convert the object into a dict
sort_descriptor_booker_dict = sort_descriptor_booker_instance.to_dict()
# create an instance of SortDescriptorBooker from a dict
sort_descriptor_booker_from_dict = SortDescriptorBooker.from_dict(sort_descriptor_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


