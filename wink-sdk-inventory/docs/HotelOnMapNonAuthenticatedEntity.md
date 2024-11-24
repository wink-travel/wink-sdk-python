# HotelOnMapNonAuthenticatedEntity

Property details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique record identifier. This is NOT the same as the unique hotel record identifier. | [optional] 
**hotel_identifier** | **str** | Unique hotel record identifier. | [optional] 
**name** | **str** | Hotel trade name | [optional] 
**local_name** | **str** | Hotel local name if different from the trade name or if it is the local language. | [optional] 
**chain** | **str** | Name of hotel chain if applicable. | [optional] 
**brand** | **str** | Name of hotel brand | [optional] 
**url_name** | **str** | Unique URL-friendly name slug of hotel | [optional] 
**star_rating** | **int** | Official or self-designated property star rating. Note that in some regions there are 6-star hotels. They are the same as 5-star hotels everywhere else. | [optional] 
**bookings** | **int** | Number of bookings for this property on the wink.travel platform. | [optional] [default to 0]
**aggregate_review_rating** | **float** | Aggregate score based on all current user reviews. | [optional] [default to 0.0]
**location** | [**GeoJsonPointNonAuthenticatedEntity**](GeoJsonPointNonAuthenticatedEntity.md) |  | [optional] 
**short_descriptions** | [**List[LocalizedDescriptionNonAuthenticatedEntity]**](LocalizedDescriptionNonAuthenticatedEntity.md) | A localized list of short property descriptions | [optional] 
**long_descriptions** | [**List[LocalizedDescriptionNonAuthenticatedEntity]**](LocalizedDescriptionNonAuthenticatedEntity.md) | A localized list of longer property descriptions | [optional] 
**aggregate_greendex_rating** | **float** | Aggregate Green Index score if the property has answered our questionnaire available in the Extranet. | [optional] [default to 0.0]
**lifestyle_types** | **List[str]** |  | [optional] 
**total_reviews** | **int** | Count of total reviews left by users at this property. | [optional] [default to 0]
**available** | **bool** | Flag indicating whether the reactive has made this property available for sale. | [optional] [default to False]
**hotel_available** | **bool** | Flag indicating whether the property has made this property available for sale. | [optional] [default to False]
**reservations** | [**ContactNonAuthenticatedEntity**](ContactNonAuthenticatedEntity.md) |  | [optional] 
**socials** | [**List[SocialNonAuthenticatedEntity]**](SocialNonAuthenticatedEntity.md) | Property&#39;s social network accounts | [optional] 
**images** | [**List[SimpleMultimediaNonAuthenticatedEntity]**](SimpleMultimediaNonAuthenticatedEntity.md) | Property images. | [optional] 
**videos** | [**List[SimpleMultimediaNonAuthenticatedEntity]**](SimpleMultimediaNonAuthenticatedEntity.md) | Property videos. | [optional] 
**policy** | [**PropertyPolicyNonAuthenticatedEntity**](PropertyPolicyNonAuthenticatedEntity.md) |  | [optional] 
**third_party_reviews** | [**List[TravelInventoryRecognitionNonAuthenticatedEntity]**](TravelInventoryRecognitionNonAuthenticatedEntity.md) | Array of awards and third party reviews given to property by certified / non-certified providers. | [optional] 
**attractions** | **int** | Number of attractions property has listed on its profile. | [optional] [default to 0]
**recreations** | **int** | Number of activites property has listed on its profile. | [optional] [default to 0]
**pois** | **int** | Number of places property has listed on its profile. | [optional] [default to 0]
**restaurants** | **int** | Number of restaurants property has on its profile. | [optional] [default to 0]
**meeting_rooms** | **int** | Number of meeting rooms property has on its profile. | [optional] [default to 0]
**spas** | **int** | Number of spas property has on its profile. | [optional] [default to 0]
**add_ons** | **int** | Number of add-ons property has on its profile. | [optional] [default to 0]
**general_manager** | [**GeneralManagerNonAuthenticatedEntity**](GeneralManagerNonAuthenticatedEntity.md) |  | [optional] 
**location_category** | **str** | Supported OTA specification &#x60;LOC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**segment_category** | **str** | Supported OTA specification &#x60;SEG&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**hotel_category** | **str** | Supported OTA specification &#x60;PCT&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**architectural_style** | **str** | Supported OTA specification &#x60;ARC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**when_built** | **str** | Year the property was constructed. | [optional] 
**currency_code** | **str** | Currency code for property. | [optional] 
**membership_rate_discount** | **float** | A property&#39;s price score is based on calculating historical pricing data. Each property receives a unique score. There is no max score; it&#39;s there to compare it against other properties. | [optional] [default to 0]
**price_score** | **int** | A property&#39;s price score is based on calculating historical pricing data. Each property receives a unique score. There is no max score; it&#39;s there to compare it against other properties. | [optional] [default to 0]
**perk_score** | **int** | A property&#39;s perk score is based on the type of perks that is offered to the guests across all master rates. There is no max score; it&#39;s there to compare it against other properties. | [optional] [default to 0]
**package_score** | **int** | A property&#39;s package score is based on general availability and price for all packages and add-ons offered by the property. There is no max score; it&#39;s there to compare it against other properties. | [optional] [default to 0]
**loyalty_score** | **int** | A property&#39;s loyalty score is based on calculating how many available rate plans honor loyalty points. There is no max score; it&#39;s there to compare it against other properties. | [optional] [default to 0]
**popular_score** | **int** | A property&#39;s popular score is based on calculating number of bookings across room types. There is no max score; it&#39;s there to compare it against other properties. | [optional] [default to 0]
**experience_score** | **int** | A property&#39;s experience score is based on how calculating how many types of experiences are available and at what price ranges. There is no max score; it&#39;s there to compare it against other properties. | [optional] [default to 0]
**availability_score** | **int** | A property&#39;s availability score is based on general availability of all room types. If most room types are always unavailable, the attractiveness of this property goes down. We use this as our primary benchmark to decide how and when to feature properties. There is no max score; it&#39;s there to compare it against other properties. | [optional] [default to 0]
**views** | **int** | Total number of user views of this property. | [optional] [default to 0]
**hotel_amenity_codes** | **List[str]** | Supported OTA specification &#x60;HAC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**property_accessibility_codes** | **List[str]** | Supported OTA specification &#x60;PHY&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**property_security_codes** | **List[str]** | Supported OTA specification &#x60;SEC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**number_of_rooms** | **int** | Number of rooms / keys for this property. | [optional] [default to 0]
**address** | [**AddressNonAuthenticatedEntity**](AddressNonAuthenticatedEntity.md) |  | [optional] 
**active** | **bool** | A property is considered active when both available and hotelAvailable flags are true. | [optional] 
**url_parameters** | **str** | Convenience data point that creates url friendly query parameters of property. | [optional] 

## Example

```python
from wink_sdk_inventory.models.hotel_on_map_non_authenticated_entity import HotelOnMapNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of HotelOnMapNonAuthenticatedEntity from a JSON string
hotel_on_map_non_authenticated_entity_instance = HotelOnMapNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(HotelOnMapNonAuthenticatedEntity.to_json())

# convert the object into a dict
hotel_on_map_non_authenticated_entity_dict = hotel_on_map_non_authenticated_entity_instance.to_dict()
# create an instance of HotelOnMapNonAuthenticatedEntity from a dict
hotel_on_map_non_authenticated_entity_from_dict = HotelOnMapNonAuthenticatedEntity.from_dict(hotel_on_map_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


