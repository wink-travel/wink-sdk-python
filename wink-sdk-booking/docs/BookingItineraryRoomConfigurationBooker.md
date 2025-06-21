# BookingItineraryRoomConfigurationBooker

Room Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adults** | **int** | Number of adults | [default to 1]
**children** | [**List[BookingItineraryRoomConfigurationChildBooker]**](BookingItineraryRoomConfigurationChildBooker.md) |  | [optional] 

## Example

```python
from wink_sdk_booking.models.booking_itinerary_room_configuration_booker import BookingItineraryRoomConfigurationBooker

# TODO update the JSON string below
json = "{}"
# create an instance of BookingItineraryRoomConfigurationBooker from a JSON string
booking_itinerary_room_configuration_booker_instance = BookingItineraryRoomConfigurationBooker.from_json(json)
# print the JSON string representation of the object
print(BookingItineraryRoomConfigurationBooker.to_json())

# convert the object into a dict
booking_itinerary_room_configuration_booker_dict = booking_itinerary_room_configuration_booker_instance.to_dict()
# create an instance of BookingItineraryRoomConfigurationBooker from a dict
booking_itinerary_room_configuration_booker_from_dict = BookingItineraryRoomConfigurationBooker.from_dict(booking_itinerary_room_configuration_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


