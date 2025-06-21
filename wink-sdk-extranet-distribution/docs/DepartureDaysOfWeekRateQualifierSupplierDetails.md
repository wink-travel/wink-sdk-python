# DepartureDaysOfWeekRateQualifierSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_of_week** | [**DowPatternGroupSupplierDetails**](DowPatternGroupSupplierDetails.md) | The days of the week when this rate is available | 

## Example

```python
from wink_sdk_extranet_distribution.models.departure_days_of_week_rate_qualifier_supplier_details import DepartureDaysOfWeekRateQualifierSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DepartureDaysOfWeekRateQualifierSupplierDetails from a JSON string
departure_days_of_week_rate_qualifier_supplier_details_instance = DepartureDaysOfWeekRateQualifierSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(DepartureDaysOfWeekRateQualifierSupplierDetails.to_json())

# convert the object into a dict
departure_days_of_week_rate_qualifier_supplier_details_dict = departure_days_of_week_rate_qualifier_supplier_details_instance.to_dict()
# create an instance of DepartureDaysOfWeekRateQualifierSupplierDetails from a dict
departure_days_of_week_rate_qualifier_supplier_details_from_dict = DepartureDaysOfWeekRateQualifierSupplierDetails.from_dict(departure_days_of_week_rate_qualifier_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


