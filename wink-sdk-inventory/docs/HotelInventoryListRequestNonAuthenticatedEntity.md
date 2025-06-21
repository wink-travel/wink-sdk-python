# HotelInventoryListRequestNonAuthenticatedEntity

Wrapper to query for multiple property inventories

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | **List[object]** |  | 

## Example

```python
from wink_sdk_inventory.models.hotel_inventory_list_request_non_authenticated_entity import HotelInventoryListRequestNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of HotelInventoryListRequestNonAuthenticatedEntity from a JSON string
hotel_inventory_list_request_non_authenticated_entity_instance = HotelInventoryListRequestNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(HotelInventoryListRequestNonAuthenticatedEntity.to_json())

# convert the object into a dict
hotel_inventory_list_request_non_authenticated_entity_dict = hotel_inventory_list_request_non_authenticated_entity_instance.to_dict()
# create an instance of HotelInventoryListRequestNonAuthenticatedEntity from a dict
hotel_inventory_list_request_non_authenticated_entity_from_dict = HotelInventoryListRequestNonAuthenticatedEntity.from_dict(hotel_inventory_list_request_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


