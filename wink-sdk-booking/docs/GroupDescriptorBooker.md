# GroupDescriptorBooker

Descriptors to group result sets by.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field to group data set on | [optional] 
**dir** | **str** | Group sort direction | [optional] 
**aggregates** | [**List[AggregateDescriptorBooker]**](AggregateDescriptorBooker.md) | Primitive aggregate data points | [optional] 

## Example

```python
from wink_sdk_booking.models.group_descriptor_booker import GroupDescriptorBooker

# TODO update the JSON string below
json = "{}"
# create an instance of GroupDescriptorBooker from a JSON string
group_descriptor_booker_instance = GroupDescriptorBooker.from_json(json)
# print the JSON string representation of the object
print(GroupDescriptorBooker.to_json())

# convert the object into a dict
group_descriptor_booker_dict = group_descriptor_booker_instance.to_dict()
# create an instance of GroupDescriptorBooker from a dict
group_descriptor_booker_from_dict = GroupDescriptorBooker.from_dict(group_descriptor_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


