# BookingUserSessionAgent

User session information containing itinerary and other user related data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**itinerary** | [**BookingItineraryAgent**](BookingItineraryAgent.md) | Dates and travel info. | 
**language** | **str** | User&#39;s language preference | [optional] 
**currency** | **str** | User&#39;s currency preference | [optional] 
**promotional_codes** | **List[str]** |  | [optional] 
**selected_room_configuration_index** | **int** | User can pass the current room configuration index to retrieve rates specifically for that room configuration. | [optional] 
**lifestyle** | **str** | The preferred user lifestyle. | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.booking_user_session_agent import BookingUserSessionAgent

# TODO update the JSON string below
json = "{}"
# create an instance of BookingUserSessionAgent from a JSON string
booking_user_session_agent_instance = BookingUserSessionAgent.from_json(json)
# print the JSON string representation of the object
print(BookingUserSessionAgent.to_json())

# convert the object into a dict
booking_user_session_agent_dict = booking_user_session_agent_instance.to_dict()
# create an instance of BookingUserSessionAgent from a dict
booking_user_session_agent_from_dict = BookingUserSessionAgent.from_dict(booking_user_session_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


