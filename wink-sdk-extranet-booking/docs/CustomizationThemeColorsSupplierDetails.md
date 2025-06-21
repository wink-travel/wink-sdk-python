# CustomizationThemeColorsSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | **str** | Primary color | [optional] [default to '#dc3545']
**secondary** | **str** | Secondary color | [optional] [default to '#6c757d']
**success** | **str** | Success color | [optional] [default to '#28a745']
**danger** | **str** | Danger color | [optional] [default to '#dc3545']
**warning** | **str** | Warning color | [optional] [default to '#ffc107']
**info** | **str** | Info color | [optional] [default to '#17a2b8']
**light** | **str** | Light color | [optional] [default to '#f8f9fa']
**dark** | **str** | Dark color | [optional] [default to '#343a40']
**body** | **str** | Body color | [optional] [default to '#212529']
**muted** | **str** | Muted color | [optional] [default to '#6c757d']
**white** | **str** | White color | [optional] [default to '#ffffff']

## Example

```python
from wink_sdk_extranet_booking.models.customization_theme_colors_supplier_details import CustomizationThemeColorsSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationThemeColorsSupplierDetails from a JSON string
customization_theme_colors_supplier_details_instance = CustomizationThemeColorsSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(CustomizationThemeColorsSupplierDetails.to_json())

# convert the object into a dict
customization_theme_colors_supplier_details_dict = customization_theme_colors_supplier_details_instance.to_dict()
# create an instance of CustomizationThemeColorsSupplierDetails from a dict
customization_theme_colors_supplier_details_from_dict = CustomizationThemeColorsSupplierDetails.from_dict(customization_theme_colors_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


