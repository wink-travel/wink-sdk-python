# ManagedByEntityAgent

If another company entity is managing this property, on behalf of the property, it can be specified here and the managing entity would be applicable a management fee on every booking.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Entity identifier | 
**name** | **str** | Name of entity | 
**commission_in_percent** | **float** | Agency commission | 
**rules** | [**ManagedByEntityRulesAgent**](ManagedByEntityRulesAgent.md) |  | [optional] 
**valid** | **bool** | Whether managing entity is eligible a commission. | [optional] [readonly] 

## Example

```python
from wink_sdk_travel_agent.models.managed_by_entity_agent import ManagedByEntityAgent

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedByEntityAgent from a JSON string
managed_by_entity_agent_instance = ManagedByEntityAgent.from_json(json)
# print the JSON string representation of the object
print(ManagedByEntityAgent.to_json())

# convert the object into a dict
managed_by_entity_agent_dict = managed_by_entity_agent_instance.to_dict()
# create an instance of ManagedByEntityAgent from a dict
managed_by_entity_agent_from_dict = ManagedByEntityAgent.from_dict(managed_by_entity_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


