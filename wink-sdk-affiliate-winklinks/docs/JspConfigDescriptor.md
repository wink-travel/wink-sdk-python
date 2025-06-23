# JspConfigDescriptor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taglibs** | [**List[TaglibDescriptor]**](TaglibDescriptor.md) |  | [optional] 
**jsp_property_groups** | [**List[JspPropertyGroupDescriptor]**](JspPropertyGroupDescriptor.md) |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.jsp_config_descriptor import JspConfigDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of JspConfigDescriptor from a JSON string
jsp_config_descriptor_instance = JspConfigDescriptor.from_json(json)
# print the JSON string representation of the object
print(JspConfigDescriptor.to_json())

# convert the object into a dict
jsp_config_descriptor_dict = jsp_config_descriptor_instance.to_dict()
# create an instance of JspConfigDescriptor from a dict
jsp_config_descriptor_from_dict = JspConfigDescriptor.from_dict(jsp_config_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


