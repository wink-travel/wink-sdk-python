# TimezoneRateQualifierSupplier

Restrict promotion to specific time zones. See [Geo-IP timezone geoname data](#operation/showTimezones)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timezone** | **str** | Bookers timezone | 

## Example

```python
from wink_sdk_extranet_monetize.models.timezone_rate_qualifier_supplier import TimezoneRateQualifierSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of TimezoneRateQualifierSupplier from a JSON string
timezone_rate_qualifier_supplier_instance = TimezoneRateQualifierSupplier.from_json(json)
# print the JSON string representation of the object
print(TimezoneRateQualifierSupplier.to_json())

# convert the object into a dict
timezone_rate_qualifier_supplier_dict = timezone_rate_qualifier_supplier_instance.to_dict()
# create an instance of TimezoneRateQualifierSupplier from a dict
timezone_rate_qualifier_supplier_from_dict = TimezoneRateQualifierSupplier.from_dict(timezone_rate_qualifier_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


