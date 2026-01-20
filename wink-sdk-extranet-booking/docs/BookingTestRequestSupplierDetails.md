# BookingTestRequestSupplierDetails

Test booking request body for property ID

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**VerifyRatesRequestSupplierDetails**](VerifyRatesRequestSupplierDetails.md) | Query object that was used to generate the room property | 
**room** | [**RoomConfigurationPriceSupplierDetails**](RoomConfigurationPriceSupplierDetails.md) | The room we want to book | 
**notification** | [**BookingTestNotificationSupplierDetails**](BookingTestNotificationSupplierDetails.md) | Notification options | 

## Example

```python
from wink_sdk_extranet_booking.models.booking_test_request_supplier_details import BookingTestRequestSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BookingTestRequestSupplierDetails from a JSON string
booking_test_request_supplier_details_instance = BookingTestRequestSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(BookingTestRequestSupplierDetails.to_json())

# convert the object into a dict
booking_test_request_supplier_details_dict = booking_test_request_supplier_details_instance.to_dict()
# create an instance of BookingTestRequestSupplierDetails from a dict
booking_test_request_supplier_details_from_dict = BookingTestRequestSupplierDetails.from_dict(booking_test_request_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


