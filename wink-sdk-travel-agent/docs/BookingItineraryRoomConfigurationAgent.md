# BookingItineraryRoomConfigurationAgent

Room Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adults** | **int** | Number of adults | [optional] [default to 1]
**children** | [**List[BookingItineraryRoomConfigurationChildAgent]**](BookingItineraryRoomConfigurationChildAgent.md) | Children configurations | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.booking_itinerary_room_configuration_agent import BookingItineraryRoomConfigurationAgent

# TODO update the JSON string below
json = "{}"
# create an instance of BookingItineraryRoomConfigurationAgent from a JSON string
booking_itinerary_room_configuration_agent_instance = BookingItineraryRoomConfigurationAgent.from_json(json)
# print the JSON string representation of the object
print(BookingItineraryRoomConfigurationAgent.to_json())

# convert the object into a dict
booking_itinerary_room_configuration_agent_dict = booking_itinerary_room_configuration_agent_instance.to_dict()
# create an instance of BookingItineraryRoomConfigurationAgent from a dict
booking_itinerary_room_configuration_agent_from_dict = BookingItineraryRoomConfigurationAgent.from_dict(booking_itinerary_room_configuration_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


