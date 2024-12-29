# SellerUrlPriceNonAuthenticatedEntity

The price of the link being exposed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**price** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**percent_discount** | **float** | Price discount in percent | [optional] 

## Example

```python
from wink_sdk_inventory.models.seller_url_price_non_authenticated_entity import SellerUrlPriceNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SellerUrlPriceNonAuthenticatedEntity from a JSON string
seller_url_price_non_authenticated_entity_instance = SellerUrlPriceNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SellerUrlPriceNonAuthenticatedEntity.to_json())

# convert the object into a dict
seller_url_price_non_authenticated_entity_dict = seller_url_price_non_authenticated_entity_instance.to_dict()
# create an instance of SellerUrlPriceNonAuthenticatedEntity from a dict
seller_url_price_non_authenticated_entity_from_dict = SellerUrlPriceNonAuthenticatedEntity.from_dict(seller_url_price_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


