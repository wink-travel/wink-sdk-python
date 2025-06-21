# BeneficiarySupplierDetails

Beneficiary is a registered account with rights to compensation within a booking.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_identifier** | **str** | accountIdentifier of beneficiary that can map to an account with us | 
**account_name** | **str** | accountName of beneficiary that can map to an account with us | 
**account_email** | **str** | accountEmail of beneficiary that can map to an account with us | 
**account_url** | **str** | accountUrl of beneficiary that can map to an account with us | [optional] 
**type** | **str** | The type of beneficiary payment. | 
**amount_due** | [**BeneficiaryChargeSupplierDetails**](BeneficiaryChargeSupplierDetails.md) | The original slice requested | [optional] 
**source_currency** | **str** | The source currency | 
**display_currency** | **str** | The display currency | 
**supplier_currency** | **str** | The supplier currency | 
**internal_currency** | **str** | The internal currency | 
**capture_currency** | **str** | The capture currency | 
**source_amount** | **float** | Amount in source currency | 
**display_amount** | **float** | Amount in display currency | 
**supplier_amount** | **float** | Amount in supplier currency | 
**internal_amount** | **float** | Amount in internal currency | 
**capture_amount** | **float** | Amount in capture currency | 
**source_amount_refund_modifier** | **float** | The delta from the original source amount after a refund occurred | 
**display_amount_refund_modifier** | **float** | The delta from the original display amount after a refund occurred | 
**supplier_amount_refund_modifier** | **float** | The delta from the original supplier amount after a refund occurred | 
**internal_amount_refund_modifier** | **float** | The delta from the original internal amount after a refund occurred | 
**capture_amount_refund_modifier** | **float** | The delta from the original capture amount after a refund occurred | 
**pending_refunds** | **List[object]** |  | [optional] 
**net_source_amount** | **float** | Source amount minus source modifier. | 
**net_display_amount** | **float** | Display amount minus display modifier. | 
**net_supplier_amount** | **float** | Supplier amount minus supplier modifier. | 
**net_internal_amount** | **float** | Internal amount minus internal modifier. | 
**net_capture_amount** | **float** | Capture amount minus capture modifier. | 
**reconciled** | **bool** | Whether a funds transfer has occurred for this booking. | [optional] 
**metadata** | **Dict[str, str]** | Place to add more data related to the beneficiary. | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.beneficiary_supplier_details import BeneficiarySupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BeneficiarySupplierDetails from a JSON string
beneficiary_supplier_details_instance = BeneficiarySupplierDetails.from_json(json)
# print the JSON string representation of the object
print(BeneficiarySupplierDetails.to_json())

# convert the object into a dict
beneficiary_supplier_details_dict = beneficiary_supplier_details_instance.to_dict()
# create an instance of BeneficiarySupplierDetails from a dict
beneficiary_supplier_details_from_dict = BeneficiarySupplierDetails.from_dict(beneficiary_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


