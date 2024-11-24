# ArrivalDaysOfWeekRateQualifierSupplierDetails

Restrict promotion to specific days of the week the guest is arriving.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_of_week** | [**DowPatternGroupSupplierDetails**](DowPatternGroupSupplierDetails.md) |  | 

## Example

```python
from wink_sdk_extranet_distribution.models.arrival_days_of_week_rate_qualifier_supplier_details import ArrivalDaysOfWeekRateQualifierSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ArrivalDaysOfWeekRateQualifierSupplierDetails from a JSON string
arrival_days_of_week_rate_qualifier_supplier_details_instance = ArrivalDaysOfWeekRateQualifierSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(ArrivalDaysOfWeekRateQualifierSupplierDetails.to_json())

# convert the object into a dict
arrival_days_of_week_rate_qualifier_supplier_details_dict = arrival_days_of_week_rate_qualifier_supplier_details_instance.to_dict()
# create an instance of ArrivalDaysOfWeekRateQualifierSupplierDetails from a dict
arrival_days_of_week_rate_qualifier_supplier_details_from_dict = ArrivalDaysOfWeekRateQualifierSupplierDetails.from_dict(arrival_days_of_week_rate_qualifier_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


