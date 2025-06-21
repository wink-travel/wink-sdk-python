# ConsumerDataMapNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**map** | [**InventoryMapLightweightNonAuthenticatedEntity**](InventoryMapLightweightNonAuthenticatedEntity.md) |  | 
**markers** | [**List[InventoryMapMarkerNonAuthenticatedEntity]**](InventoryMapMarkerNonAuthenticatedEntity.md) |  | 

## Example

```python
from wink_sdk_inventory.models.consumer_data_map_non_authenticated_entity import ConsumerDataMapNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumerDataMapNonAuthenticatedEntity from a JSON string
consumer_data_map_non_authenticated_entity_instance = ConsumerDataMapNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ConsumerDataMapNonAuthenticatedEntity.to_json())

# convert the object into a dict
consumer_data_map_non_authenticated_entity_dict = consumer_data_map_non_authenticated_entity_instance.to_dict()
# create an instance of ConsumerDataMapNonAuthenticatedEntity from a dict
consumer_data_map_non_authenticated_entity_from_dict = ConsumerDataMapNonAuthenticatedEntity.from_dict(consumer_data_map_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


