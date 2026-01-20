# RoomTypeBestPriceForDateRangeNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room** | [**RoomTypeBestPriceForDateRangeInfoNonAuthenticatedEntity**](RoomTypeBestPriceForDateRangeInfoNonAuthenticatedEntity.md) | The room type. | 
**start_date** | **date** | SimpleDateTimeItinerary startDate | 
**end_date** | **date** | SimpleDateTimeItinerary endDate | 
**room_nights** | **int** | Number of nights the guests will be staying | 
**available** | **bool** | Utilify flag to verify whether this rate is available or not | 
**price** | [**RoomTypeBestPriceForDateRangePriceNonAuthenticatedEntity**](RoomTypeBestPriceForDateRangePriceNonAuthenticatedEntity.md) |  | [optional] 

## Example

```python
from wink_sdk_inventory.models.room_type_best_price_for_date_range_non_authenticated_entity import RoomTypeBestPriceForDateRangeNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of RoomTypeBestPriceForDateRangeNonAuthenticatedEntity from a JSON string
room_type_best_price_for_date_range_non_authenticated_entity_instance = RoomTypeBestPriceForDateRangeNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(RoomTypeBestPriceForDateRangeNonAuthenticatedEntity.to_json())

# convert the object into a dict
room_type_best_price_for_date_range_non_authenticated_entity_dict = room_type_best_price_for_date_range_non_authenticated_entity_instance.to_dict()
# create an instance of RoomTypeBestPriceForDateRangeNonAuthenticatedEntity from a dict
room_type_best_price_for_date_range_non_authenticated_entity_from_dict = RoomTypeBestPriceForDateRangeNonAuthenticatedEntity.from_dict(room_type_best_price_for_date_range_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


