# CreateScheduleItemRequestSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **datetime** | Start date time of scheduled event | 
**end** | **datetime** | End date time of scheduled event | 
**start_timezone** | **str** | Schedule timezone | 
**end_timezone** | **str** | Schedule timezone | 
**is_all_day** | **bool** | Flag indicating whether this is an all day event. | [default to False]
**recurrence_rule** | **str** | If rule is present, indicates that scheduled event is a recurring event. For more details go to the [iCalendar website](https://icalendar.org/) | [optional] 
**recurrence_id** | **str** | The parent ID of the recurring event. | [optional] 
**recurrence_exception** | **List[datetime]** | Exceptions to the recurrence rule. | [optional] 
**booking_identifier** | **UUID** | Booking identifier this scheduled event was created as part of. | 
**type** | **str** | The type of travel inventory. | 
**attendees** | **int** | Number of guests attending this event. | [default to 1]

## Example

```python
from wink_sdk_extranet_distribution.models.create_schedule_item_request_supplier import CreateScheduleItemRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScheduleItemRequestSupplier from a JSON string
create_schedule_item_request_supplier_instance = CreateScheduleItemRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(CreateScheduleItemRequestSupplier.to_json())

# convert the object into a dict
create_schedule_item_request_supplier_dict = create_schedule_item_request_supplier_instance.to_dict()
# create an instance of CreateScheduleItemRequestSupplier from a dict
create_schedule_item_request_supplier_from_dict = CreateScheduleItemRequestSupplier.from_dict(create_schedule_item_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


