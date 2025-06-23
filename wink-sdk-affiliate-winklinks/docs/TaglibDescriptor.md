# TaglibDescriptor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taglib_location** | **str** |  | [optional] 
**taglib_uri** | **str** |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.taglib_descriptor import TaglibDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of TaglibDescriptor from a JSON string
taglib_descriptor_instance = TaglibDescriptor.from_json(json)
# print the JSON string representation of the object
print(TaglibDescriptor.to_json())

# convert the object into a dict
taglib_descriptor_dict = taglib_descriptor_instance.to_dict()
# create an instance of TaglibDescriptor from a dict
taglib_descriptor_from_dict = TaglibDescriptor.from_dict(taglib_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


