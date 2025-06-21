# GuestUserSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_identifier** | **str** | User identifier | [optional] 
**first_name** | **str** | First name | 
**last_name** | **str** | Last name | 
**email** | **str** | Email | 
**telephone** | **str** | Telephone | [optional] 
**profile** | [**ProfileLightweightSupplier**](ProfileLightweightSupplier.md) | Optional profile record | [optional] 
**full_name** | **str** | Full name | [optional] [readonly] 

## Example

```python
from wink_sdk_extranet_booking.models.guest_user_supplier import GuestUserSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of GuestUserSupplier from a JSON string
guest_user_supplier_instance = GuestUserSupplier.from_json(json)
# print the JSON string representation of the object
print(GuestUserSupplier.to_json())

# convert the object into a dict
guest_user_supplier_dict = guest_user_supplier_instance.to_dict()
# create an instance of GuestUserSupplier from a dict
guest_user_supplier_from_dict = GuestUserSupplier.from_dict(guest_user_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


