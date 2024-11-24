# TravelAgentAgent

Customize account with a custom logo / profile picture.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**self_acquires** | **bool** | Whether the agent is in charge of charging the property. | 
**self_disburses** | **bool** | Whether the agent is in charge of paying the property. | 

## Example

```python
from wink_sdk_travel_agent.models.travel_agent_agent import TravelAgentAgent

# TODO update the JSON string below
json = "{}"
# create an instance of TravelAgentAgent from a JSON string
travel_agent_agent_instance = TravelAgentAgent.from_json(json)
# print the JSON string representation of the object
print(TravelAgentAgent.to_json())

# convert the object into a dict
travel_agent_agent_dict = travel_agent_agent_instance.to_dict()
# create an instance of TravelAgentAgent from a dict
travel_agent_agent_from_dict = TravelAgentAgent.from_dict(travel_agent_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


