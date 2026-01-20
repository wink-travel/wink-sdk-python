# ProfileLightweightBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_identifier** | **UUID** | Profile identifier | 
**user_identifier** | **UUID** | User identifier | 
**share** | **bool** | Indicates whether the user wants to share this profile of themselves with hotel(s) | 
**user** | [**ProfileUserBooker**](ProfileUserBooker.md) | User details | 
**personal** | [**PersonalBooker**](PersonalBooker.md) | Detailed customer information for this profile | 
**preferences** | [**PreferencesBooker**](PreferencesBooker.md) | Customer preferences | 

## Example

```python
from wink_sdk_booking.models.profile_lightweight_booker import ProfileLightweightBooker

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileLightweightBooker from a JSON string
profile_lightweight_booker_instance = ProfileLightweightBooker.from_json(json)
# print the JSON string representation of the object
print(ProfileLightweightBooker.to_json())

# convert the object into a dict
profile_lightweight_booker_dict = profile_lightweight_booker_instance.to_dict()
# create an instance of ProfileLightweightBooker from a dict
profile_lightweight_booker_from_dict = ProfileLightweightBooker.from_dict(profile_lightweight_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


