# SessionCookieConfigNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**attributes** | **Dict[str, str]** |  | [optional] 
**comment** | **str** |  | [optional] 
**secure** | **bool** |  | [optional] 
**max_age** | **int** |  | [optional] 
**http_only** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.session_cookie_config_non_authenticated_entity import SessionCookieConfigNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SessionCookieConfigNonAuthenticatedEntity from a JSON string
session_cookie_config_non_authenticated_entity_instance = SessionCookieConfigNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SessionCookieConfigNonAuthenticatedEntity.to_json())

# convert the object into a dict
session_cookie_config_non_authenticated_entity_dict = session_cookie_config_non_authenticated_entity_instance.to_dict()
# create an instance of SessionCookieConfigNonAuthenticatedEntity from a dict
session_cookie_config_non_authenticated_entity_from_dict = SessionCookieConfigNonAuthenticatedEntity.from_dict(session_cookie_config_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


