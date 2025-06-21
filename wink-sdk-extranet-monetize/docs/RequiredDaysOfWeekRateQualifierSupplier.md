# RequiredDaysOfWeekRateQualifierSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_of_week** | [**DowPatternGroupSupplier**](DowPatternGroupSupplier.md) | The days of the week the user has to stay on to get this rate | 

## Example

```python
from wink_sdk_extranet_monetize.models.required_days_of_week_rate_qualifier_supplier import RequiredDaysOfWeekRateQualifierSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of RequiredDaysOfWeekRateQualifierSupplier from a JSON string
required_days_of_week_rate_qualifier_supplier_instance = RequiredDaysOfWeekRateQualifierSupplier.from_json(json)
# print the JSON string representation of the object
print(RequiredDaysOfWeekRateQualifierSupplier.to_json())

# convert the object into a dict
required_days_of_week_rate_qualifier_supplier_dict = required_days_of_week_rate_qualifier_supplier_instance.to_dict()
# create an instance of RequiredDaysOfWeekRateQualifierSupplier from a dict
required_days_of_week_rate_qualifier_supplier_from_dict = RequiredDaysOfWeekRateQualifierSupplier.from_dict(required_days_of_week_rate_qualifier_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


