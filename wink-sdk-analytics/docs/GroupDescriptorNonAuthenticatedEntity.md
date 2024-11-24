# GroupDescriptorNonAuthenticatedEntity

Descriptors to group result sets by.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field to group data set on | [optional] 
**dir** | **str** | Group sort direction | [optional] 
**aggregates** | [**List[AggregateDescriptorNonAuthenticatedEntity]**](AggregateDescriptorNonAuthenticatedEntity.md) | Primitive aggregate data points | [optional] 

## Example

```python
from wink_sdk_analytics.models.group_descriptor_non_authenticated_entity import GroupDescriptorNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of GroupDescriptorNonAuthenticatedEntity from a JSON string
group_descriptor_non_authenticated_entity_instance = GroupDescriptorNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(GroupDescriptorNonAuthenticatedEntity.to_json())

# convert the object into a dict
group_descriptor_non_authenticated_entity_dict = group_descriptor_non_authenticated_entity_instance.to_dict()
# create an instance of GroupDescriptorNonAuthenticatedEntity from a dict
group_descriptor_non_authenticated_entity_from_dict = GroupDescriptorNonAuthenticatedEntity.from_dict(group_descriptor_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


