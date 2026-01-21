# RoomConfigurationPriceSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channel_inventory_identifier** | **str** | Sales channel inventory identifier | 
**list** | [**List[LocalizedTransactionalTravelInventorySupplierDetails]**](LocalizedTransactionalTravelInventorySupplierDetails.md) |  | [optional] 
**commissionable** | **bool** | Whether this package is commissionable based on the incoming sales channel. | 
**commission** | **float** | The commission percentage. | 
**direct** | **bool** | Indicates whether the blocking from sales channel is direct or not. If you are a travel agent doing your own acquiring, this flag has to be true to make a booking. | [default to False]
**adults** | **int** | The actual amount of adults as determined by the hotel&#39;s policy | 
**children** | **int** | The actual amount of children as determined by the hotel&#39;s policy | [optional] 
**start_date** | **date** | SimpleDateTimeItinerary startDate | 
**end_date** | **date** | SimpleDateTimeItinerary endDate | 
**room_rate_identifier** | **str** | Specified master rate identifier | 
**room_rate_internal_name** | **str** | Specified master rate internal name | 
**rate_plan** | [**RoomConfigurationPriceRatePlanSupplierDetails**](RoomConfigurationPriceRatePlanSupplierDetails.md) | Specified rate plan | 
**perk_types** | [**List[PerkLightweightSupplierDetails]**](PerkLightweightSupplierDetails.md) |  | [optional] 
**price** | [**StayRateSupplierDetails**](StayRateSupplierDetails.md) | Calculated price | 
**extra_charges** | [**ExtraChargesSupplierDetails**](ExtraChargesSupplierDetails.md) | Per rate plan level extra charges with localized prices | [optional] 
**configuration** | [**RoomConfigurationSupplierDetails**](RoomConfigurationSupplierDetails.md) | The selected room configuration that created this record | 
**add_on_offers** | [**List[AddOnLocalizedInventorySupplierDetails]**](AddOnLocalizedInventorySupplierDetails.md) |  | [optional] 
**perk_value** | **int** | The combined value of these perkTypes | [optional] 
**active_cancellation_policy** | [**CancellationPolicyLightweightSupplierDetails**](CancellationPolicyLightweightSupplierDetails.md) | The active / selected cancellation policy for this room configuration | 
**room_nights** | **int** | Number of nights the guests will be staying | 
**price_list** | [**List[LocalizedTransactionalTravelInventorySupplierDetails]**](LocalizedTransactionalTravelInventorySupplierDetails.md) |  | [optional] 
**source_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**user_specified_currency_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**internal_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**available** | **bool** |  | [optional] 
**rate_source** | **str** |  | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.room_configuration_price_supplier_details import RoomConfigurationPriceSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RoomConfigurationPriceSupplierDetails from a JSON string
room_configuration_price_supplier_details_instance = RoomConfigurationPriceSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(RoomConfigurationPriceSupplierDetails.to_json())

# convert the object into a dict
room_configuration_price_supplier_details_dict = room_configuration_price_supplier_details_instance.to_dict()
# create an instance of RoomConfigurationPriceSupplierDetails from a dict
room_configuration_price_supplier_details_from_dict = RoomConfigurationPriceSupplierDetails.from_dict(room_configuration_price_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


