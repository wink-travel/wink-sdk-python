# UpsertUserProfileRequest

User profile information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name | 
**last_name** | **str** | Last name | 
**username** | **str** | Unique user email | 
**profile_picture** | [**SimpleMultimedia**](SimpleMultimedia.md) | Profile picture that originates from a Cloudinary upload | [optional] 

## Example

```python
from wink_sdk_user_settings.models.upsert_user_profile_request import UpsertUserProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertUserProfileRequest from a JSON string
upsert_user_profile_request_instance = UpsertUserProfileRequest.from_json(json)
# print the JSON string representation of the object
print(UpsertUserProfileRequest.to_json())

# convert the object into a dict
upsert_user_profile_request_dict = upsert_user_profile_request_instance.to_dict()
# create an instance of UpsertUserProfileRequest from a dict
upsert_user_profile_request_from_dict = UpsertUserProfileRequest.from_dict(upsert_user_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


