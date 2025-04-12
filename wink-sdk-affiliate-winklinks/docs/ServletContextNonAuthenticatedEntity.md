# ServletContextNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_loader** | [**ApplicationContextNonAuthenticatedEntityClassLoaderParent**](ApplicationContextNonAuthenticatedEntityClassLoaderParent.md) |  | [optional] 
**major_version** | **int** |  | [optional] 
**minor_version** | **int** |  | [optional] 
**default_session_tracking_modes** | **List[str]** |  | [optional] 
**effective_major_version** | **int** |  | [optional] 
**effective_minor_version** | **int** |  | [optional] 
**server_info** | **str** |  | [optional] 
**servlet_context_name** | **str** |  | [optional] 
**servlet_registrations** | [**Dict[str, ServletRegistrationNonAuthenticatedEntity]**](ServletRegistrationNonAuthenticatedEntity.md) |  | [optional] 
**filter_registrations** | [**Dict[str, FilterRegistrationNonAuthenticatedEntity]**](FilterRegistrationNonAuthenticatedEntity.md) |  | [optional] 
**effective_session_tracking_modes** | **List[str]** |  | [optional] 
**jsp_config_descriptor** | [**JspConfigDescriptorNonAuthenticatedEntity**](JspConfigDescriptorNonAuthenticatedEntity.md) |  | [optional] 
**virtual_server_name** | **str** |  | [optional] 
**session_timeout** | **int** |  | [optional] 
**request_character_encoding** | **str** |  | [optional] 
**response_character_encoding** | **str** |  | [optional] 
**attribute_names** | **object** |  | [optional] 
**context_path** | **str** |  | [optional] 
**init_parameter_names** | **object** |  | [optional] 
**session_tracking_modes** | **List[str]** |  | [optional] 
**session_cookie_config** | [**SessionCookieConfigNonAuthenticatedEntity**](SessionCookieConfigNonAuthenticatedEntity.md) |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.servlet_context_non_authenticated_entity import ServletContextNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ServletContextNonAuthenticatedEntity from a JSON string
servlet_context_non_authenticated_entity_instance = ServletContextNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ServletContextNonAuthenticatedEntity.to_json())

# convert the object into a dict
servlet_context_non_authenticated_entity_dict = servlet_context_non_authenticated_entity_instance.to_dict()
# create an instance of ServletContextNonAuthenticatedEntity from a dict
servlet_context_non_authenticated_entity_from_dict = ServletContextNonAuthenticatedEntity.from_dict(servlet_context_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


