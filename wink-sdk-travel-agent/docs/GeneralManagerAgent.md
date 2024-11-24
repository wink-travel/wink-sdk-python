# GeneralManagerAgent

General manager related data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of GM currently managing the property. | 
**image** | [**SimpleMultimediaAgent**](SimpleMultimediaAgent.md) |  | [optional] 
**descriptions** | [**List[LocalizedDescriptionAgent]**](LocalizedDescriptionAgent.md) | Localized welcome message from GM. | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.general_manager_agent import GeneralManagerAgent

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralManagerAgent from a JSON string
general_manager_agent_instance = GeneralManagerAgent.from_json(json)
# print the JSON string representation of the object
print(GeneralManagerAgent.to_json())

# convert the object into a dict
general_manager_agent_dict = general_manager_agent_instance.to_dict()
# create an instance of GeneralManagerAgent from a dict
general_manager_agent_from_dict = GeneralManagerAgent.from_dict(general_manager_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


