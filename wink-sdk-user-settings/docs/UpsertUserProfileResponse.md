# UpsertUserProfileResponse

User profile information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | User ID | 
**first_name** | **str** | First name | 
**last_name** | **str** | Last name | 
**username** | **str** | Unique user email | 
**profile_picture** | [**SimpleMultimedia**](SimpleMultimedia.md) |  | [optional] 
**profile_picture_url** | **str** | A fully qualified URL based on the Cloudinary identifier | [optional] 

## Example

```python
from wink_sdk_user_settings.models.upsert_user_profile_response import UpsertUserProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertUserProfileResponse from a JSON string
upsert_user_profile_response_instance = UpsertUserProfileResponse.from_json(json)
# print the JSON string representation of the object
print(UpsertUserProfileResponse.to_json())

# convert the object into a dict
upsert_user_profile_response_dict = upsert_user_profile_response_instance.to_dict()
# create an instance of UpsertUserProfileResponse from a dict
upsert_user_profile_response_from_dict = UpsertUserProfileResponse.from_dict(upsert_user_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


