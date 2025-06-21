# SimpleDescriptionSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Use as title or short text description | 
**description** | **str** | Longer text description | 
**language** | **str** | Indicate which language this description is written in. | [default to 'en']
**creator** | **str** | Whether it was user or system generated. | [optional] [default to 'USER']
**md5_content_hash** | **str** | The md5 hash of the name, description and language. | [optional] 
**hash_mismatch** | **bool** |  | [optional] [readonly] 

## Example

```python
from wink_sdk_extranet_monetize.models.simple_description_supplier import SimpleDescriptionSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleDescriptionSupplier from a JSON string
simple_description_supplier_instance = SimpleDescriptionSupplier.from_json(json)
# print the JSON string representation of the object
print(SimpleDescriptionSupplier.to_json())

# convert the object into a dict
simple_description_supplier_dict = simple_description_supplier_instance.to_dict()
# create an instance of SimpleDescriptionSupplier from a dict
simple_description_supplier_from_dict = SimpleDescriptionSupplier.from_dict(simple_description_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


