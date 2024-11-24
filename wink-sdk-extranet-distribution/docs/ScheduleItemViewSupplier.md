# ScheduleItemViewSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique document identifier | [optional] [readonly] 
**created_date** | **datetime** | Datetime this record was first created | [optional] [readonly] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] [readonly] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] [readonly] 
**data** | [**ScheduleItemSupplier**](ScheduleItemSupplier.md) |  | 

## Example

```python
from wink_sdk_extranet_distribution.models.schedule_item_view_supplier import ScheduleItemViewSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleItemViewSupplier from a JSON string
schedule_item_view_supplier_instance = ScheduleItemViewSupplier.from_json(json)
# print the JSON string representation of the object
print(ScheduleItemViewSupplier.to_json())

# convert the object into a dict
schedule_item_view_supplier_dict = schedule_item_view_supplier_instance.to_dict()
# create an instance of ScheduleItemViewSupplier from a dict
schedule_item_view_supplier_from_dict = ScheduleItemViewSupplier.from_dict(schedule_item_view_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


