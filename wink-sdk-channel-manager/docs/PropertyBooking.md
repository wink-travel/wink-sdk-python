# PropertyBooking


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**booking_identifier** | **str** | Booking ID | 
**property_identifier** | **str** | ChannelManagerProperty ID | 
**room_rate_identifier** | **str** | Master Rate ID | 
**name** | **str** | Master Rate name | 
**guest_room_name** | **str** | Guest room name | 
**rate_plan_name** | **str** | Rate plan name | 
**rooms** | **int** | Number of rooms | 
**guests** | **int** | Number of guests | 
**adults** | **int** | Number of adults | 
**children** | **int** | Number of children | 
**first_name** | **str** | First name of traveler | 
**last_name** | **str** | Last name of traveler | 
**email** | **str** | E-mail of traveler | 
**amount** | **float** | Total booking amount | 
**currency_code** | **str** | Supplier currency | 
**booking_code** | **str** | Ref. code for traveler | 
**start_date** | **date** | Arrival date | 
**end_date** | **date** | Departure date | 
**created_date** | **datetime** | Created date | 
**cancelled** | **bool** | Whether booking is cancelled or not | 
**cancel_date** | **datetime** | Cancellation date if booking was cancelled | [optional] 
**payment_method_type** | **str** | Payment method | 
**payment_wallet_type** | **str** | Optional payment wallet type | [optional] 
**payment_method_status** | **str** | Status of payment | 
**sales_channel_name** | **str** | Sales channel name | 
**sales_channel_identifier** | **str** | Sales channel ID | 

## Example

```python
from wink_sdk_channel_manager.models.property_booking import PropertyBooking

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyBooking from a JSON string
property_booking_instance = PropertyBooking.from_json(json)
# print the JSON string representation of the object
print(PropertyBooking.to_json())

# convert the object into a dict
property_booking_dict = property_booking_instance.to_dict()
# create an instance of PropertyBooking from a dict
property_booking_from_dict = PropertyBooking.from_dict(property_booking_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


