# PetInfoLightweightAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Pet name | 
**type** | **str** | Pet type | 

## Example

```python
from wink_sdk_travel_agent.models.pet_info_lightweight_agent import PetInfoLightweightAgent

# TODO update the JSON string below
json = "{}"
# create an instance of PetInfoLightweightAgent from a JSON string
pet_info_lightweight_agent_instance = PetInfoLightweightAgent.from_json(json)
# print the JSON string representation of the object
print(PetInfoLightweightAgent.to_json())

# convert the object into a dict
pet_info_lightweight_agent_dict = pet_info_lightweight_agent_instance.to_dict()
# create an instance of PetInfoLightweightAgent from a dict
pet_info_lightweight_agent_from_dict = PetInfoLightweightAgent.from_dict(pet_info_lightweight_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


