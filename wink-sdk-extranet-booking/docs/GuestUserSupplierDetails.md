# GuestUserSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_identifier** | **str** | User identifier | [optional] 
**first_name** | **str** | First name | 
**last_name** | **str** | Last name | 
**email** | **str** | Email | 
**telephone** | **str** | Telephone | [optional] 
**profile** | [**ProfileLightweightSupplierDetails**](ProfileLightweightSupplierDetails.md) | Optional profile record | [optional] 
**full_name** | **str** | Full name | [optional] [readonly] 

## Example

```python
from wink_sdk_extranet_booking.models.guest_user_supplier_details import GuestUserSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GuestUserSupplierDetails from a JSON string
guest_user_supplier_details_instance = GuestUserSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(GuestUserSupplierDetails.to_json())

# convert the object into a dict
guest_user_supplier_details_dict = guest_user_supplier_details_instance.to_dict()
# create an instance of GuestUserSupplierDetails from a dict
guest_user_supplier_details_from_dict = GuestUserSupplierDetails.from_dict(guest_user_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


