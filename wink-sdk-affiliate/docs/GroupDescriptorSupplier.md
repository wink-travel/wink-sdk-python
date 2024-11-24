# GroupDescriptorSupplier

Descriptors to group result sets by.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field to group data set on | [optional] 
**dir** | **str** | Group sort direction | [optional] 
**aggregates** | [**List[AggregateDescriptorSupplier]**](AggregateDescriptorSupplier.md) | Primitive aggregate data points | [optional] 

## Example

```python
from wink_sdk_affiliate.models.group_descriptor_supplier import GroupDescriptorSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of GroupDescriptorSupplier from a JSON string
group_descriptor_supplier_instance = GroupDescriptorSupplier.from_json(json)
# print the JSON string representation of the object
print(GroupDescriptorSupplier.to_json())

# convert the object into a dict
group_descriptor_supplier_dict = group_descriptor_supplier_instance.to_dict()
# create an instance of GroupDescriptorSupplier from a dict
group_descriptor_supplier_from_dict = GroupDescriptorSupplier.from_dict(group_descriptor_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


