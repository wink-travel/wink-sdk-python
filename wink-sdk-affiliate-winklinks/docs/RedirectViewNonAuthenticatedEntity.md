# RedirectViewNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_context** | [**ApplicationContextNonAuthenticatedEntity**](ApplicationContextNonAuthenticatedEntity.md) |  | [optional] 
**servlet_context** | [**ServletContextNonAuthenticatedEntity**](ServletContextNonAuthenticatedEntity.md) |  | [optional] 
**content_type** | **str** |  | [optional] 
**request_context_attribute** | **str** |  | [optional] 
**static_attributes** | **Dict[str, object]** |  | [optional] 
**expose_path_variables** | **bool** |  | [optional] 
**expose_context_beans_as_attributes** | **bool** |  | [optional] 
**exposed_context_bean_names** | **List[str]** |  | [optional] 
**bean_name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**context_relative** | **bool** |  | [optional] 
**http10_compatible** | **bool** |  | [optional] 
**expose_model_attributes** | **bool** |  | [optional] 
**encoding_scheme** | **str** |  | [optional] 
**status_code** | [**HttpStatusCodeNonAuthenticatedEntity**](HttpStatusCodeNonAuthenticatedEntity.md) |  | [optional] 
**expand_uri_template_variables** | **bool** |  | [optional] 
**propagate_query_params** | **bool** |  | [optional] 
**hosts** | **List[str]** |  | [optional] 
**redirect_view** | **bool** |  | [optional] 
**propagate_query_properties** | **bool** |  | [optional] 
**attributes** | **Dict[str, str]** |  | [optional] 
**attributes_map** | **Dict[str, object]** |  | [optional] 
**attributes_csv** | **str** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.redirect_view_non_authenticated_entity import RedirectViewNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of RedirectViewNonAuthenticatedEntity from a JSON string
redirect_view_non_authenticated_entity_instance = RedirectViewNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(RedirectViewNonAuthenticatedEntity.to_json())

# convert the object into a dict
redirect_view_non_authenticated_entity_dict = redirect_view_non_authenticated_entity_instance.to_dict()
# create an instance of RedirectViewNonAuthenticatedEntity from a dict
redirect_view_non_authenticated_entity_from_dict = RedirectViewNonAuthenticatedEntity.from_dict(redirect_view_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


