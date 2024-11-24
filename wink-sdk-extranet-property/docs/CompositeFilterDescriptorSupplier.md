# CompositeFilterDescriptorSupplier

Descriptors used for filtering result set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logic** | **str** | Whether to filter inclusively or exclusively | [optional] 
**filters** | [**List[FilterDescriptorSupplier]**](FilterDescriptorSupplier.md) | Descriptors used for filtering the result set | [optional] 

## Example

```python
from wink_sdk_extranet_property.models.composite_filter_descriptor_supplier import CompositeFilterDescriptorSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of CompositeFilterDescriptorSupplier from a JSON string
composite_filter_descriptor_supplier_instance = CompositeFilterDescriptorSupplier.from_json(json)
# print the JSON string representation of the object
print(CompositeFilterDescriptorSupplier.to_json())

# convert the object into a dict
composite_filter_descriptor_supplier_dict = composite_filter_descriptor_supplier_instance.to_dict()
# create an instance of CompositeFilterDescriptorSupplier from a dict
composite_filter_descriptor_supplier_from_dict = CompositeFilterDescriptorSupplier.from_dict(composite_filter_descriptor_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


