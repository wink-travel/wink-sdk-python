# ReportingAncillarySupplier

Displays ancillary accounting details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Full name of ancillary in English. | [optional] 
**type** | **str** | The type | [optional] 
**gross_amount** | **float** | The gross amount. | [optional] 
**net_amount** | **float** | The gross amount minus fees and commissions. | [optional] 
**net_amount_with_refund** | **float** | The gross amount minus fees and commissions. | [optional] 
**currency** | **str** | The currency for these amounts. | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.reporting_ancillary_supplier import ReportingAncillarySupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ReportingAncillarySupplier from a JSON string
reporting_ancillary_supplier_instance = ReportingAncillarySupplier.from_json(json)
# print the JSON string representation of the object
print(ReportingAncillarySupplier.to_json())

# convert the object into a dict
reporting_ancillary_supplier_dict = reporting_ancillary_supplier_instance.to_dict()
# create an instance of ReportingAncillarySupplier from a dict
reporting_ancillary_supplier_from_dict = ReportingAncillarySupplier.from_dict(reporting_ancillary_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


