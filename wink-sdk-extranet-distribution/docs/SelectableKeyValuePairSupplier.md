# SelectableKeyValuePairSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value that should be persisted. | 
**label** | **str** | English readable text of the value. | 
**selected** | **bool** | Whether record is selected or not. | 

## Example

```python
from wink_sdk_extranet_distribution.models.selectable_key_value_pair_supplier import SelectableKeyValuePairSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of SelectableKeyValuePairSupplier from a JSON string
selectable_key_value_pair_supplier_instance = SelectableKeyValuePairSupplier.from_json(json)
# print the JSON string representation of the object
print(SelectableKeyValuePairSupplier.to_json())

# convert the object into a dict
selectable_key_value_pair_supplier_dict = selectable_key_value_pair_supplier_instance.to_dict()
# create an instance of SelectableKeyValuePairSupplier from a dict
selectable_key_value_pair_supplier_from_dict = SelectableKeyValuePairSupplier.from_dict(selectable_key_value_pair_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


