# PropertyAggregateLightweightAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel_identifier** | **str** | Unique hotel record identifier. | [optional] 
**name** | **str** | Hotel trade name | [optional] 
**local_name** | **str** | Hotel local name if different from the trade name or if it is the local language. | [optional] 
**chain** | **str** | Name of hotel chain if applicable. | [optional] 
**brand** | **str** | Name of hotel brand | [optional] 
**url_name** | **str** | Unique URL-friendly name slug of hotel | [optional] 
**unique_id** | **str** | Event shorter name | 
**star_rating** | **int** | Official or self-designated property star rating. Note that in some regions there are 6-star hotels. They are the same as 5-star hotels everywhere else. | [optional] 
**bookings** | **int** | Number of bookings for this property on the wink.travel platform. | [optional] [default to 0]
**aggregate_review_rating** | **float** | Aggregate score based on all current user reviews. | [optional] [default to 0.0]
**location** | [**GeoJsonPointAffiliate**](GeoJsonPointAffiliate.md) | Geo-location | [optional] 
**descriptions** | [**List[SimpleDescriptionAffiliate]**](SimpleDescriptionAffiliate.md) | Short and long welcome text | [optional] 
**aggregate_greendex_rating** | **float** | Aggregate Green Index score if the property has answered our questionnaire available in the Extranet. | [optional] [default to 0.0]
**lifestyle_types** | **List[object]** |  | [optional] 
**total_reviews** | **int** | Count of total reviews left by users at this property. | [optional] [default to 0]
**reservations** | [**ContactAffiliate**](ContactAffiliate.md) | Contact details for reservations desk | [optional] 
**socials** | [**List[SocialAffiliate]**](SocialAffiliate.md) | Property&#39;s social network accounts | [optional] 
**images** | [**List[SimpleMultimediaAffiliate]**](SimpleMultimediaAffiliate.md) | Property images. | [optional] 
**videos** | [**List[SimpleMultimediaAffiliate]**](SimpleMultimediaAffiliate.md) | Property videos. | [optional] 
**policy** | [**PropertyPolicyAffiliate**](PropertyPolicyAffiliate.md) | Basic property policy record. | [optional] 
**third_party_reviews** | [**List[TravelInventoryRecognitionAffiliate]**](TravelInventoryRecognitionAffiliate.md) | Array of awards and third party reviews given to property by certified / non-certified providers. | [optional] 
**attractions** | **int** | Number of attractions property has listed on its profile. | [optional] [default to 0]
**activities** | **int** | Number of activites property has listed on its profile. | [optional] [default to 0]
**places** | **int** | Number of places property has listed on its profile. | [optional] [default to 0]
**restaurants** | **int** | Number of restaurants property has on its profile. | [optional] [default to 0]
**meeting_rooms** | **int** | Number of meeting rooms property has on its profile. | [optional] [default to 0]
**spas** | **int** | Number of spas property has on its profile. | [optional] [default to 0]
**add_ons** | **int** | Number of add-ons property has on its profile. | [optional] [default to 0]
**general_manager** | [**GeneralManagerAffiliate**](GeneralManagerAffiliate.md) |  | [optional] 
**location_category** | **str** | Supported OTA specification &#x60;LOC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**segment_category** | **str** | Supported OTA specification &#x60;SEG&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**hotel_category** | **str** | Supported OTA specification &#x60;PCT&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**architectural_style** | **str** | Supported OTA specification &#x60;ARC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**when_built** | **str** | Year the property was constructed. | [optional] 
**currency_code** | **str** | Currency code for property. | [optional] 
**membership_rate_discount** | **float** | A property&#39;s price score is based on calculating historical pricing data. Each property receives a unique score. There is no max score; it&#39;s there to compare it against other properties. | [optional] [default to 0]
**price_score** | **int** | A property&#39;s price score is based on calculating historical pricing data. Each property receives a unique score. There is no max score; it&#39;s there to compare it against other properties. | [optional] [default to 0]
**perk_score** | **int** | A property&#39;s perk score is based on the type of perks that is offered to the guests across all master rates. There is no max score; it&#39;s there to compare it against other properties. | [optional] [default to 0]
**add_on_score** | **int** | A property&#39;s package score is based on general availability and price for all packages and add-ons offered by the property. There is no max score; it&#39;s there to compare it against other properties. | [optional] [default to 0]
**loyalty_score** | **int** | A property&#39;s loyalty score is based on calculating how many available rate plans honor loyalty points. There is no max score; it&#39;s there to compare it against other properties. | [optional] [default to 0]
**popular_score** | **int** | A property&#39;s popular score is based on calculating number of bookings across room types. There is no max score; it&#39;s there to compare it against other properties. | [optional] [default to 0]
**experience_score** | **int** | A property&#39;s experience score is based on how calculating how many types of experiences are available and at what price ranges. There is no max score; it&#39;s there to compare it against other properties. | [optional] [default to 0]
**hotel_amenity_codes** | **List[str]** | Supported OTA specification &#x60;HAC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**property_accessibility_codes** | **List[str]** | Supported OTA specification &#x60;PHY&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**property_security_codes** | **List[str]** | Supported OTA specification &#x60;SEC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**number_of_rooms** | **int** | Number of rooms / keys for this property. | [optional] [default to 0]
**address** | [**SimpleAddressAffiliate**](SimpleAddressAffiliate.md) | Property address. | [optional] 
**active** | **bool** | Whether property is active | [optional] 
**url_parameters** | **str** | Convenience data point that creates url friendly query parameters of property. | [optional] 

## Example

```python
from wink_sdk_affiliate_browse.models.property_aggregate_lightweight_affiliate import PropertyAggregateLightweightAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyAggregateLightweightAffiliate from a JSON string
property_aggregate_lightweight_affiliate_instance = PropertyAggregateLightweightAffiliate.from_json(json)
# print the JSON string representation of the object
print(PropertyAggregateLightweightAffiliate.to_json())

# convert the object into a dict
property_aggregate_lightweight_affiliate_dict = property_aggregate_lightweight_affiliate_instance.to_dict()
# create an instance of PropertyAggregateLightweightAffiliate from a dict
property_aggregate_lightweight_affiliate_from_dict = PropertyAggregateLightweightAffiliate.from_dict(property_aggregate_lightweight_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


