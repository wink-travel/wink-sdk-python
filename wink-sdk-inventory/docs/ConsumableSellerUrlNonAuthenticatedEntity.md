# ConsumableSellerUrlNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**keywords** | **str** |  | [optional] 
**unique_id** | **str** |  | [optional] 
**twitter_account** | **str** |  | [optional] 
**facebook_app_id** | **str** |  | [optional] 
**image** | [**SellerMediaNonAuthenticatedEntity**](SellerMediaNonAuthenticatedEntity.md) |  | [optional] 
**video** | [**SellerMediaNonAuthenticatedEntity**](SellerMediaNonAuthenticatedEntity.md) |  | [optional] 
**transact_url** | **str** |  | [optional] 
**supplier_identifier** | **str** |  | [optional] 
**supplier_name** | **str** |  | [optional] 
**supplier_url_name** | **str** |  | [optional] 
**supplier_brand** | **str** |  | [optional] 
**available** | **bool** |  | [optional] 
**price** | [**SellerUrlPriceNonAuthenticatedEntity**](SellerUrlPriceNonAuthenticatedEntity.md) |  | [optional] 
**city_name** | **str** |  | [optional] 
**country_name** | **str** |  | [optional] 
**inventory_type** | **str** |  | [optional] 

## Example

```python
from wink_sdk_inventory.models.consumable_seller_url_non_authenticated_entity import ConsumableSellerUrlNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumableSellerUrlNonAuthenticatedEntity from a JSON string
consumable_seller_url_non_authenticated_entity_instance = ConsumableSellerUrlNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ConsumableSellerUrlNonAuthenticatedEntity.to_json())

# convert the object into a dict
consumable_seller_url_non_authenticated_entity_dict = consumable_seller_url_non_authenticated_entity_instance.to_dict()
# create an instance of ConsumableSellerUrlNonAuthenticatedEntity from a dict
consumable_seller_url_non_authenticated_entity_from_dict = ConsumableSellerUrlNonAuthenticatedEntity.from_dict(consumable_seller_url_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


