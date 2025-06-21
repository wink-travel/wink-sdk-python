# SellableListResponseNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**PageInventoryGridItemNonAuthenticatedEntity**](PageInventoryGridItemNonAuthenticatedEntity.md) | Property details along with the grid record. | [optional] 
**list** | [**SellableListLightweightNonAuthenticatedEntity**](SellableListLightweightNonAuthenticatedEntity.md) | Identifier blocking record | [optional] 

## Example

```python
from wink_sdk_inventory.models.sellable_list_response_non_authenticated_entity import SellableListResponseNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SellableListResponseNonAuthenticatedEntity from a JSON string
sellable_list_response_non_authenticated_entity_instance = SellableListResponseNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SellableListResponseNonAuthenticatedEntity.to_json())

# convert the object into a dict
sellable_list_response_non_authenticated_entity_dict = sellable_list_response_non_authenticated_entity_instance.to_dict()
# create an instance of SellableListResponseNonAuthenticatedEntity from a dict
sellable_list_response_non_authenticated_entity_from_dict = SellableListResponseNonAuthenticatedEntity.from_dict(sellable_list_response_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


