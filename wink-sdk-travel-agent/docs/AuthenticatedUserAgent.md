# AuthenticatedUserAgent

The authenticated user ID that made the request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_identifier** | **str** | User identifier | [optional] 
**first_name** | **str** | First name | 
**last_name** | **str** | Last name | 
**email** | **str** | Email | 
**full_name** | **str** | Full name | [optional] [readonly] 

## Example

```python
from wink_sdk_travel_agent.models.authenticated_user_agent import AuthenticatedUserAgent

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatedUserAgent from a JSON string
authenticated_user_agent_instance = AuthenticatedUserAgent.from_json(json)
# print the JSON string representation of the object
print(AuthenticatedUserAgent.to_json())

# convert the object into a dict
authenticated_user_agent_dict = authenticated_user_agent_instance.to_dict()
# create an instance of AuthenticatedUserAgent from a dict
authenticated_user_agent_from_dict = AuthenticatedUserAgent.from_dict(authenticated_user_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


