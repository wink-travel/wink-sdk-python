# BookingItineraryRoomConfigurationChildAgent

Child configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | Number of children | 
**age** | **int** | Age of children | 

## Example

```python
from wink_sdk_travel_agent.models.booking_itinerary_room_configuration_child_agent import BookingItineraryRoomConfigurationChildAgent

# TODO update the JSON string below
json = "{}"
# create an instance of BookingItineraryRoomConfigurationChildAgent from a JSON string
booking_itinerary_room_configuration_child_agent_instance = BookingItineraryRoomConfigurationChildAgent.from_json(json)
# print the JSON string representation of the object
print(BookingItineraryRoomConfigurationChildAgent.to_json())

# convert the object into a dict
booking_itinerary_room_configuration_child_agent_dict = booking_itinerary_room_configuration_child_agent_instance.to_dict()
# create an instance of BookingItineraryRoomConfigurationChildAgent from a dict
booking_itinerary_room_configuration_child_agent_from_dict = BookingItineraryRoomConfigurationChildAgent.from_dict(booking_itinerary_room_configuration_child_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


