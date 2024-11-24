# RateModifierAffiliate

Promotions that go together to make up this ancillary.

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
**room_range_rate_qualifier** | **object** | Restrict promotion by restricting to how many rooms the user wants. | [optional] 
**prepay_rate_qualifier** | **object** | Restrict promotion to either prepaid / non-prepaid rates. | [optional] 
**refundable_rate_qualifier** | **object** | Restrict promotion to either refundable / non-refundable rates. | [optional] 
**timezone_rate_qualifiers** | **List[object]** | Restrict promotion to specific time zones. See [Geo-IP timezone geoname data](#operation/showTimezones) | [optional] 
**last_minute_rate_qualifier** | **object** | Restrict promotion to users who want to book a room close to the date. | [optional] 
**length_of_stay_rate_qualifier** | **object** | Restrict promotion to users who want to stay a certain number of days. | [optional] 
**advance_booking_rate_qualifier** | **object** | Restrict promotion to users who want to book in advance. | [optional] 
**stay_date_rate_qualifiers** | **List[object]** | Restrict promotion to specific stay dates the user wants to arrive. | [optional] 
**sell_date_rate_qualifiers** | **List[object]** | Restrict promotion to specific dates the booking is made. | [optional] 
**available_days_of_week_rate_qualifier** | **object** | Restrict promotion to specific days of the week the promotion is available. | [optional] 
**arrival_days_of_week_rate_qualifier** | **object** | Restrict promotion to specific days of the week the guest is arriving. | [optional] 
**departure_days_of_week_rate_qualifier** | **object** | Restrict promotion to specific days of the week the guest is departing. | [optional] 
**required_days_of_week_rate_qualifier** | **object** | Restrict promotion to specific days of the week the guest has to stay. | [optional] 
**master_rate_identifiers** | **List[str]** | Restrict on specific master rates. | [optional] 
**add_on_identifiers** | **List[str]** | Restrict on specific add-ons. | [optional] 
**rate_plan_identifiers** | **List[str]** | Restrict on specific rate plans. | [optional] 
**blackout_dates** | **List[object]** | Exclude this promotion from specific date ranges. | [optional] 

## Example

```python
from wink_sdk_affiliate_sales_channel.models.rate_modifier_affiliate import RateModifierAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of RateModifierAffiliate from a JSON string
rate_modifier_affiliate_instance = RateModifierAffiliate.from_json(json)
# print the JSON string representation of the object
print(RateModifierAffiliate.to_json())

# convert the object into a dict
rate_modifier_affiliate_dict = rate_modifier_affiliate_instance.to_dict()
# create an instance of RateModifierAffiliate from a dict
rate_modifier_affiliate_from_dict = RateModifierAffiliate.from_dict(rate_modifier_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


