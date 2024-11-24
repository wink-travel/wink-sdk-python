# BookingTestNotificationSupplierDetails

Notification options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notify_property** | **bool** | Whether to notify property of booking | [optional] 
**notify_channel_manager** | **bool** | Whether to notify channel manager of booking | [optional] 
**notify_booker** | **bool** | Whether to notify booker of booking | [optional] 
**booker** | [**BookingUserSupplierDetails**](BookingUserSupplierDetails.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.booking_test_notification_supplier_details import BookingTestNotificationSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BookingTestNotificationSupplierDetails from a JSON string
booking_test_notification_supplier_details_instance = BookingTestNotificationSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(BookingTestNotificationSupplierDetails.to_json())

# convert the object into a dict
booking_test_notification_supplier_details_dict = booking_test_notification_supplier_details_instance.to_dict()
# create an instance of BookingTestNotificationSupplierDetails from a dict
booking_test_notification_supplier_details_from_dict = BookingTestNotificationSupplierDetails.from_dict(booking_test_notification_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


