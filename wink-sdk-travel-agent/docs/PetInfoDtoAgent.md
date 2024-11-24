# PetInfoDtoAgent

Array of customer's pets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Pet name | 
**type** | **str** | Pet type | 

## Example

```python
from wink_sdk_travel_agent.models.pet_info_dto_agent import PetInfoDtoAgent

# TODO update the JSON string below
json = "{}"
# create an instance of PetInfoDtoAgent from a JSON string
pet_info_dto_agent_instance = PetInfoDtoAgent.from_json(json)
# print the JSON string representation of the object
print(PetInfoDtoAgent.to_json())

# convert the object into a dict
pet_info_dto_agent_dict = pet_info_dto_agent_instance.to_dict()
# create an instance of PetInfoDtoAgent from a dict
pet_info_dto_agent_from_dict = PetInfoDtoAgent.from_dict(pet_info_dto_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


