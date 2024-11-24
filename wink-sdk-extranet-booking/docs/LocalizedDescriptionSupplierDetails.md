# LocalizedDescriptionSupplierDetails

List of localized descriptions for this fee.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Longer text description | 
**language** | **str** | Indicate which language this description is written in. | [default to 'en']

## Example

```python
from wink_sdk_extranet_booking.models.localized_description_supplier_details import LocalizedDescriptionSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of LocalizedDescriptionSupplierDetails from a JSON string
localized_description_supplier_details_instance = LocalizedDescriptionSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(LocalizedDescriptionSupplierDetails.to_json())

# convert the object into a dict
localized_description_supplier_details_dict = localized_description_supplier_details_instance.to_dict()
# create an instance of LocalizedDescriptionSupplierDetails from a dict
localized_description_supplier_details_from_dict = LocalizedDescriptionSupplierDetails.from_dict(localized_description_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


