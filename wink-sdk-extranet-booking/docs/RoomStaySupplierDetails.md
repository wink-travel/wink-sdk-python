# RoomStaySupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**PropertyPolicySupplierDetails**](PropertyPolicySupplierDetails.md) | Property policy information. | 
**room** | [**GuestRoomLightweightSupplierDetails**](GuestRoomLightweightSupplierDetails.md) | Guest room details. | 
**rooms** | **int** | Number of rooms. Always 1 since we switched to creating one booking per room. | [default to 1]
**bedroom_configuration** | [**BedroomConfigurationSupplierDetails**](BedroomConfigurationSupplierDetails.md) | Desired bedroom layout | 
**adults** | **int** | The actual amount of adults as determined by the hotel&#39;s policy. | [default to 2]
**children** | **int** | The actual amount of children as determined by the hotel&#39;s policy. | [default to 0]
**start_date** | **date** | Stay start date | 
**end_date** | **date** | Stay end date | 
**price** | [**StayRateSupplierDetails**](StayRateSupplierDetails.md) | Price details | 
**room_rate_identifier** | **str** | Master rate identifier | 
**room_rate_internal_name** | **str** | Master rate internal name | 
**rate_plan** | [**RoomConfigurationPriceRatePlanSupplierDetails**](RoomConfigurationPriceRatePlanSupplierDetails.md) | Rate plan used for this stay | 
**perk_types** | [**List[PerkLightweightSupplierDetails]**](PerkLightweightSupplierDetails.md) | List of perks that came with the master rate | [optional] 
**extra_charges** | [**ExtraChargesSupplierDetails**](ExtraChargesSupplierDetails.md) | Rate plan-level extra charges | 
**active_cancellation_policy** | [**CancellationPolicyLightweightSupplierDetails**](CancellationPolicyLightweightSupplierDetails.md) | Based on the itinerary, the cancellation policy could be taken directly from the rate plan or it could be a policy exception also listed on the rate plan | 
**room_nights** | **int** | Total number of nights the guest stays at the hotel. -1 indicates there is an error. | [optional] 
**cancellable_by_hotel** | **bool** |  | [optional] 
**cancellable_with_potential_charge** | **bool** |  | [optional] 
**guests** | **int** |  | [optional] 
**rate_source** | **str** |  | [optional] 
**source_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**user_specified_currency_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**internal_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**cancellable** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.room_stay_supplier_details import RoomStaySupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RoomStaySupplierDetails from a JSON string
room_stay_supplier_details_instance = RoomStaySupplierDetails.from_json(json)
# print the JSON string representation of the object
print(RoomStaySupplierDetails.to_json())

# convert the object into a dict
room_stay_supplier_details_dict = room_stay_supplier_details_instance.to_dict()
# create an instance of RoomStaySupplierDetails from a dict
room_stay_supplier_details_from_dict = RoomStaySupplierDetails.from_dict(room_stay_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


