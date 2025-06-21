# CountryRateQualifierSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | [**GeoNameCountrySupplierDetails**](GeoNameCountrySupplierDetails.md) | country to restrict on | 

## Example

```python
from wink_sdk_extranet_distribution.models.country_rate_qualifier_supplier_details import CountryRateQualifierSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CountryRateQualifierSupplierDetails from a JSON string
country_rate_qualifier_supplier_details_instance = CountryRateQualifierSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(CountryRateQualifierSupplierDetails.to_json())

# convert the object into a dict
country_rate_qualifier_supplier_details_dict = country_rate_qualifier_supplier_details_instance.to_dict()
# create an instance of CountryRateQualifierSupplierDetails from a dict
country_rate_qualifier_supplier_details_from_dict = CountryRateQualifierSupplierDetails.from_dict(country_rate_qualifier_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


