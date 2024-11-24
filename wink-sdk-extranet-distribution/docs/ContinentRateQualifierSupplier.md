# ContinentRateQualifierSupplier

Restrict promotion to specific continents. See [Geo-IP continent geoname data](#operation/showContinents)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continent** | **str** | Continent code | 

## Example

```python
from wink_sdk_extranet_distribution.models.continent_rate_qualifier_supplier import ContinentRateQualifierSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ContinentRateQualifierSupplier from a JSON string
continent_rate_qualifier_supplier_instance = ContinentRateQualifierSupplier.from_json(json)
# print the JSON string representation of the object
print(ContinentRateQualifierSupplier.to_json())

# convert the object into a dict
continent_rate_qualifier_supplier_dict = continent_rate_qualifier_supplier_instance.to_dict()
# create an instance of ContinentRateQualifierSupplier from a dict
continent_rate_qualifier_supplier_from_dict = ContinentRateQualifierSupplier.from_dict(continent_rate_qualifier_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


