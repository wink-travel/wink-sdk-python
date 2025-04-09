# SocialAgent

Social network

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of social network. | [optional] 
**location** | **str** | URL or social network identifier to social network profile | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.social_agent import SocialAgent

# TODO update the JSON string below
json = "{}"
# create an instance of SocialAgent from a JSON string
social_agent_instance = SocialAgent.from_json(json)
# print the JSON string representation of the object
print(SocialAgent.to_json())

# convert the object into a dict
social_agent_dict = social_agent_instance.to_dict()
# create an instance of SocialAgent from a dict
social_agent_from_dict = SocialAgent.from_dict(social_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


