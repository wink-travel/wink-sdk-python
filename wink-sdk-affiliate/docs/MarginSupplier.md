# MarginSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top** | **float** |  | [optional] 
**right** | **float** |  | [optional] 
**bottom** | **float** |  | [optional] 
**left** | **float** |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.margin_supplier import MarginSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of MarginSupplier from a JSON string
margin_supplier_instance = MarginSupplier.from_json(json)
# print the JSON string representation of the object
print(MarginSupplier.to_json())

# convert the object into a dict
margin_supplier_dict = margin_supplier_instance.to_dict()
# create an instance of MarginSupplier from a dict
margin_supplier_from_dict = MarginSupplier.from_dict(margin_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


