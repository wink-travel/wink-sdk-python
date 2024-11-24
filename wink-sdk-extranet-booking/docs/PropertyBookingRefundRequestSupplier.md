# PropertyBookingRefundRequestSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of reason | 
**description** | **str** | Textual description of why the refund is being requested | 
**refund** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | 
**cancel_on_refund** | **str** | Whether to cancel the booking alongside requesting a refund. | 

## Example

```python
from wink_sdk_extranet_booking.models.property_booking_refund_request_supplier import PropertyBookingRefundRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyBookingRefundRequestSupplier from a JSON string
property_booking_refund_request_supplier_instance = PropertyBookingRefundRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(PropertyBookingRefundRequestSupplier.to_json())

# convert the object into a dict
property_booking_refund_request_supplier_dict = property_booking_refund_request_supplier_instance.to_dict()
# create an instance of PropertyBookingRefundRequestSupplier from a dict
property_booking_refund_request_supplier_from_dict = PropertyBookingRefundRequestSupplier.from_dict(property_booking_refund_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


