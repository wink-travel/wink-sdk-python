# ProfileAgent

Optional profile record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_identifier** | **str** | Profile identifier | 
**user_identifier** | **str** | User identifier | 
**share** | **bool** | Indicates whether the user wants to share this profile of themselves with hotel(s) | 
**user** | [**ProfileUserAgent**](ProfileUserAgent.md) |  | 
**personal** | [**PersonalAgent**](PersonalAgent.md) |  | 
**preferences** | [**PreferencesAgent**](PreferencesAgent.md) |  | 

## Example

```python
from wink_sdk_travel_agent.models.profile_agent import ProfileAgent

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileAgent from a JSON string
profile_agent_instance = ProfileAgent.from_json(json)
# print the JSON string representation of the object
print(ProfileAgent.to_json())

# convert the object into a dict
profile_agent_dict = profile_agent_instance.to_dict()
# create an instance of ProfileAgent from a dict
profile_agent_from_dict = ProfileAgent.from_dict(profile_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


