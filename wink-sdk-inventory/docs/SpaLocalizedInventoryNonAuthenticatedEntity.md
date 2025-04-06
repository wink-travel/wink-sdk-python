# SpaLocalizedInventoryNonAuthenticatedEntity

List of property spas on and off the premises.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spa** | [**SpaLightweightNonAuthenticatedEntity**](SpaLightweightNonAuthenticatedEntity.md) |  | [optional] 
**list** | [**List[LocalizedTransactionalTravelInventoryNonAuthenticatedEntity]**](LocalizedTransactionalTravelInventoryNonAuthenticatedEntity.md) |  | [optional] 
**channel_inventory_identifier** | **str** | Channel inventory identifier referencing this record. | [optional] 
**commissionable** | **bool** | Whether this package is commissionable based on the incoming sales channel. | [optional] 
**commission** | **float** | The commission percentage. | [optional] 
**direct** | **bool** | Indicates whether the blocking from sales channel is direct or not. If you are a travel agent doing your own acquiring, this flag has to be true to make a booking. | [default to False]
**price_list** | [**List[LocalizedTransactionalTravelInventoryNonAuthenticatedEntity]**](LocalizedTransactionalTravelInventoryNonAuthenticatedEntity.md) |  | [optional] 

## Example

```python
from wink_sdk_inventory.models.spa_localized_inventory_non_authenticated_entity import SpaLocalizedInventoryNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SpaLocalizedInventoryNonAuthenticatedEntity from a JSON string
spa_localized_inventory_non_authenticated_entity_instance = SpaLocalizedInventoryNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SpaLocalizedInventoryNonAuthenticatedEntity.to_json())

# convert the object into a dict
spa_localized_inventory_non_authenticated_entity_dict = spa_localized_inventory_non_authenticated_entity_instance.to_dict()
# create an instance of SpaLocalizedInventoryNonAuthenticatedEntity from a dict
spa_localized_inventory_non_authenticated_entity_from_dict = SpaLocalizedInventoryNonAuthenticatedEntity.from_dict(spa_localized_inventory_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


