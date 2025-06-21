# SpecialRateLightweightAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique record identifier | 
**hotel_identifier** | **str** | Hotel identifier. | 
**name** | **str** | Internal name of promotion. | 
**type** | **str** | Set whether you want the price to go up or down when the rules of this promotion have been satisfied. | 
**modifier** | **object** |  | 
**enabled** | **bool** | Whether this promotion is enabled or not. | [default to True]
**pricing_type** | **str** | This determines whether this discount should be applied per night, per stay or per person - per night | 
**descriptions** | [**List[LocalizedDescriptionAffiliate]**](LocalizedDescriptionAffiliate.md) | Localized descriptions describing promotion. At least one English entry is required. | 
**city_rate_qualifiers** | **List[object]** | Restrict promotion to specific cities. See [Geo-IP city geoname data](#operation/searchForCity) | [optional] 
**continent_rate_qualifiers** | **List[object]** | Restrict promotion to specific continents. See [Geo-IP continent geoname data](#operation/showContinents) | [optional] 
**country_rate_qualifiers** | **List[object]** | Restrict promotion to specific countries. See [Geo-IP country geoname data](#operation/showCountries) | [optional] 
**promotion_rate_qualifiers** | **List[object]** | Restrict promotion by requiring users to enter a promo code. | [optional] 
**ip_range_rate_qualifiers** | **List[object]** | Restrict promotion to specific IP ranges. | [optional] 
**room_range_rate_qualifier** | **object** |  | [optional] 
**prepay_rate_qualifier** | **object** |  | [optional] 
**refundable_rate_qualifier** | **object** |  | [optional] 
**timezone_rate_qualifiers** | **List[object]** | Restrict promotion to specific time zones. See [Geo-IP timezone geoname data](#operation/showTimezones) | [optional] 
**last_minute_rate_qualifier** | **object** |  | [optional] 
**length_of_stay_rate_qualifier** | **object** |  | [optional] 
**advance_booking_rate_qualifier** | **object** |  | [optional] 
**stay_date_rate_qualifiers** | **List[object]** | Restrict promotion to specific stay dates the user wants to arrive. | [optional] 
**sell_date_rate_qualifiers** | **List[object]** | Restrict promotion to specific dates the booking is made. | [optional] 
**available_days_of_week_rate_qualifier** | **object** |  | [optional] 
**arrival_days_of_week_rate_qualifier** | **object** |  | [optional] 
**departure_days_of_week_rate_qualifier** | **object** |  | [optional] 
**required_days_of_week_rate_qualifier** | **object** |  | [optional] 
**master_rate_identifiers** | **List[str]** | Restrict on specific master rates. | [optional] 
**add_on_identifiers** | **List[str]** | Restrict on specific add-ons. | [optional] 
**rate_plan_identifiers** | **List[str]** | Restrict on specific rate plans. | [optional] 
**blackout_dates** | **List[object]** | Exclude this promotion from specific date ranges. | [optional] 

## Example

```python
from wink_sdk_affiliate_browse.models.special_rate_lightweight_affiliate import SpecialRateLightweightAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialRateLightweightAffiliate from a JSON string
special_rate_lightweight_affiliate_instance = SpecialRateLightweightAffiliate.from_json(json)
# print the JSON string representation of the object
print(SpecialRateLightweightAffiliate.to_json())

# convert the object into a dict
special_rate_lightweight_affiliate_dict = special_rate_lightweight_affiliate_instance.to_dict()
# create an instance of SpecialRateLightweightAffiliate from a dict
special_rate_lightweight_affiliate_from_dict = SpecialRateLightweightAffiliate.from_dict(special_rate_lightweight_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


