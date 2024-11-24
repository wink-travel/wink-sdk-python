# BedroomSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of bedroom | 
**bed_list** | [**List[BedSupplier]**](BedSupplier.md) | A bedroom can have more than one bed type. | 

## Example

```python
from wink_sdk_extranet_facilities.models.bedroom_supplier import BedroomSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of BedroomSupplier from a JSON string
bedroom_supplier_instance = BedroomSupplier.from_json(json)
# print the JSON string representation of the object
print(BedroomSupplier.to_json())

# convert the object into a dict
bedroom_supplier_dict = bedroom_supplier_instance.to_dict()
# create an instance of BedroomSupplier from a dict
bedroom_supplier_from_dict = BedroomSupplier.from_dict(bedroom_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


