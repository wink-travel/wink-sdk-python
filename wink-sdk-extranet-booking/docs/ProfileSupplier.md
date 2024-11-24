# ProfileSupplier

Optional profile record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_identifier** | **str** | Profile identifier | 
**user_identifier** | **str** | User identifier | 
**share** | **bool** | Indicates whether the user wants to share this profile of themselves with hotel(s) | 
**user** | [**ProfileUserSupplier**](ProfileUserSupplier.md) |  | 
**personal** | [**PersonalSupplier**](PersonalSupplier.md) |  | 
**preferences** | [**PreferencesSupplier**](PreferencesSupplier.md) |  | 

## Example

```python
from wink_sdk_extranet_booking.models.profile_supplier import ProfileSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileSupplier from a JSON string
profile_supplier_instance = ProfileSupplier.from_json(json)
# print the JSON string representation of the object
print(ProfileSupplier.to_json())

# convert the object into a dict
profile_supplier_dict = profile_supplier_instance.to_dict()
# create an instance of ProfileSupplier from a dict
profile_supplier_from_dict = ProfileSupplier.from_dict(profile_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


