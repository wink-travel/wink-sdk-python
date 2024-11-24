# ReportingDailyRateSupplierDetails

Displays rate accounting details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The rate date. | [optional] 
**base_amount** | **float** | The rate given to us by channel manager / CRS / PMS. | [optional] 
**gross_amount** | **float** | The derived amount based on promotions, member discounts etc within our platform. | [optional] 
**net_amount** | **float** | The gross amount minus fees and commissions. | [optional] 
**net_amount_with_refund** | **float** | The net amount minus potential refund. Null if booking contains no refund. | [optional] 
**currency** | **str** | The currency for these amounts. | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.reporting_daily_rate_supplier_details import ReportingDailyRateSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ReportingDailyRateSupplierDetails from a JSON string
reporting_daily_rate_supplier_details_instance = ReportingDailyRateSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(ReportingDailyRateSupplierDetails.to_json())

# convert the object into a dict
reporting_daily_rate_supplier_details_dict = reporting_daily_rate_supplier_details_instance.to_dict()
# create an instance of ReportingDailyRateSupplierDetails from a dict
reporting_daily_rate_supplier_details_from_dict = ReportingDailyRateSupplierDetails.from_dict(reporting_daily_rate_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


