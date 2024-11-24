# ProfileUserAgent

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
from wink_sdk_travel_agent.models.profile_user_agent import ProfileUserAgent

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileUserAgent from a JSON string
profile_user_agent_instance = ProfileUserAgent.from_json(json)
# print the JSON string representation of the object
print(ProfileUserAgent.to_json())

# convert the object into a dict
profile_user_agent_dict = profile_user_agent_instance.to_dict()
# create an instance of ProfileUserAgent from a dict
profile_user_agent_from_dict = ProfileUserAgent.from_dict(profile_user_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


