# CountryRateQualifierSupplier

Restrict promotion to specific countries. See [Geo-IP country geoname data](#operation/showCountries)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | [**GeoNameCountrySupplier**](GeoNameCountrySupplier.md) |  | 

## Example

```python
from wink_sdk_extranet_distribution.models.country_rate_qualifier_supplier import CountryRateQualifierSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of CountryRateQualifierSupplier from a JSON string
country_rate_qualifier_supplier_instance = CountryRateQualifierSupplier.from_json(json)
# print the JSON string representation of the object
print(CountryRateQualifierSupplier.to_json())

# convert the object into a dict
country_rate_qualifier_supplier_dict = country_rate_qualifier_supplier_instance.to_dict()
# create an instance of CountryRateQualifierSupplier from a dict
country_rate_qualifier_supplier_from_dict = CountryRateQualifierSupplier.from_dict(country_rate_qualifier_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


