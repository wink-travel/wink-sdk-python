# AggregateSellerInventoryListRequestNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Record identifier | 
**engine_configuration_identifier** | **str** | The configuration identifier that was used during this call. | [optional] 
**user_session** | [**UserSessionNonAuthenticatedEntity**](UserSessionNonAuthenticatedEntity.md) |  | 
**page** | **int** | Which to page to paginate to | 
**size** | **int** | How many results to return per page | 

## Example

```python
from wink_sdk_inventory.models.aggregate_seller_inventory_list_request_non_authenticated_entity import AggregateSellerInventoryListRequestNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateSellerInventoryListRequestNonAuthenticatedEntity from a JSON string
aggregate_seller_inventory_list_request_non_authenticated_entity_instance = AggregateSellerInventoryListRequestNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(AggregateSellerInventoryListRequestNonAuthenticatedEntity.to_json())

# convert the object into a dict
aggregate_seller_inventory_list_request_non_authenticated_entity_dict = aggregate_seller_inventory_list_request_non_authenticated_entity_instance.to_dict()
# create an instance of AggregateSellerInventoryListRequestNonAuthenticatedEntity from a dict
aggregate_seller_inventory_list_request_non_authenticated_entity_from_dict = AggregateSellerInventoryListRequestNonAuthenticatedEntity.from_dict(aggregate_seller_inventory_list_request_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


