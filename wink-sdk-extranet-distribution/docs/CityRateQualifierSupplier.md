# CityRateQualifierSupplier

Restrict promotion to specific cities. See [Geo-IP city geoname data](#operation/searchForCity)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | [**GeoIPSupplier**](GeoIPSupplier.md) |  | 

## Example

```python
from wink_sdk_extranet_distribution.models.city_rate_qualifier_supplier import CityRateQualifierSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of CityRateQualifierSupplier from a JSON string
city_rate_qualifier_supplier_instance = CityRateQualifierSupplier.from_json(json)
# print the JSON string representation of the object
print(CityRateQualifierSupplier.to_json())

# convert the object into a dict
city_rate_qualifier_supplier_dict = city_rate_qualifier_supplier_instance.to_dict()
# create an instance of CityRateQualifierSupplier from a dict
city_rate_qualifier_supplier_from_dict = CityRateQualifierSupplier.from_dict(city_rate_qualifier_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


