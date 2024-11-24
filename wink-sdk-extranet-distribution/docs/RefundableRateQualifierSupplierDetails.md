# RefundableRateQualifierSupplierDetails

Restrict promotion to either refundable / non-refundable rates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refundable** | **bool** | Whether restriction is on refundable rates | 

## Example

```python
from wink_sdk_extranet_distribution.models.refundable_rate_qualifier_supplier_details import RefundableRateQualifierSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RefundableRateQualifierSupplierDetails from a JSON string
refundable_rate_qualifier_supplier_details_instance = RefundableRateQualifierSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(RefundableRateQualifierSupplierDetails.to_json())

# convert the object into a dict
refundable_rate_qualifier_supplier_details_dict = refundable_rate_qualifier_supplier_details_instance.to_dict()
# create an instance of RefundableRateQualifierSupplierDetails from a dict
refundable_rate_qualifier_supplier_details_from_dict = RefundableRateQualifierSupplierDetails.from_dict(refundable_rate_qualifier_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


