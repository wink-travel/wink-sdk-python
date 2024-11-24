# FeeSupplierDetails

Fees associated with this booking contract.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique system ID. | 
**fee** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | 
**type** | **str** | Type of fee | 
**description** | **str** | Withdrawal fee description | 

## Example

```python
from wink_sdk_extranet_booking.models.fee_supplier_details import FeeSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FeeSupplierDetails from a JSON string
fee_supplier_details_instance = FeeSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(FeeSupplierDetails.to_json())

# convert the object into a dict
fee_supplier_details_dict = fee_supplier_details_instance.to_dict()
# create an instance of FeeSupplierDetails from a dict
fee_supplier_details_from_dict = FeeSupplierDetails.from_dict(fee_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


