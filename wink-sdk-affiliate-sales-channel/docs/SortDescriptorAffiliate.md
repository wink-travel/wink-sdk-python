# SortDescriptorAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dir** | **str** | Descriptors used for sorting result set | [optional] 
**var_field** | **str** | Data set field to sort on | [optional] 

## Example

```python
from wink_sdk_affiliate_sales_channel.models.sort_descriptor_affiliate import SortDescriptorAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SortDescriptorAffiliate from a JSON string
sort_descriptor_affiliate_instance = SortDescriptorAffiliate.from_json(json)
# print the JSON string representation of the object
print(SortDescriptorAffiliate.to_json())

# convert the object into a dict
sort_descriptor_affiliate_dict = sort_descriptor_affiliate_instance.to_dict()
# create an instance of SortDescriptorAffiliate from a dict
sort_descriptor_affiliate_from_dict = SortDescriptorAffiliate.from_dict(sort_descriptor_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


