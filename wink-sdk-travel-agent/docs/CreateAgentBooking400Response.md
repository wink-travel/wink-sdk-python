# CreateAgentBooking400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.create_agent_booking400_response import CreateAgentBooking400Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAgentBooking400Response from a JSON string
create_agent_booking400_response_instance = CreateAgentBooking400Response.from_json(json)
# print the JSON string representation of the object
print(CreateAgentBooking400Response.to_json())

# convert the object into a dict
create_agent_booking400_response_dict = create_agent_booking400_response_instance.to_dict()
# create an instance of CreateAgentBooking400Response from a dict
create_agent_booking400_response_from_dict = CreateAgentBooking400Response.from_dict(create_agent_booking400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


