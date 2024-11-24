# BookingContractPaymentDetailsSupplier

Payment details the merchant provided us at the time of payment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquirer_identifier** | **str** | Unique acquiring identifier. Blank for agent payment | 
**vendor** | **str** | Name of acquiring vendor | 
**transaction_identifier** | **str** | Unique transaction id from the vendor. Agent adds their transaction identifier. | 
**customer_identifier** | **str** | Unique customer id from the vendor. Agent adds their own customer identifier. | 
**charge_identifier** | **str** | Unique charge id from the vendor.. | 
**status** | **str** | Unique transaction id from the vendor upon a successful sale. Agent adds their transaction identifier. | 
**agent_invoiced_date** | **datetime** | The date/time the invoice was generated | [optional] 
**agent_invoice_identifier** | **str** | The specific invoice this booking was registered on | [optional] 
**redirect_url** | **str** | Where to redirect to after payment [in-]complete | [optional] 
**fees** | [**List[FeeSupplier]**](FeeSupplier.md) |  | [optional] 
**vendor_specific** | **Dict[str, str]** | Vendor specific values that are returned in a successful response | 

## Example

```python
from wink_sdk_extranet_booking.models.booking_contract_payment_details_supplier import BookingContractPaymentDetailsSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of BookingContractPaymentDetailsSupplier from a JSON string
booking_contract_payment_details_supplier_instance = BookingContractPaymentDetailsSupplier.from_json(json)
# print the JSON string representation of the object
print(BookingContractPaymentDetailsSupplier.to_json())

# convert the object into a dict
booking_contract_payment_details_supplier_dict = booking_contract_payment_details_supplier_instance.to_dict()
# create an instance of BookingContractPaymentDetailsSupplier from a dict
booking_contract_payment_details_supplier_from_dict = BookingContractPaymentDetailsSupplier.from_dict(booking_contract_payment_details_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


