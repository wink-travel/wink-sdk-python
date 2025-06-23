# SessionCookieConfig


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
from wink_sdk_affiliate_winklinks.models.session_cookie_config import SessionCookieConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SessionCookieConfig from a JSON string
session_cookie_config_instance = SessionCookieConfig.from_json(json)
# print the JSON string representation of the object
print(SessionCookieConfig.to_json())

# convert the object into a dict
session_cookie_config_dict = session_cookie_config_instance.to_dict()
# create an instance of SessionCookieConfig from a dict
session_cookie_config_from_dict = SessionCookieConfig.from_dict(session_cookie_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


