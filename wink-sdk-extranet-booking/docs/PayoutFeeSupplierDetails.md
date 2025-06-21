# PayoutFeeSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique system ID. | 
**fee** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Fee amount | 
**type** | **str** | Type of fee | 
**candidate** | **str** | Who pays for this fee | 
**description** | **str** | Withdrawal fee description | 

## Example

```python
from wink_sdk_extranet_booking.models.payout_fee_supplier_details import PayoutFeeSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PayoutFeeSupplierDetails from a JSON string
payout_fee_supplier_details_instance = PayoutFeeSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(PayoutFeeSupplierDetails.to_json())

# convert the object into a dict
payout_fee_supplier_details_dict = payout_fee_supplier_details_instance.to_dict()
# create an instance of PayoutFeeSupplierDetails from a dict
payout_fee_supplier_details_from_dict = PayoutFeeSupplierDetails.from_dict(payout_fee_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


