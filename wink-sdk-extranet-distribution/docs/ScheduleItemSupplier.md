# ScheduleItemSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**start** | **datetime** | Start date time of scheduled event | [optional] 
**start_timezone** | **str** | Schedule timezone | [optional] 
**end** | **datetime** | End date time of scheduled event | [optional] 
**end_timezone** | **str** | Schedule timezone | [optional] 
**is_all_day** | **bool** | Flag indicating whether this is an all day event. | [optional] [default to False]
**title** | **str** | Title of scheduled event. | [optional] 
**description** | **str** | Description of scheduled event. | [optional] 
**recurrence_rule** | **str** | If rule is present, indicates that scheduled event is a recurring event. For more details go to the [iCalendar website](https://icalendar.org/) | [optional] 
**recurrence_id** | **str** | The parent ID of the recurring event. | [optional] 
**recurrence_exception** | **List[datetime]** | Exceptions to the recurrence rule. | [optional] 
**owner_identifier** | **str** | The unique identifier of the travel blocking you are creating a scheduled event for. | [optional] 
**booking_identifier** | **str** | Booking identifier this scheduled event was created as part of. | [optional] 
**booking_owner_identifier** | **str** | Which company owns this schedule. (Owner of the customization) | [optional] 
**hotel_identifier** | **str** | Hotel identifier that owns the travel blocking. | [optional] 
**type** | **str** | The type of travel blocking. | [optional] 
**attendees** | **int** | Number of guests attending this event. | [optional] [default to 1]
**email** | **str** | Email of the person scheduling this event. | 
**full_name** | **str** | Full name of person scheduling this event. | [optional] 
**first_name** | **str** | First name of person scheduling this event. | [optional] 
**last_name** | **str** | Last name of person scheduling this event. | [optional] 
**venue_name** | **str** | Name of venue attendees will visit. | [optional] 
**localized_venue_name** | **str** | Localized name of venue attendees will visit. | [optional] 
**contact** | [**ContactSupplier**](ContactSupplier.md) | Venue contact person | [optional] 
**address** | [**SimpleAddressSupplier**](SimpleAddressSupplier.md) | Venue address | [optional] 
**created** | **datetime** | Date time this schedule event was created. | [optional] 
**last_modified** | **datetime** | Last date time this scheduled event was modified. | [optional] 
**sequence** | **int** | Schedule event recurring sequence | [optional] [default to 0]
**brand_name** | **str** | Brand name for email header | [optional] 
**email_header_logo_url** | **str** | Venue owner logo | [optional] 
**logo_identifier** | **str** | Cloudinary image identifier of logo | [optional] 
**language** | **str** | User&#39;s desired language | [optional] 
**all_day** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.schedule_item_supplier import ScheduleItemSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleItemSupplier from a JSON string
schedule_item_supplier_instance = ScheduleItemSupplier.from_json(json)
# print the JSON string representation of the object
print(ScheduleItemSupplier.to_json())

# convert the object into a dict
schedule_item_supplier_dict = schedule_item_supplier_instance.to_dict()
# create an instance of ScheduleItemSupplier from a dict
schedule_item_supplier_from_dict = ScheduleItemSupplier.from_dict(schedule_item_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


