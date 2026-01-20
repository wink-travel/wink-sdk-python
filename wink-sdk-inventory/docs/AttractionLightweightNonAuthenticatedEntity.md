# AttractionLightweightNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **UUID** | Unique record identifier | 
**hotel_identifier** | **UUID** | Hotel identifier. | 
**featured_ind** | **bool** | Indicates whether this inventory is featured. Use this flag as a way to signify that this inventory is special. | 
**lifestyle_type** | **str** | Indicate the type of lifestyle this blocking should be associated with. | [optional] 
**location** | [**GeoJsonPointNonAuthenticatedEntity**](GeoJsonPointNonAuthenticatedEntity.md) | Geo-location point where blocking takes place. Defaults to location of property. | 
**descriptions** | [**List[SimpleDescriptionNonAuthenticatedEntity]**](SimpleDescriptionNonAuthenticatedEntity.md) | Localized descriptions describing inventory. | 
**multimedias** | [**List[SimpleMultimediaNonAuthenticatedEntity]**](SimpleMultimediaNonAuthenticatedEntity.md) | List of images / videos of blocking. | 
**contact** | [**ContactNonAuthenticatedEntity**](ContactNonAuthenticatedEntity.md) | Associate a contact person for this blocking (if applicable). | 
**address** | [**SimpleAddressNonAuthenticatedEntity**](SimpleAddressNonAuthenticatedEntity.md) | Defaults to property address. | 
**commissionable** | **bool** | Indicate whether sales channels receive commission for selling this blocking. | [default to True]
**name** | **str** | Internal name of inventory. | 
**proximity_code** | **str** | Supported OTA specification &#x60;PRX&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | 
**sort** | **int** | Use this property to sort an blocking in a list of activities. | [optional] 
**min_age_appropriate_code** | **str** | Supported OTA specification &#x60;AQC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**bookable** | **bool** | Indicates if this blocking can be added to a booking or if it is read-only marketing material only. | [default to True]
**active** | **bool** | Modify blocking availability with this flag. | [default to True]
**disability_features** | **List[str]** | Supported OTA specification &#x60;PHY&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**security_features** | **List[str]** | Supported OTA specification &#x60;SEC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**socials** | [**List[SocialNonAuthenticatedEntity]**](SocialNonAuthenticatedEntity.md) | Social network accounts for blocking (if applicable). | [optional] 
**price_point** | **str** | Level of expensiveness. | [default to 'THREE']
**recognition_list** | [**List[TravelInventoryRecognitionNonAuthenticatedEntity]**](TravelInventoryRecognitionNonAuthenticatedEntity.md) | Inventory-level recognition. | [optional] 
**applicable_start** | **date** | Start month and day or date for which the attraction (e.g. the start of a season) is available. This date property signifies that the blocking is recurring and / or seasonal. If the date is in the past, only day and month will be used to infer seasonality. If the date is a future date, it will be interpreted as a starting date. | [optional] 
**applicable_end** | **date** | End month and day or date for which the attraction (e.g. the start of a season) is available. This date property signifies that the blocking is recurring and / or seasonal. If the date is in the past, only day and month will be used to infer seasonality. If the date is a future date, it will be interpreted as a ending date. | [optional] 
**reservation_required_ind** | **bool** | Indicates whether a reservation is required to participate in this blocking. | [optional] 
**opens** | **str** | Opening time of blocking (if applicable). Leave empty if blocking is always available. | [optional] 
**closes** | **str** | Closing time of blocking (if applicable). Leave empty if blocking is always available. | [optional] 
**days_of_week** | [**DowPatternGroupNonAuthenticatedEntity**](DowPatternGroupNonAuthenticatedEntity.md) | Indicate which days this blocking is open. | [optional] 
**attraction_category_code** | **str** | Supported OTA specification &#x60;ACC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | 
**courtesy_phone** | **bool** | Whether or not a courtesy phone for contacting the hotel is available at the attraction (e.g. often times these are available in airports). When true, the phone is available. | [optional] [default to False]

## Example

```python
from wink_sdk_inventory.models.attraction_lightweight_non_authenticated_entity import AttractionLightweightNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AttractionLightweightNonAuthenticatedEntity from a JSON string
attraction_lightweight_non_authenticated_entity_instance = AttractionLightweightNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(AttractionLightweightNonAuthenticatedEntity.to_json())

# convert the object into a dict
attraction_lightweight_non_authenticated_entity_dict = attraction_lightweight_non_authenticated_entity_instance.to_dict()
# create an instance of AttractionLightweightNonAuthenticatedEntity from a dict
attraction_lightweight_non_authenticated_entity_from_dict = AttractionLightweightNonAuthenticatedEntity.from_dict(attraction_lightweight_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


