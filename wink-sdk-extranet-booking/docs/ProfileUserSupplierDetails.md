# ProfileUserSupplierDetails

User details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last name | [optional] 
**email** | **str** | Email | [optional] 
**phone** | **str** | Telephone | [optional] 
**profile_picture_url** | **str** | Profile picture URL | [optional] 
**full_name** | **str** | Full name | [optional] [readonly] 

## Example

```python
from wink_sdk_extranet_booking.models.profile_user_supplier_details import ProfileUserSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileUserSupplierDetails from a JSON string
profile_user_supplier_details_instance = ProfileUserSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(ProfileUserSupplierDetails.to_json())

# convert the object into a dict
profile_user_supplier_details_dict = profile_user_supplier_details_instance.to_dict()
# create an instance of ProfileUserSupplierDetails from a dict
profile_user_supplier_details_from_dict = ProfileUserSupplierDetails.from_dict(profile_user_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


