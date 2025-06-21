# BookingItineraryRoomConfigurationSupplier

Room Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adults** | **int** | Number of adults | [default to 1]
**children** | [**List[BookingItineraryRoomConfigurationChildSupplier]**](BookingItineraryRoomConfigurationChildSupplier.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.booking_itinerary_room_configuration_supplier import BookingItineraryRoomConfigurationSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of BookingItineraryRoomConfigurationSupplier from a JSON string
booking_itinerary_room_configuration_supplier_instance = BookingItineraryRoomConfigurationSupplier.from_json(json)
# print the JSON string representation of the object
print(BookingItineraryRoomConfigurationSupplier.to_json())

# convert the object into a dict
booking_itinerary_room_configuration_supplier_dict = booking_itinerary_room_configuration_supplier_instance.to_dict()
# create an instance of BookingItineraryRoomConfigurationSupplier from a dict
booking_itinerary_room_configuration_supplier_from_dict = BookingItineraryRoomConfigurationSupplier.from_dict(booking_itinerary_room_configuration_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


