# FilterDescriptorAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field name to filter on | 
**operator** | **str** | Filter operator to use on field | 
**value** | **object** |  | 
**ignore_case** | **bool** | Make filter comparison case insensitive. Default: Case sensitive  | [optional] 

## Example

```python
from wink_sdk_affiliate_sales_channel.models.filter_descriptor_affiliate import FilterDescriptorAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of FilterDescriptorAffiliate from a JSON string
filter_descriptor_affiliate_instance = FilterDescriptorAffiliate.from_json(json)
# print the JSON string representation of the object
print(FilterDescriptorAffiliate.to_json())

# convert the object into a dict
filter_descriptor_affiliate_dict = filter_descriptor_affiliate_instance.to_dict()
# create an instance of FilterDescriptorAffiliate from a dict
filter_descriptor_affiliate_from_dict = FilterDescriptorAffiliate.from_dict(filter_descriptor_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


