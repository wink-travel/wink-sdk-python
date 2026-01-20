# CancellationPolicyExceptionSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellation_policy_identifier** | **UUID** | Cancellation policy | 
**cancellation_policy** | [**CancellationPolicyLightweightSupplierDetails**](CancellationPolicyLightweightSupplierDetails.md) | Cancellation policy | 
**start_date** | **date** | Start date for when this cancellation policy should start to override the default cancellation policy. | 
**end_date** | **date** | End date for when this cancellation policy should end overriding the default cancellation policy. | 

## Example

```python
from wink_sdk_extranet_booking.models.cancellation_policy_exception_supplier_details import CancellationPolicyExceptionSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CancellationPolicyExceptionSupplierDetails from a JSON string
cancellation_policy_exception_supplier_details_instance = CancellationPolicyExceptionSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(CancellationPolicyExceptionSupplierDetails.to_json())

# convert the object into a dict
cancellation_policy_exception_supplier_details_dict = cancellation_policy_exception_supplier_details_instance.to_dict()
# create an instance of CancellationPolicyExceptionSupplierDetails from a dict
cancellation_policy_exception_supplier_details_from_dict = CancellationPolicyExceptionSupplierDetails.from_dict(cancellation_policy_exception_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


