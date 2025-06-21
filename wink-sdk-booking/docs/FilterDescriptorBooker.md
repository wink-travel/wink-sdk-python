# FilterDescriptorBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field name to filter on | 
**operator** | **str** | Filter operator to use on field | 
**value** | **object** |  | 
**ignore_case** | **bool** | Make filter comparison case insensitive. Default: Case sensitive  | [optional] 

## Example

```python
from wink_sdk_booking.models.filter_descriptor_booker import FilterDescriptorBooker

# TODO update the JSON string below
json = "{}"
# create an instance of FilterDescriptorBooker from a JSON string
filter_descriptor_booker_instance = FilterDescriptorBooker.from_json(json)
# print the JSON string representation of the object
print(FilterDescriptorBooker.to_json())

# convert the object into a dict
filter_descriptor_booker_dict = filter_descriptor_booker_instance.to_dict()
# create an instance of FilterDescriptorBooker from a dict
filter_descriptor_booker_from_dict = FilterDescriptorBooker.from_dict(filter_descriptor_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


