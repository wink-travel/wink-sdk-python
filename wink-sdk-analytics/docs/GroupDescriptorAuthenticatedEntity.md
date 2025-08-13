# GroupDescriptorAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field to group data set on | [optional] 
**dir** | **str** | Group sort direction | [optional] 
**aggregates** | [**List[AggregateDescriptorAuthenticatedEntity]**](AggregateDescriptorAuthenticatedEntity.md) | Primitive aggregate data points | [optional] 

## Example

```python
from wink_sdk_analytics.models.group_descriptor_authenticated_entity import GroupDescriptorAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of GroupDescriptorAuthenticatedEntity from a JSON string
group_descriptor_authenticated_entity_instance = GroupDescriptorAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(GroupDescriptorAuthenticatedEntity.to_json())

# convert the object into a dict
group_descriptor_authenticated_entity_dict = group_descriptor_authenticated_entity_instance.to_dict()
# create an instance of GroupDescriptorAuthenticatedEntity from a dict
group_descriptor_authenticated_entity_from_dict = GroupDescriptorAuthenticatedEntity.from_dict(group_descriptor_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


