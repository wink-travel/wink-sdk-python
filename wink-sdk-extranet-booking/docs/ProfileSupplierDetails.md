# ProfileSupplierDetails

Optional profile record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_identifier** | **str** | Profile identifier | 
**user_identifier** | **str** | User identifier | 
**share** | **bool** | Indicates whether the user wants to share this profile of themselves with hotel(s) | 
**user** | [**ProfileUserSupplierDetails**](ProfileUserSupplierDetails.md) |  | 
**personal** | [**PersonalSupplierDetails**](PersonalSupplierDetails.md) |  | 
**preferences** | [**PreferencesSupplierDetails**](PreferencesSupplierDetails.md) |  | 

## Example

```python
from wink_sdk_extranet_booking.models.profile_supplier_details import ProfileSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileSupplierDetails from a JSON string
profile_supplier_details_instance = ProfileSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(ProfileSupplierDetails.to_json())

# convert the object into a dict
profile_supplier_details_dict = profile_supplier_details_instance.to_dict()
# create an instance of ProfileSupplierDetails from a dict
profile_supplier_details_from_dict = ProfileSupplierDetails.from_dict(profile_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


