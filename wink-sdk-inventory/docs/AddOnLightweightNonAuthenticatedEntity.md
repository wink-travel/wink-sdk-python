# AddOnLightweightNonAuthenticatedEntity

The original add-on record created by the property.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique record identifier | 
**hotel_identifier** | **str** | Hotel identifier. | 
**featured_ind** | **bool** | Indicates whether this inventory is featured. Use this flag as a way to signify that this inventory is special. | 
**lifestyle_type** | **str** | Indicate the type of lifestyle this blocking should be associated with. | [optional] 
**location** | [**GeoJsonPointNonAuthenticatedEntity**](GeoJsonPointNonAuthenticatedEntity.md) |  | 
**descriptions** | [**List[SimpleDescriptionNonAuthenticatedEntity]**](SimpleDescriptionNonAuthenticatedEntity.md) | Localized descriptions describing blocking. | 
**multimedias** | [**List[SimpleMultimediaNonAuthenticatedEntity]**](SimpleMultimediaNonAuthenticatedEntity.md) | List of images / videos of blocking. | 
**contact** | [**ContactNonAuthenticatedEntity**](ContactNonAuthenticatedEntity.md) |  | 
**address** | [**SimpleAddressNonAuthenticatedEntity**](SimpleAddressNonAuthenticatedEntity.md) |  | 
**commissionable** | **bool** | Indicate whether sales channels receive commission for selling this blocking. | [default to True]
**name** | **str** | Internal name of blocking. | 
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
**days_of_week** | [**DowPatternGroupNonAuthenticatedEntity**](DowPatternGroupNonAuthenticatedEntity.md) |  | [optional] 
**number_of_units** | **int** | Total number of add-ons available to purchase. | [default to 0]
**mandatory** | **bool** | Make this add-on mandatory for all guests by enabling this flag. | [default to False]
**rate_plan_identifier** | **str** | Optional restriction on rate plan. | [optional] 

## Example

```python
from wink_sdk_inventory.models.add_on_lightweight_non_authenticated_entity import AddOnLightweightNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AddOnLightweightNonAuthenticatedEntity from a JSON string
add_on_lightweight_non_authenticated_entity_instance = AddOnLightweightNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(AddOnLightweightNonAuthenticatedEntity.to_json())

# convert the object into a dict
add_on_lightweight_non_authenticated_entity_dict = add_on_lightweight_non_authenticated_entity_instance.to_dict()
# create an instance of AddOnLightweightNonAuthenticatedEntity from a dict
add_on_lightweight_non_authenticated_entity_from_dict = AddOnLightweightNonAuthenticatedEntity.from_dict(add_on_lightweight_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


