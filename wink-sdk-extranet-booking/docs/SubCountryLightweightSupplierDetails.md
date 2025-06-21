# SubCountryLightweightSupplierDetails

Country subdivision such as a state or province

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Sub-country name | [optional] 
**ascii_name** | **str** | Sub-country ascii name | [optional] 
**geo_name_id** | **str** | Sub-country GeoNames identifier | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.sub_country_lightweight_supplier_details import SubCountryLightweightSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SubCountryLightweightSupplierDetails from a JSON string
sub_country_lightweight_supplier_details_instance = SubCountryLightweightSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(SubCountryLightweightSupplierDetails.to_json())

# convert the object into a dict
sub_country_lightweight_supplier_details_dict = sub_country_lightweight_supplier_details_instance.to_dict()
# create an instance of SubCountryLightweightSupplierDetails from a dict
sub_country_lightweight_supplier_details_from_dict = SubCountryLightweightSupplierDetails.from_dict(sub_country_lightweight_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


