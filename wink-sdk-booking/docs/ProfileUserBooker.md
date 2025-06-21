# ProfileUserBooker


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
from wink_sdk_booking.models.profile_user_booker import ProfileUserBooker

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileUserBooker from a JSON string
profile_user_booker_instance = ProfileUserBooker.from_json(json)
# print the JSON string representation of the object
print(ProfileUserBooker.to_json())

# convert the object into a dict
profile_user_booker_dict = profile_user_booker_instance.to_dict()
# create an instance of ProfileUserBooker from a dict
profile_user_booker_from_dict = ProfileUserBooker.from_dict(profile_user_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


