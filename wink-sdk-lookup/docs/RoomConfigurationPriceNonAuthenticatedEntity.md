# RoomConfigurationPriceNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_inventory_identifier** | **str** | Sales channel inventory identifier | 
**list** | [**List[LocalizedTransactionalTravelInventoryNonAuthenticatedEntity]**](LocalizedTransactionalTravelInventoryNonAuthenticatedEntity.md) |  | [optional] 
**commissionable** | **bool** | Whether this package is commissionable based on the incoming sales channel. | 
**commission** | **float** | The commission percentage. | 
**direct** | **bool** | Indicates whether the blocking from sales channel is direct or not. If you are a travel agent doing your own acquiring, this flag has to be true to make a booking. | [default to False]
**adults** | **int** | The actual amount of adults as determined by the hotel&#39;s policy | 
**children** | **int** | The actual amount of children as determined by the hotel&#39;s policy | [optional] 
**start_date** | **date** | SimpleDateTimeItinerary startDate | 
**end_date** | **date** | SimpleDateTimeItinerary endDate | 
**room_rate_identifier** | **str** | Specified master rate identifier | 
**room_rate_internal_name** | **str** | Specified master rate internal name | 
**rate_plan** | [**RoomConfigurationPriceRatePlanNonAuthenticatedEntity**](RoomConfigurationPriceRatePlanNonAuthenticatedEntity.md) | Specified rate plan | 
**perk_types** | [**List[PerkLightweightNonAuthenticatedEntity]**](PerkLightweightNonAuthenticatedEntity.md) |  | [optional] 
**price** | [**StayRateNonAuthenticatedEntity**](StayRateNonAuthenticatedEntity.md) | Calculated price | 
**extra_charges** | [**ExtraChargesNonAuthenticatedEntity**](ExtraChargesNonAuthenticatedEntity.md) | Per rate plan level extra charges with localized prices | [optional] 
**configuration** | [**RoomConfigurationNonAuthenticatedEntity**](RoomConfigurationNonAuthenticatedEntity.md) | The selected room configuration that created this record | 
**add_on_offers** | [**List[AddOnLocalizedInventoryNonAuthenticatedEntity]**](AddOnLocalizedInventoryNonAuthenticatedEntity.md) |  | [optional] 
**perk_value** | **int** | The combined value of these perkTypes | [optional] 
**active_cancellation_policy** | [**CancellationPolicyLightweightNonAuthenticatedEntity**](CancellationPolicyLightweightNonAuthenticatedEntity.md) | The active / selected cancellation policy for this room configuration | 
**room_nights** | **int** | Number of nights the guests will be staying | 
**price_list** | [**List[LocalizedTransactionalTravelInventoryNonAuthenticatedEntity]**](LocalizedTransactionalTravelInventoryNonAuthenticatedEntity.md) |  | [optional] 
**source_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**user_specified_currency_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**internal_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**available** | **bool** |  | [optional] 
**rate_source** | **str** |  | [optional] 

## Example

```python
from wink_sdk_lookup.models.room_configuration_price_non_authenticated_entity import RoomConfigurationPriceNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of RoomConfigurationPriceNonAuthenticatedEntity from a JSON string
room_configuration_price_non_authenticated_entity_instance = RoomConfigurationPriceNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(RoomConfigurationPriceNonAuthenticatedEntity.to_json())

# convert the object into a dict
room_configuration_price_non_authenticated_entity_dict = room_configuration_price_non_authenticated_entity_instance.to_dict()
# create an instance of RoomConfigurationPriceNonAuthenticatedEntity from a dict
room_configuration_price_non_authenticated_entity_from_dict = RoomConfigurationPriceNonAuthenticatedEntity.from_dict(room_configuration_price_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


