# BookingUserSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_identifier** | **str** | User identifier | [optional] 
**first_name** | **str** | First name | 
**last_name** | **str** | Last name | 
**email** | **str** | Email | 
**telephone** | **str** | Telephone | [optional] 
**full_name** | **str** | Full name | [optional] [readonly] 

## Example

```python
from wink_sdk_extranet_booking.models.booking_user_supplier_details import BookingUserSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BookingUserSupplierDetails from a JSON string
booking_user_supplier_details_instance = BookingUserSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(BookingUserSupplierDetails.to_json())

# convert the object into a dict
booking_user_supplier_details_dict = booking_user_supplier_details_instance.to_dict()
# create an instance of BookingUserSupplierDetails from a dict
booking_user_supplier_details_from_dict = BookingUserSupplierDetails.from_dict(booking_user_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


