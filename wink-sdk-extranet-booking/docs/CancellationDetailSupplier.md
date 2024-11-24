# CancellationDetailSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellation_type** | **str** | Cancellation type | 
**reason** | **str** | Reason for cancellation | 

## Example

```python
from wink_sdk_extranet_booking.models.cancellation_detail_supplier import CancellationDetailSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of CancellationDetailSupplier from a JSON string
cancellation_detail_supplier_instance = CancellationDetailSupplier.from_json(json)
# print the JSON string representation of the object
print(CancellationDetailSupplier.to_json())

# convert the object into a dict
cancellation_detail_supplier_dict = cancellation_detail_supplier_instance.to_dict()
# create an instance of CancellationDetailSupplier from a dict
cancellation_detail_supplier_from_dict = CancellationDetailSupplier.from_dict(cancellation_detail_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


