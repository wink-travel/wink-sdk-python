# BookingUserAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_identifier** | **str** | User identifier | [optional] 
**first_name** | **str** | First name | 
**last_name** | **str** | Last name | 
**email** | **str** | Email | 
**telephone** | **str** | Telephone | [optional] 
**full_name** | **str** | Full name | [optional] [readonly] 

## Example

```python
from wink_sdk_travel_agent.models.booking_user_agent import BookingUserAgent

# TODO update the JSON string below
json = "{}"
# create an instance of BookingUserAgent from a JSON string
booking_user_agent_instance = BookingUserAgent.from_json(json)
# print the JSON string representation of the object
print(BookingUserAgent.to_json())

# convert the object into a dict
booking_user_agent_dict = booking_user_agent_instance.to_dict()
# create an instance of BookingUserAgent from a dict
booking_user_agent_from_dict = BookingUserAgent.from_dict(booking_user_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


