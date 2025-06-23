# ServletContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_loader** | [**ApplicationContextClassLoaderParent**](ApplicationContextClassLoaderParent.md) |  | [optional] 
**major_version** | **int** |  | [optional] 
**minor_version** | **int** |  | [optional] 
**session_tracking_modes** | **List[str]** |  | [optional] 
**init_parameter_names** | **object** |  | [optional] 
**attribute_names** | **object** |  | [optional] 
**context_path** | **str** |  | [optional] 
**servlet_context_name** | **str** |  | [optional] 
**effective_major_version** | **int** |  | [optional] 
**effective_minor_version** | **int** |  | [optional] 
**server_info** | **str** |  | [optional] 
**session_cookie_config** | [**SessionCookieConfig**](SessionCookieConfig.md) |  | [optional] 
**session_timeout** | **int** |  | [optional] 
**servlet_registrations** | [**Dict[str, ServletRegistration]**](ServletRegistration.md) |  | [optional] 
**default_session_tracking_modes** | **List[str]** |  | [optional] 
**filter_registrations** | [**Dict[str, FilterRegistration]**](FilterRegistration.md) |  | [optional] 
**effective_session_tracking_modes** | **List[str]** |  | [optional] 
**jsp_config_descriptor** | [**JspConfigDescriptor**](JspConfigDescriptor.md) |  | [optional] 
**virtual_server_name** | **str** |  | [optional] 
**request_character_encoding** | **str** |  | [optional] 
**response_character_encoding** | **str** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.servlet_context import ServletContext

# TODO update the JSON string below
json = "{}"
# create an instance of ServletContext from a JSON string
servlet_context_instance = ServletContext.from_json(json)
# print the JSON string representation of the object
print(ServletContext.to_json())

# convert the object into a dict
servlet_context_dict = servlet_context_instance.to_dict()
# create an instance of ServletContext from a dict
servlet_context_from_dict = ServletContext.from_dict(servlet_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


