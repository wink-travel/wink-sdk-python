# ProfileLightweightSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_identifier** | **str** | Profile identifier | 
**user_identifier** | **str** | User identifier | 
**share** | **bool** | Indicates whether the user wants to share this profile of themselves with hotel(s) | 
**user** | [**ProfileUserSupplierDetails**](ProfileUserSupplierDetails.md) | User details | 
**personal** | [**PersonalSupplierDetails**](PersonalSupplierDetails.md) | Detailed customer information for this profile | 
**preferences** | [**PreferencesSupplierDetails**](PreferencesSupplierDetails.md) | Customer preferences | 

## Example

```python
from wink_sdk_extranet_booking.models.profile_lightweight_supplier_details import ProfileLightweightSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileLightweightSupplierDetails from a JSON string
profile_lightweight_supplier_details_instance = ProfileLightweightSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(ProfileLightweightSupplierDetails.to_json())

# convert the object into a dict
profile_lightweight_supplier_details_dict = profile_lightweight_supplier_details_instance.to_dict()
# create an instance of ProfileLightweightSupplierDetails from a dict
profile_lightweight_supplier_details_from_dict = ProfileLightweightSupplierDetails.from_dict(profile_lightweight_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


