# CreateAgentBookingRequestAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rooms** | [**List[AgentBookingRequestAgent]**](AgentBookingRequestAgent.md) | List of room configuration booking requests. Each entry is a separately booked room. | 
**display_currency** | **str** | The desired currency | [default to 'USD']
**display_language** | **str** | The desired language | [default to 'en']
**source_url** | **str** | Where did the booking occur | 
**trace_id** | **str** | Integrator can choose to include a unique identifier to help identify the collection of bookings | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.create_agent_booking_request_agent import CreateAgentBookingRequestAgent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAgentBookingRequestAgent from a JSON string
create_agent_booking_request_agent_instance = CreateAgentBookingRequestAgent.from_json(json)
# print the JSON string representation of the object
print(CreateAgentBookingRequestAgent.to_json())

# convert the object into a dict
create_agent_booking_request_agent_dict = create_agent_booking_request_agent_instance.to_dict()
# create an instance of CreateAgentBookingRequestAgent from a dict
create_agent_booking_request_agent_from_dict = CreateAgentBookingRequestAgent.from_dict(create_agent_booking_request_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


