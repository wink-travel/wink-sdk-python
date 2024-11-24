# PendingRefundSupplierDetails

When a refund is first requested, it ends up here. Once it is applied, it moves out of this list and into the parent modifier property

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_identifier** | **str** | This is the refund identifier located on the root bookingContract.refunds object | 
**source_amount_refund_modifier** | **float** | The delta from the original source amount after a refund occurred | 
**display_amount_refund_modifier** | **float** | The delta from the original display amount after a refund occurred | 
**supplier_amount_refund_modifier** | **float** | The delta from the original supplier amount after a refund occurred | 
**internal_amount_refund_modifier** | **float** | The delta from the original internal amount after a refund occurred | 
**capture_amount_refund_modifier** | **float** | The delta from the original capture amount after a refund occurred | 

## Example

```python
from wink_sdk_extranet_distribution.models.pending_refund_supplier_details import PendingRefundSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PendingRefundSupplierDetails from a JSON string
pending_refund_supplier_details_instance = PendingRefundSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(PendingRefundSupplierDetails.to_json())

# convert the object into a dict
pending_refund_supplier_details_dict = pending_refund_supplier_details_instance.to_dict()
# create an instance of PendingRefundSupplierDetails from a dict
pending_refund_supplier_details_from_dict = PendingRefundSupplierDetails.from_dict(pending_refund_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


