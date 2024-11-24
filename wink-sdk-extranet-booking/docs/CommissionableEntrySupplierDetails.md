# CommissionableEntrySupplierDetails

List of all travel inventory entries that are due a commission to the affiliate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**identifier** | **str** |  | 
**type** | **str** |  | 
**commission_percent** | **float** |  | 

## Example

```python
from wink_sdk_extranet_booking.models.commissionable_entry_supplier_details import CommissionableEntrySupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionableEntrySupplierDetails from a JSON string
commissionable_entry_supplier_details_instance = CommissionableEntrySupplierDetails.from_json(json)
# print the JSON string representation of the object
print(CommissionableEntrySupplierDetails.to_json())

# convert the object into a dict
commissionable_entry_supplier_details_dict = commissionable_entry_supplier_details_instance.to_dict()
# create an instance of CommissionableEntrySupplierDetails from a dict
commissionable_entry_supplier_details_from_dict = CommissionableEntrySupplierDetails.from_dict(commissionable_entry_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


