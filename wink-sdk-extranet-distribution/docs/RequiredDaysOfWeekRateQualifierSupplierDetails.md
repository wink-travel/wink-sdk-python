# RequiredDaysOfWeekRateQualifierSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_of_week** | [**DowPatternGroupSupplierDetails**](DowPatternGroupSupplierDetails.md) | The days of the week the user has to stay on to get this rate | 

## Example

```python
from wink_sdk_extranet_distribution.models.required_days_of_week_rate_qualifier_supplier_details import RequiredDaysOfWeekRateQualifierSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RequiredDaysOfWeekRateQualifierSupplierDetails from a JSON string
required_days_of_week_rate_qualifier_supplier_details_instance = RequiredDaysOfWeekRateQualifierSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(RequiredDaysOfWeekRateQualifierSupplierDetails.to_json())

# convert the object into a dict
required_days_of_week_rate_qualifier_supplier_details_dict = required_days_of_week_rate_qualifier_supplier_details_instance.to_dict()
# create an instance of RequiredDaysOfWeekRateQualifierSupplierDetails from a dict
required_days_of_week_rate_qualifier_supplier_details_from_dict = RequiredDaysOfWeekRateQualifierSupplierDetails.from_dict(required_days_of_week_rate_qualifier_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


