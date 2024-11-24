# PaddingSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top** | **float** |  | [optional] 
**right** | **float** |  | [optional] 
**bottom** | **float** |  | [optional] 
**left** | **float** |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.padding_supplier import PaddingSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of PaddingSupplier from a JSON string
padding_supplier_instance = PaddingSupplier.from_json(json)
# print the JSON string representation of the object
print(PaddingSupplier.to_json())

# convert the object into a dict
padding_supplier_dict = padding_supplier_instance.to_dict()
# create an instance of PaddingSupplier from a dict
padding_supplier_from_dict = PaddingSupplier.from_dict(padding_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


