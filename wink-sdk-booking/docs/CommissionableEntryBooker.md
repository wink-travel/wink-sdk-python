# CommissionableEntryBooker

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
from wink_sdk_booking.models.commissionable_entry_booker import CommissionableEntryBooker

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionableEntryBooker from a JSON string
commissionable_entry_booker_instance = CommissionableEntryBooker.from_json(json)
# print the JSON string representation of the object
print(CommissionableEntryBooker.to_json())

# convert the object into a dict
commissionable_entry_booker_dict = commissionable_entry_booker_instance.to_dict()
# create an instance of CommissionableEntryBooker from a dict
commissionable_entry_booker_from_dict = CommissionableEntryBooker.from_dict(commissionable_entry_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


