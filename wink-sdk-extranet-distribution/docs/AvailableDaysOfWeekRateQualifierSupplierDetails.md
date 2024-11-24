# AvailableDaysOfWeekRateQualifierSupplierDetails

Restrict promotion to specific days of the week the promotion is available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_of_week** | [**DowPatternGroupSupplierDetails**](DowPatternGroupSupplierDetails.md) |  | 

## Example

```python
from wink_sdk_extranet_distribution.models.available_days_of_week_rate_qualifier_supplier_details import AvailableDaysOfWeekRateQualifierSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableDaysOfWeekRateQualifierSupplierDetails from a JSON string
available_days_of_week_rate_qualifier_supplier_details_instance = AvailableDaysOfWeekRateQualifierSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(AvailableDaysOfWeekRateQualifierSupplierDetails.to_json())

# convert the object into a dict
available_days_of_week_rate_qualifier_supplier_details_dict = available_days_of_week_rate_qualifier_supplier_details_instance.to_dict()
# create an instance of AvailableDaysOfWeekRateQualifierSupplierDetails from a dict
available_days_of_week_rate_qualifier_supplier_details_from_dict = AvailableDaysOfWeekRateQualifierSupplierDetails.from_dict(available_days_of_week_rate_qualifier_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


