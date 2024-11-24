# SortDescriptorSupplier

Descriptors used for sorting result set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dir** | **str** | Descriptors used for sorting result set | [optional] 
**var_field** | **str** | Data set field to sort on | [optional] 

## Example

```python
from wink_sdk_affiliate.models.sort_descriptor_supplier import SortDescriptorSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of SortDescriptorSupplier from a JSON string
sort_descriptor_supplier_instance = SortDescriptorSupplier.from_json(json)
# print the JSON string representation of the object
print(SortDescriptorSupplier.to_json())

# convert the object into a dict
sort_descriptor_supplier_dict = sort_descriptor_supplier_instance.to_dict()
# create an instance of SortDescriptorSupplier from a dict
sort_descriptor_supplier_from_dict = SortDescriptorSupplier.from_dict(sort_descriptor_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


