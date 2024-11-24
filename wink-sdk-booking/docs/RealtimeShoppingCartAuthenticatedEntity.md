# RealtimeShoppingCartAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Shopping cart ID | 
**item_list** | [**List[RealtimeShoppingCartItemAuthenticatedEntity]**](RealtimeShoppingCartItemAuthenticatedEntity.md) | List of priced shopping cart items. Each entry is a separately booked room. | [optional] 
**user_specified_currency_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**internal_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**source_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 

## Example

```python
from wink_sdk_booking.models.realtime_shopping_cart_authenticated_entity import RealtimeShoppingCartAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of RealtimeShoppingCartAuthenticatedEntity from a JSON string
realtime_shopping_cart_authenticated_entity_instance = RealtimeShoppingCartAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(RealtimeShoppingCartAuthenticatedEntity.to_json())

# convert the object into a dict
realtime_shopping_cart_authenticated_entity_dict = realtime_shopping_cart_authenticated_entity_instance.to_dict()
# create an instance of RealtimeShoppingCartAuthenticatedEntity from a dict
realtime_shopping_cart_authenticated_entity_from_dict = RealtimeShoppingCartAuthenticatedEntity.from_dict(realtime_shopping_cart_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


