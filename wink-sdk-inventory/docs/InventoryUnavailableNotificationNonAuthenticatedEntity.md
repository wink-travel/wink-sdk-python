# InventoryUnavailableNotificationNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_identifier** | **str** |  | 
**property_name** | **str** |  | 
**inventory_name** | **str** |  | 
**inventory_type** | **str** |  | 
**inventory_identifier** | **str** |  | 
**user_session** | [**UserSessionNonAuthenticatedEntity**](UserSessionNonAuthenticatedEntity.md) |  | 

## Example

```python
from wink_sdk_inventory.models.inventory_unavailable_notification_non_authenticated_entity import InventoryUnavailableNotificationNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUnavailableNotificationNonAuthenticatedEntity from a JSON string
inventory_unavailable_notification_non_authenticated_entity_instance = InventoryUnavailableNotificationNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(InventoryUnavailableNotificationNonAuthenticatedEntity.to_json())

# convert the object into a dict
inventory_unavailable_notification_non_authenticated_entity_dict = inventory_unavailable_notification_non_authenticated_entity_instance.to_dict()
# create an instance of InventoryUnavailableNotificationNonAuthenticatedEntity from a dict
inventory_unavailable_notification_non_authenticated_entity_from_dict = InventoryUnavailableNotificationNonAuthenticatedEntity.from_dict(inventory_unavailable_notification_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


