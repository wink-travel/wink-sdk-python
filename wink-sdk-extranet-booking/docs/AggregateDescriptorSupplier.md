# AggregateDescriptorSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field to run aggregate function on | [optional] 
**aggregate** | **str** | Aggregate function | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.aggregate_descriptor_supplier import AggregateDescriptorSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateDescriptorSupplier from a JSON string
aggregate_descriptor_supplier_instance = AggregateDescriptorSupplier.from_json(json)
# print the JSON string representation of the object
print(AggregateDescriptorSupplier.to_json())

# convert the object into a dict
aggregate_descriptor_supplier_dict = aggregate_descriptor_supplier_instance.to_dict()
# create an instance of AggregateDescriptorSupplier from a dict
aggregate_descriptor_supplier_from_dict = AggregateDescriptorSupplier.from_dict(aggregate_descriptor_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


