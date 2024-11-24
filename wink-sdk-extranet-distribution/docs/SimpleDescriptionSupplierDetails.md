# SimpleDescriptionSupplierDetails

Localized media captions to give user some context about where this media was taken.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Use as title or short text description | [optional] 
**description** | **str** | Longer text description | 
**language** | **str** | Indicate which language this description is written in. | [default to 'en']

## Example

```python
from wink_sdk_extranet_distribution.models.simple_description_supplier_details import SimpleDescriptionSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleDescriptionSupplierDetails from a JSON string
simple_description_supplier_details_instance = SimpleDescriptionSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(SimpleDescriptionSupplierDetails.to_json())

# convert the object into a dict
simple_description_supplier_details_dict = simple_description_supplier_details_instance.to_dict()
# create an instance of SimpleDescriptionSupplierDetails from a dict
simple_description_supplier_details_from_dict = SimpleDescriptionSupplierDetails.from_dict(simple_description_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


