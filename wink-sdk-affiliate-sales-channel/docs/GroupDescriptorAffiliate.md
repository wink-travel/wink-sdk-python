# GroupDescriptorAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field to group data set on | [optional] 
**dir** | **str** | Group sort direction | [optional] 
**aggregates** | [**List[AggregateDescriptorAffiliate]**](AggregateDescriptorAffiliate.md) | Primitive aggregate data points | [optional] 

## Example

```python
from wink_sdk_affiliate_sales_channel.models.group_descriptor_affiliate import GroupDescriptorAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of GroupDescriptorAffiliate from a JSON string
group_descriptor_affiliate_instance = GroupDescriptorAffiliate.from_json(json)
# print the JSON string representation of the object
print(GroupDescriptorAffiliate.to_json())

# convert the object into a dict
group_descriptor_affiliate_dict = group_descriptor_affiliate_instance.to_dict()
# create an instance of GroupDescriptorAffiliate from a dict
group_descriptor_affiliate_from_dict = GroupDescriptorAffiliate.from_dict(group_descriptor_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


