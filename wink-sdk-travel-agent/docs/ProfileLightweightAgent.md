# ProfileLightweightAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_identifier** | **str** | Profile identifier | 
**user_identifier** | **str** | User identifier | 
**share** | **bool** | Indicates whether the user wants to share this profile of themselves with hotel(s) | 
**user** | [**ProfileUserAgent**](ProfileUserAgent.md) | User details | 
**personal** | [**PersonalAgent**](PersonalAgent.md) | Detailed customer information for this profile | 
**preferences** | [**PreferencesAgent**](PreferencesAgent.md) | Customer preferences | 

## Example

```python
from wink_sdk_travel_agent.models.profile_lightweight_agent import ProfileLightweightAgent

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileLightweightAgent from a JSON string
profile_lightweight_agent_instance = ProfileLightweightAgent.from_json(json)
# print the JSON string representation of the object
print(ProfileLightweightAgent.to_json())

# convert the object into a dict
profile_lightweight_agent_dict = profile_lightweight_agent_instance.to_dict()
# create an instance of ProfileLightweightAgent from a dict
profile_lightweight_agent_from_dict = ProfileLightweightAgent.from_dict(profile_lightweight_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


