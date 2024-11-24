# BookingItineraryRoomConfigurationChildBooker

Child configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | Number of children | 
**age** | **int** | Age of children | 

## Example

```python
from wink_sdk_booking.models.booking_itinerary_room_configuration_child_booker import BookingItineraryRoomConfigurationChildBooker

# TODO update the JSON string below
json = "{}"
# create an instance of BookingItineraryRoomConfigurationChildBooker from a JSON string
booking_itinerary_room_configuration_child_booker_instance = BookingItineraryRoomConfigurationChildBooker.from_json(json)
# print the JSON string representation of the object
print(BookingItineraryRoomConfigurationChildBooker.to_json())

# convert the object into a dict
booking_itinerary_room_configuration_child_booker_dict = booking_itinerary_room_configuration_child_booker_instance.to_dict()
# create an instance of BookingItineraryRoomConfigurationChildBooker from a dict
booking_itinerary_room_configuration_child_booker_from_dict = BookingItineraryRoomConfigurationChildBooker.from_dict(booking_itinerary_room_configuration_child_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


