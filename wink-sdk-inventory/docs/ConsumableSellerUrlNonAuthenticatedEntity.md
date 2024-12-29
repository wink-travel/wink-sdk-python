# ConsumableSellerUrlNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | Which language the seller wanted to use | [optional] [default to 'en']
**currency** | **str** | Which currency the seller is using | [optional] [default to 'USD']
**title** | **str** | Link title | [optional] 
**description** | **str** | Link description | [optional] 
**keywords** | **str** | Comma-separated keyword values that can be used to populate HTML metadata | [optional] 
**unique_id** | **str** | The URL ID that uniquely represents this link | [optional] 
**twitter_account** | **str** | Optional X account ID | [optional] 
**facebook_app_id** | **str** | Optional Facebook app ID | [optional] 
**image** | [**SellerMediaNonAuthenticatedEntity**](SellerMediaNonAuthenticatedEntity.md) |  | [optional] 
**video** | [**SellerMediaNonAuthenticatedEntity**](SellerMediaNonAuthenticatedEntity.md) |  | [optional] 
**transact_url** | **str** | The transation url, or where to redirect to when clicking the CTA button. | [optional] 
**supplier_identifier** | **str** | The owner ID of the inventory you want to sell | [optional] 
**supplier_name** | **str** | The owner name of the inventory you want to sell | [optional] 
**supplier_url_name** | **str** | The owner url name of the inventory you want to sell | [optional] 
**supplier_brand** | **str** | In case the property is part of a brand | [optional] 
**available** | **bool** | Whether inventory is available for sale | [optional] 
**price** | [**SellerUrlPriceNonAuthenticatedEntity**](SellerUrlPriceNonAuthenticatedEntity.md) |  | [optional] 
**city_name** | **str** | City where inventory is located | [optional] 
**country_name** | **str** | Country where inventory is located | [optional] 
**inventory_type** | **str** | Type of inventory | [optional] 

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


