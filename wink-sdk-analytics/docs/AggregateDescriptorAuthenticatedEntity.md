# AggregateDescriptorAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field to run aggregate function on | [optional] 
**aggregate** | **str** | Aggregate function | [optional] 

## Example

```python
from wink_sdk_analytics.models.aggregate_descriptor_authenticated_entity import AggregateDescriptorAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateDescriptorAuthenticatedEntity from a JSON string
aggregate_descriptor_authenticated_entity_instance = AggregateDescriptorAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(AggregateDescriptorAuthenticatedEntity.to_json())

# convert the object into a dict
aggregate_descriptor_authenticated_entity_dict = aggregate_descriptor_authenticated_entity_instance.to_dict()
# create an instance of AggregateDescriptorAuthenticatedEntity from a dict
aggregate_descriptor_authenticated_entity_from_dict = AggregateDescriptorAuthenticatedEntity.from_dict(aggregate_descriptor_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


