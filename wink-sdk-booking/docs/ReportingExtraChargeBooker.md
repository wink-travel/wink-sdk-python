# ReportingExtraChargeBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**gross_amount** | **float** |  | [optional] 
**net_amount** | **float** |  | [optional] 
**net_amount_with_refund** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 

## Example

```python
from wink_sdk_booking.models.reporting_extra_charge_booker import ReportingExtraChargeBooker

# TODO update the JSON string below
json = "{}"
# create an instance of ReportingExtraChargeBooker from a JSON string
reporting_extra_charge_booker_instance = ReportingExtraChargeBooker.from_json(json)
# print the JSON string representation of the object
print(ReportingExtraChargeBooker.to_json())

# convert the object into a dict
reporting_extra_charge_booker_dict = reporting_extra_charge_booker_instance.to_dict()
# create an instance of ReportingExtraChargeBooker from a dict
reporting_extra_charge_booker_from_dict = ReportingExtraChargeBooker.from_dict(reporting_extra_charge_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


