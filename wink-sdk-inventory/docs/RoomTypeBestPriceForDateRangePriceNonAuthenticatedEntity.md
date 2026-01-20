# RoomTypeBestPriceForDateRangePriceNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_specified_currency_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Total amount with any extra charges included | [optional] 
**source_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Source total amount with any extra charges included | [optional] 

## Example

```python
from wink_sdk_inventory.models.room_type_best_price_for_date_range_price_non_authenticated_entity import RoomTypeBestPriceForDateRangePriceNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of RoomTypeBestPriceForDateRangePriceNonAuthenticatedEntity from a JSON string
room_type_best_price_for_date_range_price_non_authenticated_entity_instance = RoomTypeBestPriceForDateRangePriceNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(RoomTypeBestPriceForDateRangePriceNonAuthenticatedEntity.to_json())

# convert the object into a dict
room_type_best_price_for_date_range_price_non_authenticated_entity_dict = room_type_best_price_for_date_range_price_non_authenticated_entity_instance.to_dict()
# create an instance of RoomTypeBestPriceForDateRangePriceNonAuthenticatedEntity from a dict
room_type_best_price_for_date_range_price_non_authenticated_entity_from_dict = RoomTypeBestPriceForDateRangePriceNonAuthenticatedEntity.from_dict(room_type_best_price_for_date_range_price_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


