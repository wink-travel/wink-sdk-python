# RoomStayBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**PropertyPolicyBooker**](PropertyPolicyBooker.md) | Property policy information. | 
**room** | [**GuestRoomLightweightBooker**](GuestRoomLightweightBooker.md) | Guest room details. | 
**rooms** | **int** | Number of rooms. Always 1 since we switched to creating one booking per room. | [default to 1]
**bedroom_configuration** | [**BedroomConfigurationBooker**](BedroomConfigurationBooker.md) | Desired bedroom layout | 
**adults** | **int** | The actual amount of adults as determined by the hotel&#39;s policy. | [default to 2]
**children** | **int** | The actual amount of children as determined by the hotel&#39;s policy. | [default to 0]
**start_date** | **date** | Stay start date | 
**end_date** | **date** | Stay end date | 
**price** | [**StayRateBooker**](StayRateBooker.md) | Price details | 
**room_rate_identifier** | **str** | Master rate identifier | 
**room_rate_internal_name** | **str** | Master rate internal name | 
**rate_plan** | [**RoomConfigurationPriceRatePlanBooker**](RoomConfigurationPriceRatePlanBooker.md) | Rate plan used for this stay | 
**perk_types** | [**List[PerkLightweightBooker]**](PerkLightweightBooker.md) | List of perks that came with the master rate | [optional] 
**extra_charges** | [**ExtraChargesBooker**](ExtraChargesBooker.md) | Rate plan-level extra charges | 
**active_cancellation_policy** | [**CancellationPolicyLightweightBooker**](CancellationPolicyLightweightBooker.md) | Based on the itinerary, the cancellation policy could be taken directly from the rate plan or it could be a policy exception also listed on the rate plan | 
**cancellable** | **bool** |  | [optional] 
**cancellable_by_hotel** | **bool** |  | [optional] 
**cancellable_with_potential_charge** | **bool** |  | [optional] 
**source_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**user_specified_currency_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**internal_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**guests** | **int** |  | [optional] 
**room_nights** | **int** | Total number of nights the guest stays at the hotel. -1 indicates there is an error. | [optional] 
**rate_source** | **str** |  | [optional] 

## Example

```python
from wink_sdk_booking.models.room_stay_booker import RoomStayBooker

# TODO update the JSON string below
json = "{}"
# create an instance of RoomStayBooker from a JSON string
room_stay_booker_instance = RoomStayBooker.from_json(json)
# print the JSON string representation of the object
print(RoomStayBooker.to_json())

# convert the object into a dict
room_stay_booker_dict = room_stay_booker_instance.to_dict()
# create an instance of RoomStayBooker from a dict
room_stay_booker_from_dict = RoomStayBooker.from_dict(room_stay_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


