# RedirectViewStatusCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **bool** |  | [optional] 
**is4xx_client_error** | **bool** |  | [optional] 
**is5xx_server_error** | **bool** |  | [optional] 
**is1xx_informational** | **bool** |  | [optional] 
**is2xx_successful** | **bool** |  | [optional] 
**is3xx_redirection** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.redirect_view_status_code import RedirectViewStatusCode

# TODO update the JSON string below
json = "{}"
# create an instance of RedirectViewStatusCode from a JSON string
redirect_view_status_code_instance = RedirectViewStatusCode.from_json(json)
# print the JSON string representation of the object
print(RedirectViewStatusCode.to_json())

# convert the object into a dict
redirect_view_status_code_dict = redirect_view_status_code_instance.to_dict()
# create an instance of RedirectViewStatusCode from a dict
redirect_view_status_code_from_dict = RedirectViewStatusCode.from_dict(redirect_view_status_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


