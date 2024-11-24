# ProfileBooker

Optional profile record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_identifier** | **str** | Profile identifier | 
**user_identifier** | **str** | User identifier | 
**share** | **bool** | Indicates whether the user wants to share this profile of themselves with hotel(s) | 
**user** | [**ProfileUserBooker**](ProfileUserBooker.md) |  | 
**personal** | [**PersonalBooker**](PersonalBooker.md) |  | 
**preferences** | [**PreferencesBooker**](PreferencesBooker.md) |  | 

## Example

```python
from wink_sdk_booking.models.profile_booker import ProfileBooker

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileBooker from a JSON string
profile_booker_instance = ProfileBooker.from_json(json)
# print the JSON string representation of the object
print(ProfileBooker.to_json())

# convert the object into a dict
profile_booker_dict = profile_booker_instance.to_dict()
# create an instance of ProfileBooker from a dict
profile_booker_from_dict = ProfileBooker.from_dict(profile_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


