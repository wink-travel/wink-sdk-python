# BookingItineraryRoomConfigurationSupplierDetails

Room Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adults** | **int** | Number of adults | [default to 1]
**children** | [**List[BookingItineraryRoomConfigurationChildSupplierDetails]**](BookingItineraryRoomConfigurationChildSupplierDetails.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.booking_itinerary_room_configuration_supplier_details import BookingItineraryRoomConfigurationSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BookingItineraryRoomConfigurationSupplierDetails from a JSON string
booking_itinerary_room_configuration_supplier_details_instance = BookingItineraryRoomConfigurationSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(BookingItineraryRoomConfigurationSupplierDetails.to_json())

# convert the object into a dict
booking_itinerary_room_configuration_supplier_details_dict = booking_itinerary_room_configuration_supplier_details_instance.to_dict()
# create an instance of BookingItineraryRoomConfigurationSupplierDetails from a dict
booking_itinerary_room_configuration_supplier_details_from_dict = BookingItineraryRoomConfigurationSupplierDetails.from_dict(booking_itinerary_room_configuration_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


