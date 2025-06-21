# GuestUserAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_identifier** | **str** | User identifier | [optional] 
**first_name** | **str** | First name | 
**last_name** | **str** | Last name | 
**email** | **str** | Email | 
**telephone** | **str** | Telephone | [optional] 
**profile** | [**ProfileLightweightAgent**](ProfileLightweightAgent.md) | Optional profile record | [optional] 
**full_name** | **str** | Full name | [optional] [readonly] 

## Example

```python
from wink_sdk_travel_agent.models.guest_user_agent import GuestUserAgent

# TODO update the JSON string below
json = "{}"
# create an instance of GuestUserAgent from a JSON string
guest_user_agent_instance = GuestUserAgent.from_json(json)
# print the JSON string representation of the object
print(GuestUserAgent.to_json())

# convert the object into a dict
guest_user_agent_dict = guest_user_agent_instance.to_dict()
# create an instance of GuestUserAgent from a dict
guest_user_agent_from_dict = GuestUserAgent.from_dict(guest_user_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


