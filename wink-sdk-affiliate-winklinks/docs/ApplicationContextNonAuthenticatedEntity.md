# ApplicationContextNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent** | **object** |  | [optional] 
**id** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**application_name** | **str** |  | [optional] 
**startup_date** | **int** |  | [optional] 
**autowire_capable_bean_factory** | **object** |  | [optional] 
**environment** | [**EnvironmentNonAuthenticatedEntity**](EnvironmentNonAuthenticatedEntity.md) |  | [optional] 
**bean_definition_count** | **int** |  | [optional] 
**bean_definition_names** | **List[str]** |  | [optional] 
**parent_bean_factory** | **object** |  | [optional] 
**class_loader** | [**ApplicationContextNonAuthenticatedEntityClassLoader**](ApplicationContextNonAuthenticatedEntityClassLoader.md) |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.application_context_non_authenticated_entity import ApplicationContextNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationContextNonAuthenticatedEntity from a JSON string
application_context_non_authenticated_entity_instance = ApplicationContextNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ApplicationContextNonAuthenticatedEntity.to_json())

# convert the object into a dict
application_context_non_authenticated_entity_dict = application_context_non_authenticated_entity_instance.to_dict()
# create an instance of ApplicationContextNonAuthenticatedEntity from a dict
application_context_non_authenticated_entity_from_dict = ApplicationContextNonAuthenticatedEntity.from_dict(application_context_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


