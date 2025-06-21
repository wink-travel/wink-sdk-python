# CityRateQualifierSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | [**GeoIpLightweightSupplierDetails**](GeoIpLightweightSupplierDetails.md) | City geoIP | 

## Example

```python
from wink_sdk_extranet_distribution.models.city_rate_qualifier_supplier_details import CityRateQualifierSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CityRateQualifierSupplierDetails from a JSON string
city_rate_qualifier_supplier_details_instance = CityRateQualifierSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(CityRateQualifierSupplierDetails.to_json())

# convert the object into a dict
city_rate_qualifier_supplier_details_dict = city_rate_qualifier_supplier_details_instance.to_dict()
# create an instance of CityRateQualifierSupplierDetails from a dict
city_rate_qualifier_supplier_details_from_dict = CityRateQualifierSupplierDetails.from_dict(city_rate_qualifier_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


