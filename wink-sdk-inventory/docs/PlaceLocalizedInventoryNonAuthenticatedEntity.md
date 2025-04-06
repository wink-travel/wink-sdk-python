# PlaceLocalizedInventoryNonAuthenticatedEntity

List of property places on and off the premises.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**place** | [**PlaceLightweightNonAuthenticatedEntity**](PlaceLightweightNonAuthenticatedEntity.md) |  | [optional] 
**list** | [**List[LocalizedTransactionalTravelInventoryNonAuthenticatedEntity]**](LocalizedTransactionalTravelInventoryNonAuthenticatedEntity.md) |  | [optional] 
**channel_inventory_identifier** | **str** | Channel inventory identifier referencing this record. | [optional] 
**commissionable** | **bool** | Whether this package is commissionable based on the incoming sales channel. | [optional] 
**commission** | **float** | The commission percentage. | [optional] 
**direct** | **bool** | Indicates whether the blocking from sales channel is direct or not. If you are a travel agent doing your own acquiring, this flag has to be true to make a booking. | [default to False]
**price_list** | [**List[LocalizedTransactionalTravelInventoryNonAuthenticatedEntity]**](LocalizedTransactionalTravelInventoryNonAuthenticatedEntity.md) |  | [optional] 

## Example

```python
from wink_sdk_inventory.models.place_localized_inventory_non_authenticated_entity import PlaceLocalizedInventoryNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PlaceLocalizedInventoryNonAuthenticatedEntity from a JSON string
place_localized_inventory_non_authenticated_entity_instance = PlaceLocalizedInventoryNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(PlaceLocalizedInventoryNonAuthenticatedEntity.to_json())

# convert the object into a dict
place_localized_inventory_non_authenticated_entity_dict = place_localized_inventory_non_authenticated_entity_instance.to_dict()
# create an instance of PlaceLocalizedInventoryNonAuthenticatedEntity from a dict
place_localized_inventory_non_authenticated_entity_from_dict = PlaceLocalizedInventoryNonAuthenticatedEntity.from_dict(place_localized_inventory_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


