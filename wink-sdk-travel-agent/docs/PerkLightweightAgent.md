# PerkLightweightAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Enum identifier identifier for this perk. Makes the persistent version backwards compatible. | 
**guaranteed** | **bool** | Whether perk is guaranteed or not. | [optional] 
**level** | **int** | The platform value of this perk. | [optional] 
**descriptions** | [**List[SimpleDescriptionAgent]**](SimpleDescriptionAgent.md) | Localized description for this perk | 
**sort** | **int** | This is how perks get sorted when in a list | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.perk_lightweight_agent import PerkLightweightAgent

# TODO update the JSON string below
json = "{}"
# create an instance of PerkLightweightAgent from a JSON string
perk_lightweight_agent_instance = PerkLightweightAgent.from_json(json)
# print the JSON string representation of the object
print(PerkLightweightAgent.to_json())

# convert the object into a dict
perk_lightweight_agent_dict = perk_lightweight_agent_instance.to_dict()
# create an instance of PerkLightweightAgent from a dict
perk_lightweight_agent_from_dict = PerkLightweightAgent.from_dict(perk_lightweight_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


