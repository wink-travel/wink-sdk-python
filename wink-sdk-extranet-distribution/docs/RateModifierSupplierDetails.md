# RateModifierSupplierDetails

Promotions that go together to make up this ancillary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique record identifier | 
**hotel_identifier** | **str** | Hotel identifier. | 
**name** | **str** | Internal name of promotion. | 
**type** | **str** | Set whether you want the price to go up or down when the rules of this promotion have been satisfied. | 
**modifier** | [**VariableChargeSupplierDetails**](VariableChargeSupplierDetails.md) |  | 
**enabled** | **bool** | Whether this promotion is enabled or not. | [default to True]
**pricing_type** | **str** | This determines whether this discount should be applied per night, per stay or per person - per night | 
**descriptions** | [**List[LocalizedDescriptionSupplierDetails]**](LocalizedDescriptionSupplierDetails.md) | Localized descriptions describing promotion. At least one English entry is required. | 
**city_rate_qualifiers** | [**List[CityRateQualifierSupplierDetails]**](CityRateQualifierSupplierDetails.md) | Restrict promotion to specific cities. See [Geo-IP city geoname data](#operation/searchForCity) | [optional] 
**continent_rate_qualifiers** | [**List[ContinentRateQualifierSupplierDetails]**](ContinentRateQualifierSupplierDetails.md) | Restrict promotion to specific continents. See [Geo-IP continent geoname data](#operation/showContinents) | [optional] 
**country_rate_qualifiers** | [**List[CountryRateQualifierSupplierDetails]**](CountryRateQualifierSupplierDetails.md) | Restrict promotion to specific countries. See [Geo-IP country geoname data](#operation/showCountries) | [optional] 
**promotion_rate_qualifiers** | [**List[PromotionRateQualifierSupplierDetails]**](PromotionRateQualifierSupplierDetails.md) | Restrict promotion by requiring users to enter a promo code. | [optional] 
**ip_range_rate_qualifiers** | [**List[IPRangeRateQualifierSupplierDetails]**](IPRangeRateQualifierSupplierDetails.md) | Restrict promotion to specific IP ranges. | [optional] 
**room_range_rate_qualifier** | [**RoomRangeRateQualifierSupplierDetails**](RoomRangeRateQualifierSupplierDetails.md) |  | [optional] 
**prepay_rate_qualifier** | [**PrepayRateQualifierSupplierDetails**](PrepayRateQualifierSupplierDetails.md) |  | [optional] 
**refundable_rate_qualifier** | [**RefundableRateQualifierSupplierDetails**](RefundableRateQualifierSupplierDetails.md) |  | [optional] 
**timezone_rate_qualifiers** | [**List[TimezoneRateQualifierSupplierDetails]**](TimezoneRateQualifierSupplierDetails.md) | Restrict promotion to specific time zones. See [Geo-IP timezone geoname data](#operation/showTimezones) | [optional] 
**last_minute_rate_qualifier** | [**MinutesBeforeBookingStartDateRateQualifierSupplierDetails**](MinutesBeforeBookingStartDateRateQualifierSupplierDetails.md) |  | [optional] 
**length_of_stay_rate_qualifier** | [**LengthOfStayRateQualifierSupplierDetails**](LengthOfStayRateQualifierSupplierDetails.md) |  | [optional] 
**advance_booking_rate_qualifier** | [**AdvanceBookingRateQualifierSupplierDetails**](AdvanceBookingRateQualifierSupplierDetails.md) |  | [optional] 
**stay_date_rate_qualifiers** | [**List[StayDateRateQualifierSupplierDetails]**](StayDateRateQualifierSupplierDetails.md) | Restrict promotion to specific stay dates the user wants to arrive. | [optional] 
**sell_date_rate_qualifiers** | [**List[SellDateRateQualifierSupplierDetails]**](SellDateRateQualifierSupplierDetails.md) | Restrict promotion to specific dates the booking is made. | [optional] 
**available_days_of_week_rate_qualifier** | [**AvailableDaysOfWeekRateQualifierSupplierDetails**](AvailableDaysOfWeekRateQualifierSupplierDetails.md) |  | [optional] 
**arrival_days_of_week_rate_qualifier** | [**ArrivalDaysOfWeekRateQualifierSupplierDetails**](ArrivalDaysOfWeekRateQualifierSupplierDetails.md) |  | [optional] 
**departure_days_of_week_rate_qualifier** | [**DepartureDaysOfWeekRateQualifierSupplierDetails**](DepartureDaysOfWeekRateQualifierSupplierDetails.md) |  | [optional] 
**required_days_of_week_rate_qualifier** | [**RequiredDaysOfWeekRateQualifierSupplierDetails**](RequiredDaysOfWeekRateQualifierSupplierDetails.md) |  | [optional] 
**master_rate_identifiers** | **List[str]** | Restrict on specific master rates. | [optional] 
**add_on_identifiers** | **List[str]** | Restrict on specific add-ons. | [optional] 
**rate_plan_identifiers** | **List[str]** | Restrict on specific rate plans. | [optional] 
**blackout_dates** | [**List[BlackoutDateSupplierDetails]**](BlackoutDateSupplierDetails.md) | Exclude this promotion from specific date ranges. | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.rate_modifier_supplier_details import RateModifierSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RateModifierSupplierDetails from a JSON string
rate_modifier_supplier_details_instance = RateModifierSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(RateModifierSupplierDetails.to_json())

# convert the object into a dict
rate_modifier_supplier_details_dict = rate_modifier_supplier_details_instance.to_dict()
# create an instance of RateModifierSupplierDetails from a dict
rate_modifier_supplier_details_from_dict = RateModifierSupplierDetails.from_dict(rate_modifier_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


