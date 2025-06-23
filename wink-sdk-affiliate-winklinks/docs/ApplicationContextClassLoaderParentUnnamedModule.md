# ApplicationContextClassLoaderParentUnnamedModule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**descriptor** | [**ApplicationContextClassLoaderParentUnnamedModuleDescriptor**](ApplicationContextClassLoaderParentUnnamedModuleDescriptor.md) |  | [optional] 
**named** | **bool** |  | [optional] 
**annotations** | **List[object]** |  | [optional] 
**declared_annotations** | **List[object]** |  | [optional] 
**packages** | **List[str]** |  | [optional] 
**native_access_enabled** | **bool** |  | [optional] 
**layer** | **object** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.application_context_class_loader_parent_unnamed_module import ApplicationContextClassLoaderParentUnnamedModule

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationContextClassLoaderParentUnnamedModule from a JSON string
application_context_class_loader_parent_unnamed_module_instance = ApplicationContextClassLoaderParentUnnamedModule.from_json(json)
# print the JSON string representation of the object
print(ApplicationContextClassLoaderParentUnnamedModule.to_json())

# convert the object into a dict
application_context_class_loader_parent_unnamed_module_dict = application_context_class_loader_parent_unnamed_module_instance.to_dict()
# create an instance of ApplicationContextClassLoaderParentUnnamedModule from a dict
application_context_class_loader_parent_unnamed_module_from_dict = ApplicationContextClassLoaderParentUnnamedModule.from_dict(application_context_class_loader_parent_unnamed_module_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


