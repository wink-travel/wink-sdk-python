# IdentifierNamePairSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Identifier of associated entity | 
**name** | **str** | Entity name | 

## Example

```python
from wink_sdk_extranet_monetize.models.identifier_name_pair_supplier import IdentifierNamePairSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of IdentifierNamePairSupplier from a JSON string
identifier_name_pair_supplier_instance = IdentifierNamePairSupplier.from_json(json)
# print the JSON string representation of the object
print(IdentifierNamePairSupplier.to_json())

# convert the object into a dict
identifier_name_pair_supplier_dict = identifier_name_pair_supplier_instance.to_dict()
# create an instance of IdentifierNamePairSupplier from a dict
identifier_name_pair_supplier_from_dict = IdentifierNamePairSupplier.from_dict(identifier_name_pair_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


