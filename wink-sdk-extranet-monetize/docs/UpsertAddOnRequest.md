# UpsertAddOnRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**featured_ind** | **bool** | Indicates whether this inventory is featured. Use this flag as a way to signify that this inventory is special. | 
**lifestyle_type** | **str** | Indicate the type of lifestyle this blocking should be associated with. | [optional] 
**location** | [**GeoJsonPoint**](GeoJsonPoint.md) | Geo-location point where blocking takes place. Defaults to location of property. | 
**descriptions** | [**List[UpsertSimpleDescription]**](UpsertSimpleDescription.md) |  | 
**multimedias** | [**List[SimpleMultimedia]**](SimpleMultimedia.md) |  | 
**contact** | [**Contact**](Contact.md) | Associate a contact person for this blocking (if applicable). | [optional] 
**address** | [**UpsertAddressRequest**](UpsertAddressRequest.md) | Defaults to property address. | 
**commissionable** | **bool** | Indicate whether sales channels receive commission for selling this blocking. | [default to True]
**name** | **str** | Internal name of blocking. | 
**proximity_code** | **str** | Supported OTA specification &#x60;PRX&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**sort** | **int** | Use this property to sort an blocking in a list of activities. | [optional] 
**min_age_appropriate_code** | **str** | Supported OTA specification &#x60;AQC&#x60; code. See [OTA geoname data](#operation/showAvailableCodesForCategory) | [optional] 
**bookable** | **bool** | Indicates if this blocking can be added to a booking or if it is read-only marketing material only. | [default to True]
**active** | **bool** | Modify blocking availability with this flag. | [default to True]
**disability_features** | **List[str]** |  | [optional] 
**security_features** | **List[str]** |  | [optional] 
**socials** | [**List[Social]**](Social.md) |  | [optional] 
**price_point** | **str** | Level of expensiveness. | [default to 'THREE']
**recognition_list** | [**List[TravelInventoryRecognition]**](TravelInventoryRecognition.md) |  | [optional] 
**transaction_inventory_list** | [**List[TransactionalTravelInventory]**](TransactionalTravelInventory.md) |  | [optional] 
**applicable_start** | **date** | Start month and day or date for which the attraction (e.g. the start of a season) is available. This date property signifies that the blocking is recurring and / or seasonal. If the date is in the past, only day and month will be used to infer seasonality. If the date is a future date, it will be interpreted as a starting date. | [optional] 
**applicable_end** | **date** | End month and day or date for which the attraction (e.g. the start of a season) is available. This date property signifies that the blocking is recurring and / or seasonal. If the date is in the past, only day and month will be used to infer seasonality. If the date is a future date, it will be interpreted as a ending date. | [optional] 
**reservation_required_ind** | **bool** | Indicates whether a reservation is required to participate in this blocking. | [optional] 
**opens** | **str** | Opening time of blocking (if applicable). Leave empty if blocking is always available. | [optional] 
**closes** | **str** | Closing time of blocking (if applicable). Leave empty if blocking is always available. | [optional] 
**days_of_week** | [**DowPatternGroup**](DowPatternGroup.md) | Indicate which days this blocking is open. | [optional] 
**number_of_units** | **int** | Total number of add-ons available to purchase. | [default to 0]
**rate_plan_identifier** | **str** | Pass an optional rate plan identifier if you want to add more complex restrictions to this add-on. Example: You want the add-on to only be available when a specific room is available. | [optional] 
**mandatory** | **bool** | Make this add-on mandatory for all guests by enabling this flag. | [default to False]
**transactional_inventory_list** | [**List[TransactionalTravelInventory]**](TransactionalTravelInventory.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_monetize.models.upsert_add_on_request import UpsertAddOnRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertAddOnRequest from a JSON string
upsert_add_on_request_instance = UpsertAddOnRequest.from_json(json)
# print the JSON string representation of the object
print(UpsertAddOnRequest.to_json())

# convert the object into a dict
upsert_add_on_request_dict = upsert_add_on_request_instance.to_dict()
# create an instance of UpsertAddOnRequest from a dict
upsert_add_on_request_from_dict = UpsertAddOnRequest.from_dict(upsert_add_on_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


