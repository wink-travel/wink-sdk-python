# PropertyWithBestPriceNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel** | [**PropertyAggregateLightweightNonAuthenticatedEntity**](PropertyAggregateLightweightNonAuthenticatedEntity.md) | Property details | 
**lowest_price** | [**RoomTypeBestPriceNonAuthenticatedEntity**](RoomTypeBestPriceNonAuthenticatedEntity.md) | Best-priced room at property | 
**room_type_list** | [**List[GuestRoomLightweightNonAuthenticatedEntity]**](GuestRoomLightweightNonAuthenticatedEntity.md) | Unique property room types | 
**price_list** | [**List[RoomTypeBestPriceNonAuthenticatedEntity]**](RoomTypeBestPriceNonAuthenticatedEntity.md) | Best-priced room types | 
**potential_channel_discount_percent** | **float** | The potential discount the user is entitled to if user is a member / authenticated. | 
**source_to_user_currency_quote** | [**QuoteLightweightNonAuthenticatedEntity**](QuoteLightweightNonAuthenticatedEntity.md) | Exchange rate quote between the property&#39;s source currency and the user&#39;s desired currency that was used to populate price. | 
**source_to_internal_currency_quote** | [**QuoteLightweightNonAuthenticatedEntity**](QuoteLightweightNonAuthenticatedEntity.md) | Exchange rate quote between the property&#39;s source currency and the reactive&#39;s currency that was used to populate price. | 
**available** | **bool** | Flag to indicate whether this blocking is available or not. This data point is identifier to the available flag on the &#x60;price&#x60; child data point. | [optional] 

## Example

```python
from wink_sdk_inventory.models.property_with_best_price_non_authenticated_entity import PropertyWithBestPriceNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyWithBestPriceNonAuthenticatedEntity from a JSON string
property_with_best_price_non_authenticated_entity_instance = PropertyWithBestPriceNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(PropertyWithBestPriceNonAuthenticatedEntity.to_json())

# convert the object into a dict
property_with_best_price_non_authenticated_entity_dict = property_with_best_price_non_authenticated_entity_instance.to_dict()
# create an instance of PropertyWithBestPriceNonAuthenticatedEntity from a dict
property_with_best_price_non_authenticated_entity_from_dict = PropertyWithBestPriceNonAuthenticatedEntity.from_dict(property_with_best_price_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


