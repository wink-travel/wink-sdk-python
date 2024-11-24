# BookingUserSessionSupplier

User session information containing itinerary and other user related data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**itinerary** | [**BookingItinerarySupplier**](BookingItinerarySupplier.md) |  | 
**language** | **str** | User&#39;s language preference | [optional] 
**currency** | **str** | User&#39;s currency preference | [optional] 
**promotional_codes** | **List[str]** |  | [optional] 
**selected_room_configuration_index** | **int** | User can pass the current room configuration index to retrieve rates specifically for that room configuration. | [optional] 
**lifestyle** | **str** | The preferred user lifestyle. | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.booking_user_session_supplier import BookingUserSessionSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of BookingUserSessionSupplier from a JSON string
booking_user_session_supplier_instance = BookingUserSessionSupplier.from_json(json)
# print the JSON string representation of the object
print(BookingUserSessionSupplier.to_json())

# convert the object into a dict
booking_user_session_supplier_dict = booking_user_session_supplier_instance.to_dict()
# create an instance of BookingUserSessionSupplier from a dict
booking_user_session_supplier_from_dict = BookingUserSessionSupplier.from_dict(booking_user_session_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


