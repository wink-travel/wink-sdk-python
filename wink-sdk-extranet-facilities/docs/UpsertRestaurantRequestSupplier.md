# UpsertRestaurantRequestSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**featured_ind** | **bool** | Indicates whether this inventory is featured. Use this flag as a way to signify that this inventory is special. | 
**lifestyle_type** | **str** | Indicate the type of lifestyle this blocking should be associated with. | [optional] 
**location** | [**GeoJsonPointSupplier**](GeoJsonPointSupplier.md) | Geo-location point where blocking takes place. Defaults to location of property. | 
**descriptions** | [**List[UpsertSimpleDescriptionSupplier]**](UpsertSimpleDescriptionSupplier.md) |  | 
**multimedias** | [**List[SimpleMultimediaSupplier]**](SimpleMultimediaSupplier.md) |  | 
**contact** | [**ContactSupplier**](ContactSupplier.md) | Associate a contact person for this blocking (if applicable). | [optional] 
**address** | [**UpsertAddressRequestSupplier**](UpsertAddressRequestSupplier.md) | Defaults to property address. | 
**commissionable** | **bool** | Indicate whether sales channels receive commission for selling this blocking. | [default to True]
**name** | **str** | Internal name of blocking. | 
**proximity_code** | **str** | Supported OTA specification &#x60;PRX&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**sort** | **int** | Use this property to sort an blocking in a list of activities. | [optional] 
**min_age_appropriate_code** | **str** | Supported OTA specification &#x60;AQC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**bookable** | **bool** | Indicates if this blocking can be added to a booking or if it is read-only marketing material only. | [default to True]
**active** | **bool** | Modify blocking availability with this flag. | [default to True]
**disability_features** | **List[str]** |  | [optional] 
**security_features** | **List[str]** |  | [optional] 
**socials** | [**List[SocialSupplier]**](SocialSupplier.md) |  | [optional] 
**price_point** | **str** | Level of expensiveness. | [default to 'THREE']
**recognition_list** | [**List[TravelInventoryRecognitionSupplier]**](TravelInventoryRecognitionSupplier.md) |  | [optional] 
**transaction_inventory_list** | [**List[TransactionalTravelInventorySupplier]**](TransactionalTravelInventorySupplier.md) |  | [optional] 
**applicable_start** | **date** | Start month and day or date for which the attraction (e.g. the start of a season) is available. This date property signifies that the blocking is recurring and / or seasonal. If the date is in the past, only day and month will be used to infer seasonality. If the date is a future date, it will be interpreted as a starting date. | [optional] 
**applicable_end** | **date** | End month and day or date for which the attraction (e.g. the start of a season) is available. This date property signifies that the blocking is recurring and / or seasonal. If the date is in the past, only day and month will be used to infer seasonality. If the date is a future date, it will be interpreted as a ending date. | [optional] 
**reservation_required_ind** | **bool** | Indicates whether a reservation is required to participate in this blocking. | [optional] 
**opens** | **str** | Opening time of blocking (if applicable). Leave empty if blocking is always available. | [optional] 
**closes** | **str** | Closing time of blocking (if applicable). Leave empty if blocking is always available. | [optional] 
**days_of_week** | [**DowPatternGroupSupplier**](DowPatternGroupSupplier.md) | Indicate which days this blocking is open. | [optional] 
**max_seating_capacity** | **int** | Restaurant supports these many people. | 
**max_single_party** | **int** | Largest table at restaurant. | 
**offer_breakfast** | **bool** | Restaurant offers breakfast. | [default to False]
**offer_brunch** | **bool** | Restaurant offers brunch. | [default to False]
**offer_lunch** | **bool** | Restaurant offers lunch. | [default to False]
**offer_dinner** | **bool** | Restaurant offers dinner. | [default to False]
**amenities** | **List[str]** |  | [optional] 
**info_codes** | **List[str]** |  | [optional] 
**cuisine_codes** | **List[str]** |  | [optional] 
**transactional_inventory_list** | [**List[TransactionalTravelInventorySupplier]**](TransactionalTravelInventorySupplier.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_facilities.models.upsert_restaurant_request_supplier import UpsertRestaurantRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertRestaurantRequestSupplier from a JSON string
upsert_restaurant_request_supplier_instance = UpsertRestaurantRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(UpsertRestaurantRequestSupplier.to_json())

# convert the object into a dict
upsert_restaurant_request_supplier_dict = upsert_restaurant_request_supplier_instance.to_dict()
# create an instance of UpsertRestaurantRequestSupplier from a dict
upsert_restaurant_request_supplier_from_dict = UpsertRestaurantRequestSupplier.from_dict(upsert_restaurant_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


