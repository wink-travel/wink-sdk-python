# BookingUserSupplier


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
from wink_sdk_extranet_booking.models.booking_user_supplier import BookingUserSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of BookingUserSupplier from a JSON string
booking_user_supplier_instance = BookingUserSupplier.from_json(json)
# print the JSON string representation of the object
print(BookingUserSupplier.to_json())

# convert the object into a dict
booking_user_supplier_dict = booking_user_supplier_instance.to_dict()
# create an instance of BookingUserSupplier from a dict
booking_user_supplier_from_dict = BookingUserSupplier.from_dict(booking_user_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


