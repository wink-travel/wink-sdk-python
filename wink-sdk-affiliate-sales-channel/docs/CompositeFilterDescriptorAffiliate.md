# CompositeFilterDescriptorAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logic** | **str** | Whether to filter inclusively or exclusively | [optional] 
**filters** | [**List[FilterDescriptorAffiliate]**](FilterDescriptorAffiliate.md) | Descriptors used for filtering the result set | [optional] 

## Example

```python
from wink_sdk_affiliate_sales_channel.models.composite_filter_descriptor_affiliate import CompositeFilterDescriptorAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of CompositeFilterDescriptorAffiliate from a JSON string
composite_filter_descriptor_affiliate_instance = CompositeFilterDescriptorAffiliate.from_json(json)
# print the JSON string representation of the object
print(CompositeFilterDescriptorAffiliate.to_json())

# convert the object into a dict
composite_filter_descriptor_affiliate_dict = composite_filter_descriptor_affiliate_instance.to_dict()
# create an instance of CompositeFilterDescriptorAffiliate from a dict
composite_filter_descriptor_affiliate_from_dict = CompositeFilterDescriptorAffiliate.from_dict(composite_filter_descriptor_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


