# UpsertTravelAgentRequestAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**self_acquires** | **bool** | Whether the agent is in charge of charging the property. | 
**self_disburses** | **bool** | Whether the agent is in charge of paying the property. | 

## Example

```python
from wink_sdk_travel_agent.models.upsert_travel_agent_request_agent import UpsertTravelAgentRequestAgent

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertTravelAgentRequestAgent from a JSON string
upsert_travel_agent_request_agent_instance = UpsertTravelAgentRequestAgent.from_json(json)
# print the JSON string representation of the object
print(UpsertTravelAgentRequestAgent.to_json())

# convert the object into a dict
upsert_travel_agent_request_agent_dict = upsert_travel_agent_request_agent_instance.to_dict()
# create an instance of UpsertTravelAgentRequestAgent from a dict
upsert_travel_agent_request_agent_from_dict = UpsertTravelAgentRequestAgent.from_dict(upsert_travel_agent_request_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


