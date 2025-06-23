# ApplicationContextClassLoaderParent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**registered_as_parallel_capable** | **bool** |  | [optional] 
**unnamed_module** | [**ApplicationContextClassLoaderParentUnnamedModule**](ApplicationContextClassLoaderParentUnnamedModule.md) |  | [optional] 
**defined_packages** | [**List[ApplicationContextClassLoaderParentDefinedPackagesInner]**](ApplicationContextClassLoaderParentDefinedPackagesInner.md) |  | [optional] 
**default_assertion_status** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.application_context_class_loader_parent import ApplicationContextClassLoaderParent

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationContextClassLoaderParent from a JSON string
application_context_class_loader_parent_instance = ApplicationContextClassLoaderParent.from_json(json)
# print the JSON string representation of the object
print(ApplicationContextClassLoaderParent.to_json())

# convert the object into a dict
application_context_class_loader_parent_dict = application_context_class_loader_parent_instance.to_dict()
# create an instance of ApplicationContextClassLoaderParent from a dict
application_context_class_loader_parent_from_dict = ApplicationContextClassLoaderParent.from_dict(application_context_class_loader_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


