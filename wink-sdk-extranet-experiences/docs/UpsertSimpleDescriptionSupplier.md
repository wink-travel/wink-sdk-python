# UpsertSimpleDescriptionSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Use as title or short text description | 
**description** | **str** | Longer text description | 
**language** | **str** | Indicate which language this description is written in. | [default to 'en']

## Example

```python
from wink_sdk_extranet_experiences.models.upsert_simple_description_supplier import UpsertSimpleDescriptionSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertSimpleDescriptionSupplier from a JSON string
upsert_simple_description_supplier_instance = UpsertSimpleDescriptionSupplier.from_json(json)
# print the JSON string representation of the object
print(UpsertSimpleDescriptionSupplier.to_json())

# convert the object into a dict
upsert_simple_description_supplier_dict = upsert_simple_description_supplier_instance.to_dict()
# create an instance of UpsertSimpleDescriptionSupplier from a dict
upsert_simple_description_supplier_from_dict = UpsertSimpleDescriptionSupplier.from_dict(upsert_simple_description_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


