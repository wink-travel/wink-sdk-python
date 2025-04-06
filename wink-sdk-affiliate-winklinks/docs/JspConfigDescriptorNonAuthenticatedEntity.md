# JspConfigDescriptorNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taglibs** | [**List[TaglibDescriptorNonAuthenticatedEntity]**](TaglibDescriptorNonAuthenticatedEntity.md) |  | [optional] 
**jsp_property_groups** | [**List[JspPropertyGroupDescriptorNonAuthenticatedEntity]**](JspPropertyGroupDescriptorNonAuthenticatedEntity.md) |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.jsp_config_descriptor_non_authenticated_entity import JspConfigDescriptorNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of JspConfigDescriptorNonAuthenticatedEntity from a JSON string
jsp_config_descriptor_non_authenticated_entity_instance = JspConfigDescriptorNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(JspConfigDescriptorNonAuthenticatedEntity.to_json())

# convert the object into a dict
jsp_config_descriptor_non_authenticated_entity_dict = jsp_config_descriptor_non_authenticated_entity_instance.to_dict()
# create an instance of JspConfigDescriptorNonAuthenticatedEntity from a dict
jsp_config_descriptor_non_authenticated_entity_from_dict = JspConfigDescriptorNonAuthenticatedEntity.from_dict(jsp_config_descriptor_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


