# UpdateScheduleItemRequestSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **datetime** | Start date time of scheduled event | 
**end** | **datetime** | End date time of scheduled event | 
**start_timezone** | **str** | Schedule timezone | 
**end_timezone** | **str** | Schedule timezone | 
**is_all_day** | **bool** | Flag indicating whether this is an all day event. | [default to False]
**attendees** | **int** | Number of guests attending this event. | [default to 1]

## Example

```python
from wink_sdk_extranet_distribution.models.update_schedule_item_request_supplier import UpdateScheduleItemRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateScheduleItemRequestSupplier from a JSON string
update_schedule_item_request_supplier_instance = UpdateScheduleItemRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(UpdateScheduleItemRequestSupplier.to_json())

# convert the object into a dict
update_schedule_item_request_supplier_dict = update_schedule_item_request_supplier_instance.to_dict()
# create an instance of UpdateScheduleItemRequestSupplier from a dict
update_schedule_item_request_supplier_from_dict = UpdateScheduleItemRequestSupplier.from_dict(update_schedule_item_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


