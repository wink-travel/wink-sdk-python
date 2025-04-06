# ApplicationContextNonAuthenticatedEntityClassLoaderParent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**registered_as_parallel_capable** | **bool** |  | [optional] 
**unnamed_module** | [**ApplicationContextNonAuthenticatedEntityClassLoaderParentUnnamedModule**](ApplicationContextNonAuthenticatedEntityClassLoaderParentUnnamedModule.md) |  | [optional] 
**defined_packages** | [**List[ApplicationContextNonAuthenticatedEntityClassLoaderParentUnnamedModuleClassLoaderDefinedPackagesInner]**](ApplicationContextNonAuthenticatedEntityClassLoaderParentUnnamedModuleClassLoaderDefinedPackagesInner.md) |  | [optional] 
**default_assertion_status** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.application_context_non_authenticated_entity_class_loader_parent import ApplicationContextNonAuthenticatedEntityClassLoaderParent

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationContextNonAuthenticatedEntityClassLoaderParent from a JSON string
application_context_non_authenticated_entity_class_loader_parent_instance = ApplicationContextNonAuthenticatedEntityClassLoaderParent.from_json(json)
# print the JSON string representation of the object
print(ApplicationContextNonAuthenticatedEntityClassLoaderParent.to_json())

# convert the object into a dict
application_context_non_authenticated_entity_class_loader_parent_dict = application_context_non_authenticated_entity_class_loader_parent_instance.to_dict()
# create an instance of ApplicationContextNonAuthenticatedEntityClassLoaderParent from a dict
application_context_non_authenticated_entity_class_loader_parent_from_dict = ApplicationContextNonAuthenticatedEntityClassLoaderParent.from_dict(application_context_non_authenticated_entity_class_loader_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


