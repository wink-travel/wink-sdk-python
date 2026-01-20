# BedroomConfigurationAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **UUID** | Unique identifier | 
**name** | **str** | Name of layout | 
**bedroom_list** | [**List[BedroomAgent]**](BedroomAgent.md) | A room type can have more than one bedroom configuration. | 

## Example

```python
from wink_sdk_travel_agent.models.bedroom_configuration_agent import BedroomConfigurationAgent

# TODO update the JSON string below
json = "{}"
# create an instance of BedroomConfigurationAgent from a JSON string
bedroom_configuration_agent_instance = BedroomConfigurationAgent.from_json(json)
# print the JSON string representation of the object
print(BedroomConfigurationAgent.to_json())

# convert the object into a dict
bedroom_configuration_agent_dict = bedroom_configuration_agent_instance.to_dict()
# create an instance of BedroomConfigurationAgent from a dict
bedroom_configuration_agent_from_dict = BedroomConfigurationAgent.from_dict(bedroom_configuration_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


