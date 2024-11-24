# BookingCancellableSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel_identifier** | **str** | Owner identifier of booking. | 
**booking_identifier** | **str** | Booking unique identifier. | 
**cancellable** | **bool** | Whether booking can be cancelled or not. | 

## Example

```python
from wink_sdk_extranet_booking.models.booking_cancellable_supplier import BookingCancellableSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of BookingCancellableSupplier from a JSON string
booking_cancellable_supplier_instance = BookingCancellableSupplier.from_json(json)
# print the JSON string representation of the object
print(BookingCancellableSupplier.to_json())

# convert the object into a dict
booking_cancellable_supplier_dict = booking_cancellable_supplier_instance.to_dict()
# create an instance of BookingCancellableSupplier from a dict
booking_cancellable_supplier_from_dict = BookingCancellableSupplier.from_dict(booking_cancellable_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


