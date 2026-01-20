# RoomTypeBestPriceForDateRangeInfoNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **UUID** | Unique record identifier | 
**name** | **str** | Internal name of inventory. | 
**max_occupancy** | **int** | Maximum number of guest allowed in a room type. | [default to 2]

## Example

```python
from wink_sdk_inventory.models.room_type_best_price_for_date_range_info_non_authenticated_entity import RoomTypeBestPriceForDateRangeInfoNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of RoomTypeBestPriceForDateRangeInfoNonAuthenticatedEntity from a JSON string
room_type_best_price_for_date_range_info_non_authenticated_entity_instance = RoomTypeBestPriceForDateRangeInfoNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(RoomTypeBestPriceForDateRangeInfoNonAuthenticatedEntity.to_json())

# convert the object into a dict
room_type_best_price_for_date_range_info_non_authenticated_entity_dict = room_type_best_price_for_date_range_info_non_authenticated_entity_instance.to_dict()
# create an instance of RoomTypeBestPriceForDateRangeInfoNonAuthenticatedEntity from a dict
room_type_best_price_for_date_range_info_non_authenticated_entity_from_dict = RoomTypeBestPriceForDateRangeInfoNonAuthenticatedEntity.from_dict(room_type_best_price_for_date_range_info_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


