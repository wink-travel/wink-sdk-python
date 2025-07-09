# LocalizedPriceNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_to_user_currency_quote** | [**QuoteLightweightNonAuthenticatedEntity**](QuoteLightweightNonAuthenticatedEntity.md) | Hotel to user currency exchange rate. | 
**source_to_internal_currency_quote** | [**QuoteLightweightNonAuthenticatedEntity**](QuoteLightweightNonAuthenticatedEntity.md) | Hotel to wink currency exchange rate. | 
**user_specified_currency_base_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Base total in user specified currency. | 
**source_base_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Base total in hotel currency. | 
**internal_base_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Base total in wink currency. | 
**user_specified_currency_promotional_modifier** | **float** | Promotional modifiers in user specified currency | [optional] 
**source_promotional_modifier** | **float** | Promotional modifiers in hotel currency | [optional] 
**internal_promotional_modifier** | **float** | Promotional modifiers in wink currency | [optional] 
**user_specified_currency_premium_modifier** | **float** | Premium modifiers in user specified currency | [optional] 
**source_premium_modifier** | **float** | Premium modifiers in hotel currency | [optional] 
**internal_premium_modifier** | **float** | Premium modifiers in wink currency | [optional] 
**user_specified_currency_channel_modifier** | **float** | Channel / Membership modifier in user specified currency | [optional] 
**source_channel_modifier** | **float** | Channel / Membership modifier in hotel currency | [optional] 
**internal_channel_modifier** | **float** | Channel / Membership modifier in wink currency | [optional] 
**quantity** | **int** | How many of this item is included in this price | [optional] [default to 1]
**promotional_discount_percent** | **float** | Promotional discount percent | [optional] 
**channel_discount_percent** | **float** | Channel discount percent | [optional] 
**premium_percent** | **float** | Premium percent | [optional] 
**total_discount_percent** | **float** |  | [optional] 
**source_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**user_specified_currency_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**internal_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**has_channel_discount** | **bool** |  | [optional] 
**has_premium** | **bool** |  | [optional] 
**has_promotion** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_lookup.models.localized_price_non_authenticated_entity import LocalizedPriceNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of LocalizedPriceNonAuthenticatedEntity from a JSON string
localized_price_non_authenticated_entity_instance = LocalizedPriceNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(LocalizedPriceNonAuthenticatedEntity.to_json())

# convert the object into a dict
localized_price_non_authenticated_entity_dict = localized_price_non_authenticated_entity_instance.to_dict()
# create an instance of LocalizedPriceNonAuthenticatedEntity from a dict
localized_price_non_authenticated_entity_from_dict = LocalizedPriceNonAuthenticatedEntity.from_dict(localized_price_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


