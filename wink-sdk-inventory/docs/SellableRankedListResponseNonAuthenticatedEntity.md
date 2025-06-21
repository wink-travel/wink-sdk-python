# SellableRankedListResponseNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | [**PageInventoryGridItemNonAuthenticatedEntity**](PageInventoryGridItemNonAuthenticatedEntity.md) | Property details along with the grid record. | [optional] 
**list** | [**SellableRankedListLightweightNonAuthenticatedEntity**](SellableRankedListLightweightNonAuthenticatedEntity.md) | Identifier blocking record | [optional] 

## Example

```python
from wink_sdk_inventory.models.sellable_ranked_list_response_non_authenticated_entity import SellableRankedListResponseNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SellableRankedListResponseNonAuthenticatedEntity from a JSON string
sellable_ranked_list_response_non_authenticated_entity_instance = SellableRankedListResponseNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SellableRankedListResponseNonAuthenticatedEntity.to_json())

# convert the object into a dict
sellable_ranked_list_response_non_authenticated_entity_dict = sellable_ranked_list_response_non_authenticated_entity_instance.to_dict()
# create an instance of SellableRankedListResponseNonAuthenticatedEntity from a dict
sellable_ranked_list_response_non_authenticated_entity_from_dict = SellableRankedListResponseNonAuthenticatedEntity.from_dict(sellable_ranked_list_response_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


