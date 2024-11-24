# AggregateDescriptorBooker

Primitive aggregate data points

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field to run aggregate function on | [optional] 
**aggregate** | **str** | Aggregate function | [optional] 

## Example

```python
from wink_sdk_booking.models.aggregate_descriptor_booker import AggregateDescriptorBooker

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateDescriptorBooker from a JSON string
aggregate_descriptor_booker_instance = AggregateDescriptorBooker.from_json(json)
# print the JSON string representation of the object
print(AggregateDescriptorBooker.to_json())

# convert the object into a dict
aggregate_descriptor_booker_dict = aggregate_descriptor_booker_instance.to_dict()
# create an instance of AggregateDescriptorBooker from a dict
aggregate_descriptor_booker_from_dict = AggregateDescriptorBooker.from_dict(aggregate_descriptor_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


