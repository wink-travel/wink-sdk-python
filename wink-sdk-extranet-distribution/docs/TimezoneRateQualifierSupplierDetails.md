# TimezoneRateQualifierSupplierDetails

Restrict promotion to specific time zones. See [Geo-IP timezone geoname data](#operation/showTimezones)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timezone** | **str** | Bookers timezone | 

## Example

```python
from wink_sdk_extranet_distribution.models.timezone_rate_qualifier_supplier_details import TimezoneRateQualifierSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of TimezoneRateQualifierSupplierDetails from a JSON string
timezone_rate_qualifier_supplier_details_instance = TimezoneRateQualifierSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(TimezoneRateQualifierSupplierDetails.to_json())

# convert the object into a dict
timezone_rate_qualifier_supplier_details_dict = timezone_rate_qualifier_supplier_details_instance.to_dict()
# create an instance of TimezoneRateQualifierSupplierDetails from a dict
timezone_rate_qualifier_supplier_details_from_dict = TimezoneRateQualifierSupplierDetails.from_dict(timezone_rate_qualifier_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


