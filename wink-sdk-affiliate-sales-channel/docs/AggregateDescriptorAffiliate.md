# AggregateDescriptorAffiliate

Primitive aggregate data points

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field to run aggregate function on | [optional] 
**aggregate** | **str** | Aggregate function | [optional] 

## Example

```python
from wink_sdk_affiliate_sales_channel.models.aggregate_descriptor_affiliate import AggregateDescriptorAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateDescriptorAffiliate from a JSON string
aggregate_descriptor_affiliate_instance = AggregateDescriptorAffiliate.from_json(json)
# print the JSON string representation of the object
print(AggregateDescriptorAffiliate.to_json())

# convert the object into a dict
aggregate_descriptor_affiliate_dict = aggregate_descriptor_affiliate_instance.to_dict()
# create an instance of AggregateDescriptorAffiliate from a dict
aggregate_descriptor_affiliate_from_dict = AggregateDescriptorAffiliate.from_dict(aggregate_descriptor_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


