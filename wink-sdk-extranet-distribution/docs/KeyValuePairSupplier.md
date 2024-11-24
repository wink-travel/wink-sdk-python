# KeyValuePairSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value that should be persisted. | 
**label** | **str** | English readable text of the value. | 

## Example

```python
from wink_sdk_extranet_distribution.models.key_value_pair_supplier import KeyValuePairSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of KeyValuePairSupplier from a JSON string
key_value_pair_supplier_instance = KeyValuePairSupplier.from_json(json)
# print the JSON string representation of the object
print(KeyValuePairSupplier.to_json())

# convert the object into a dict
key_value_pair_supplier_dict = key_value_pair_supplier_instance.to_dict()
# create an instance of KeyValuePairSupplier from a dict
key_value_pair_supplier_from_dict = KeyValuePairSupplier.from_dict(key_value_pair_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


