# AddOnLocalizedInventoryNonAuthenticatedEntity

Add-ons that are available with this room configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_on** | [**AddOnNonAuthenticatedEntity**](AddOnNonAuthenticatedEntity.md) |  | 
**price_list** | [**List[LocalizedTransactionalTravelInventoryNonAuthenticatedEntity]**](LocalizedTransactionalTravelInventoryNonAuthenticatedEntity.md) |  | [optional] 
**channel_inventory_identifier** | **str** | Channel blocking identifier referencing this record. | [optional] 
**commissionable** | **bool** | Whether this package is commissionable based on the incoming sales channel. | [optional] 
**commission** | **float** | The commission percentage. | [optional] 
**direct** | **bool** | Indicates whether the blocking from sales channel is direct or not. If you are a travel agent doing your own acquiring, this flag has to be true to make a booking. | [default to False]

## Example

```python
from wink_sdk_lookup.models.add_on_localized_inventory_non_authenticated_entity import AddOnLocalizedInventoryNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AddOnLocalizedInventoryNonAuthenticatedEntity from a JSON string
add_on_localized_inventory_non_authenticated_entity_instance = AddOnLocalizedInventoryNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(AddOnLocalizedInventoryNonAuthenticatedEntity.to_json())

# convert the object into a dict
add_on_localized_inventory_non_authenticated_entity_dict = add_on_localized_inventory_non_authenticated_entity_instance.to_dict()
# create an instance of AddOnLocalizedInventoryNonAuthenticatedEntity from a dict
add_on_localized_inventory_non_authenticated_entity_from_dict = AddOnLocalizedInventoryNonAuthenticatedEntity.from_dict(add_on_localized_inventory_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


