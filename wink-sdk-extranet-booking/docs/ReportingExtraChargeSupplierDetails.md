# ReportingExtraChargeSupplierDetails

Displays extra charge accounting details.

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
from wink_sdk_extranet_booking.models.reporting_extra_charge_supplier_details import ReportingExtraChargeSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ReportingExtraChargeSupplierDetails from a JSON string
reporting_extra_charge_supplier_details_instance = ReportingExtraChargeSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(ReportingExtraChargeSupplierDetails.to_json())

# convert the object into a dict
reporting_extra_charge_supplier_details_dict = reporting_extra_charge_supplier_details_instance.to_dict()
# create an instance of ReportingExtraChargeSupplierDetails from a dict
reporting_extra_charge_supplier_details_from_dict = ReportingExtraChargeSupplierDetails.from_dict(reporting_extra_charge_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


