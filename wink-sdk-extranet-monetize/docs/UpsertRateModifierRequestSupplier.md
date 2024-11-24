# UpsertRateModifierRequestSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Internal name of promotion. | 
**type** | **str** | Set whether you want the price to go up or down when the rules of this promotion have been satisfied. | 
**modifier** | [**VariableChargeSupplier**](VariableChargeSupplier.md) |  | 
**enabled** | **bool** | Whether this promotion is enabled or not. | [default to True]
**pricing_type** | **str** | This determines whether this discount should be applied per night, per stay or per person - per night | 
**descriptions** | [**List[LocalizedDescriptionSupplier]**](LocalizedDescriptionSupplier.md) | Localized descriptions describing promotion. At least one English entry is required. | 
**city_rate_qualifiers** | [**List[CityRateQualifierSupplier]**](CityRateQualifierSupplier.md) | Restrict promotion to specific cities. See [Geo-IP city geoname data](#operation/searchForCity) | [optional] 
**continent_rate_qualifiers** | [**List[ContinentRateQualifierSupplier]**](ContinentRateQualifierSupplier.md) | Restrict promotion to specific continents. See [Geo-IP continent geoname data](#operation/showContinents) | [optional] 
**country_rate_qualifiers** | [**List[CountryRateQualifierSupplier]**](CountryRateQualifierSupplier.md) | Restrict promotion to specific countries. See [Geo-IP country geoname data](#operation/showCountries) | [optional] 
**promotion_rate_qualifiers** | [**List[PromotionRateQualifierSupplier]**](PromotionRateQualifierSupplier.md) | Restrict promotion by requiring users to enter a promo code. | [optional] 
**ip_range_rate_qualifiers** | [**List[IPRangeRateQualifierSupplier]**](IPRangeRateQualifierSupplier.md) | Restrict promotion to specific IP ranges. | [optional] 
**room_range_rate_qualifier** | [**RoomRangeRateQualifierSupplier**](RoomRangeRateQualifierSupplier.md) |  | [optional] 
**prepay_rate_qualifier** | [**PrepayRateQualifierSupplier**](PrepayRateQualifierSupplier.md) |  | [optional] 
**refundable_rate_qualifier** | [**RefundableRateQualifierSupplier**](RefundableRateQualifierSupplier.md) |  | [optional] 
**timezone_rate_qualifiers** | [**List[TimezoneRateQualifierSupplier]**](TimezoneRateQualifierSupplier.md) | Restrict promotion to specific time zones. See [Geo-IP timezone geoname data](#operation/showTimezones) | [optional] 
**last_minute_rate_qualifier** | [**MinutesBeforeBookingStartDateRateQualifierSupplier**](MinutesBeforeBookingStartDateRateQualifierSupplier.md) |  | [optional] 
**length_of_stay_rate_qualifier** | [**LengthOfStayRateQualifierSupplier**](LengthOfStayRateQualifierSupplier.md) |  | [optional] 
**advance_booking_rate_qualifier** | [**AdvanceBookingRateQualifierSupplier**](AdvanceBookingRateQualifierSupplier.md) |  | [optional] 
**stay_date_rate_qualifiers** | [**List[StayDateRateQualifierSupplier]**](StayDateRateQualifierSupplier.md) | Restrict promotion to specific stay dates the user wants to arrive. | [optional] 
**sell_date_rate_qualifiers** | [**List[SellDateRateQualifierSupplier]**](SellDateRateQualifierSupplier.md) | Restrict promotion to specific dates the booking is made. | [optional] 
**available_days_of_week_rate_qualifier** | [**AvailableDaysOfWeekRateQualifierSupplier**](AvailableDaysOfWeekRateQualifierSupplier.md) |  | [optional] 
**arrival_days_of_week_rate_qualifier** | [**ArrivalDaysOfWeekRateQualifierSupplier**](ArrivalDaysOfWeekRateQualifierSupplier.md) |  | [optional] 
**departure_days_of_week_rate_qualifier** | [**DepartureDaysOfWeekRateQualifierSupplier**](DepartureDaysOfWeekRateQualifierSupplier.md) |  | [optional] 
**required_days_of_week_rate_qualifier** | [**RequiredDaysOfWeekRateQualifierSupplier**](RequiredDaysOfWeekRateQualifierSupplier.md) |  | [optional] 
**master_rate_identifiers** | **List[str]** | Restrict on specific master rates. | [optional] 
**add_on_identifiers** | **List[str]** | Restrict on specific add-ons. | [optional] 
**rate_plan_identifiers** | **List[str]** | Restrict on specific rate plans. | [optional] 
**blackout_dates** | [**List[BlackoutDateSupplier]**](BlackoutDateSupplier.md) | Exclude this promotion from specific date ranges. | [optional] 

## Example

```python
from wink_sdk_extranet_monetize.models.upsert_rate_modifier_request_supplier import UpsertRateModifierRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertRateModifierRequestSupplier from a JSON string
upsert_rate_modifier_request_supplier_instance = UpsertRateModifierRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(UpsertRateModifierRequestSupplier.to_json())

# convert the object into a dict
upsert_rate_modifier_request_supplier_dict = upsert_rate_modifier_request_supplier_instance.to_dict()
# create an instance of UpsertRateModifierRequestSupplier from a dict
upsert_rate_modifier_request_supplier_from_dict = UpsertRateModifierRequestSupplier.from_dict(upsert_rate_modifier_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


