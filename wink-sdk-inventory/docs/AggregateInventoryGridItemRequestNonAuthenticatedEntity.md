# AggregateInventoryGridItemRequestNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **UUID** | Record identifier | 
**user_session** | [**UserSessionNonAuthenticatedEntity**](UserSessionNonAuthenticatedEntity.md) | User session containing itinerary and other data by the user | 
**customization_identifier** | **UUID** | The configuration identifier that was used during this call. | [optional] 
**locale** | **str** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from wink_sdk_inventory.models.aggregate_inventory_grid_item_request_non_authenticated_entity import AggregateInventoryGridItemRequestNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateInventoryGridItemRequestNonAuthenticatedEntity from a JSON string
aggregate_inventory_grid_item_request_non_authenticated_entity_instance = AggregateInventoryGridItemRequestNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(AggregateInventoryGridItemRequestNonAuthenticatedEntity.to_json())

# convert the object into a dict
aggregate_inventory_grid_item_request_non_authenticated_entity_dict = aggregate_inventory_grid_item_request_non_authenticated_entity_instance.to_dict()
# create an instance of AggregateInventoryGridItemRequestNonAuthenticatedEntity from a dict
aggregate_inventory_grid_item_request_non_authenticated_entity_from_dict = AggregateInventoryGridItemRequestNonAuthenticatedEntity.from_dict(aggregate_inventory_grid_item_request_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


