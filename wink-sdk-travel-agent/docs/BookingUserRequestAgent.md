# BookingUserRequestAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name | 
**last_name** | **str** | Last name | 
**email** | **str** | Email | 
**telephone** | **str** | Telephone | [optional] 
**valid** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.booking_user_request_agent import BookingUserRequestAgent

# TODO update the JSON string below
json = "{}"
# create an instance of BookingUserRequestAgent from a JSON string
booking_user_request_agent_instance = BookingUserRequestAgent.from_json(json)
# print the JSON string representation of the object
print(BookingUserRequestAgent.to_json())

# convert the object into a dict
booking_user_request_agent_dict = booking_user_request_agent_instance.to_dict()
# create an instance of BookingUserRequestAgent from a dict
booking_user_request_agent_from_dict = BookingUserRequestAgent.from_dict(booking_user_request_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


