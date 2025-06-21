# ProfileLightweightSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_identifier** | **str** | Profile identifier | 
**user_identifier** | **str** | User identifier | 
**share** | **bool** | Indicates whether the user wants to share this profile of themselves with hotel(s) | 
**user** | [**ProfileUserSupplier**](ProfileUserSupplier.md) | User details | 
**personal** | [**PersonalSupplier**](PersonalSupplier.md) | Detailed customer information for this profile | 
**preferences** | [**PreferencesSupplier**](PreferencesSupplier.md) | Customer preferences | 

## Example

```python
from wink_sdk_extranet_booking.models.profile_lightweight_supplier import ProfileLightweightSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileLightweightSupplier from a JSON string
profile_lightweight_supplier_instance = ProfileLightweightSupplier.from_json(json)
# print the JSON string representation of the object
print(ProfileLightweightSupplier.to_json())

# convert the object into a dict
profile_lightweight_supplier_dict = profile_lightweight_supplier_instance.to_dict()
# create an instance of ProfileLightweightSupplier from a dict
profile_lightweight_supplier_from_dict = ProfileLightweightSupplier.from_dict(profile_lightweight_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


