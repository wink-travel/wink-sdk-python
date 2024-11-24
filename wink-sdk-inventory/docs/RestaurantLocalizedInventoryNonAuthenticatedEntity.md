# RestaurantLocalizedInventoryNonAuthenticatedEntity

List of property restaurants on and off the premises.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**restaurant** | [**RestaurantNonAuthenticatedEntity**](RestaurantNonAuthenticatedEntity.md) |  | [optional] 
**list** | [**List[LocalizedTransactionalTravelInventoryNonAuthenticatedEntity]**](LocalizedTransactionalTravelInventoryNonAuthenticatedEntity.md) |  | [optional] 
**channel_inventory_identifier** | **str** | Channel blocking identifier referencing this record. | [optional] 
**commissionable** | **bool** | Whether this package is commissionable based on the incoming sales channel. | [optional] 
**commission** | **float** | The commission percentage. | [optional] 
**direct** | **bool** | Indicates whether the blocking from sales channel is direct or not. If you are a travel agent doing your own acquiring, this flag has to be true to make a booking. | [default to False]
**price_list** | [**List[LocalizedTransactionalTravelInventoryNonAuthenticatedEntity]**](LocalizedTransactionalTravelInventoryNonAuthenticatedEntity.md) |  | [optional] 

## Example

```python
from wink_sdk_inventory.models.restaurant_localized_inventory_non_authenticated_entity import RestaurantLocalizedInventoryNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantLocalizedInventoryNonAuthenticatedEntity from a JSON string
restaurant_localized_inventory_non_authenticated_entity_instance = RestaurantLocalizedInventoryNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(RestaurantLocalizedInventoryNonAuthenticatedEntity.to_json())

# convert the object into a dict
restaurant_localized_inventory_non_authenticated_entity_dict = restaurant_localized_inventory_non_authenticated_entity_instance.to_dict()
# create an instance of RestaurantLocalizedInventoryNonAuthenticatedEntity from a dict
restaurant_localized_inventory_non_authenticated_entity_from_dict = RestaurantLocalizedInventoryNonAuthenticatedEntity.from_dict(restaurant_localized_inventory_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


