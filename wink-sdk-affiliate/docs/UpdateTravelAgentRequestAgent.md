# UpdateTravelAgentRequestAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**self_acquires** | **bool** | Whether the agent is in charge of charging the property. | 
**self_disburses** | **bool** | Whether the agent is in charge of paying the property. | 

## Example

```python
from wink_sdk_affiliate.models.update_travel_agent_request_agent import UpdateTravelAgentRequestAgent

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTravelAgentRequestAgent from a JSON string
update_travel_agent_request_agent_instance = UpdateTravelAgentRequestAgent.from_json(json)
# print the JSON string representation of the object
print(UpdateTravelAgentRequestAgent.to_json())

# convert the object into a dict
update_travel_agent_request_agent_dict = update_travel_agent_request_agent_instance.to_dict()
# create an instance of UpdateTravelAgentRequestAgent from a dict
update_travel_agent_request_agent_from_dict = UpdateTravelAgentRequestAgent.from_dict(update_travel_agent_request_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


