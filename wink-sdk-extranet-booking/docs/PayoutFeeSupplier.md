# PayoutFeeSupplier

Fees incurred when making the withdrawal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique system ID. | 
**fee** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | 
**type** | **str** | Type of fee | 
**candidate** | **str** | Who pays for this fee | 
**description** | **str** | Withdrawal fee description | 

## Example

```python
from wink_sdk_extranet_booking.models.payout_fee_supplier import PayoutFeeSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutFeeSupplier from a JSON string
payout_fee_supplier_instance = PayoutFeeSupplier.from_json(json)
# print the JSON string representation of the object
print(PayoutFeeSupplier.to_json())

# convert the object into a dict
payout_fee_supplier_dict = payout_fee_supplier_instance.to_dict()
# create an instance of PayoutFeeSupplier from a dict
payout_fee_supplier_from_dict = PayoutFeeSupplier.from_dict(payout_fee_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


