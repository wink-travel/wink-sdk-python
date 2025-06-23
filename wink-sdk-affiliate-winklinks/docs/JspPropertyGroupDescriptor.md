# JspPropertyGroupDescriptor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deferred_syntax_allowed_as_literal** | **str** |  | [optional] 
**error_on_el_not_found** | **str** |  | [optional] 
**page_encoding** | **str** |  | [optional] 
**scripting_invalid** | **str** |  | [optional] 
**is_xml** | **str** |  | [optional] 
**include_preludes** | **List[str]** |  | [optional] 
**include_codas** | **List[str]** |  | [optional] 
**trim_directive_whitespaces** | **str** |  | [optional] 
**error_on_undeclared_namespace** | **str** |  | [optional] 
**el_ignored** | **str** |  | [optional] 
**buffer** | **str** |  | [optional] 
**default_content_type** | **str** |  | [optional] 
**url_patterns** | **List[str]** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.jsp_property_group_descriptor import JspPropertyGroupDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of JspPropertyGroupDescriptor from a JSON string
jsp_property_group_descriptor_instance = JspPropertyGroupDescriptor.from_json(json)
# print the JSON string representation of the object
print(JspPropertyGroupDescriptor.to_json())

# convert the object into a dict
jsp_property_group_descriptor_dict = jsp_property_group_descriptor_instance.to_dict()
# create an instance of JspPropertyGroupDescriptor from a dict
jsp_property_group_descriptor_from_dict = JspPropertyGroupDescriptor.from_dict(jsp_property_group_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


