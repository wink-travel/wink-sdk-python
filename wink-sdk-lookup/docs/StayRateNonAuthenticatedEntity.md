# StayRateNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_specified_currency_base_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Base total in user specified currency. | [optional] 
**source_base_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Base total in hotel&#39;s currency. | [optional] 
**internal_base_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Base total in wink currency. | [optional] 
**source_extra_pax_modifier** | **float** | Extra person modifier in hotel currency. | [optional] 
**internal_extra_pax_modifier** | **float** | Extra person modifier in wink currency | [optional] 
**user_specified_currency_extra_pax_modifier** | **float** | Extra person modifier in user specified currency | [optional] 
**source_extra_child_modifier** | **float** | Extra child modifier in hotel currency | [optional] 
**internal_extra_child_modifier** | **float** | Extra child modifier in wink currency | [optional] 
**user_specified_currency_extra_child_modifier** | **float** | Extra child modifier in user specified currcency | [optional] 
**source_single_occupant_modifier** | **float** | Single occupant modifier in hotel currency | [optional] 
**internal_single_occupant_modifier** | **float** | Singe occupant modifier in wink currency | [optional] 
**user_specified_currency_single_occupant_modifier** | **float** | Single occupant modifier in user specified currency | [optional] 
**source_promotional_modifier** | **float** | Rate discount modifiers in hotel currency | [optional] 
**internal_promotional_modifier** | **float** | Rate discount modifiers in wink currency | [optional] 
**user_specified_currency_promotional_modifier** | **float** | Rate discount modifiers in user specified currency | [optional] 
**source_premium_modifier** | **float** | Rate premiums modifiers in hotel currency | [optional] 
**internal_premium_modifier** | **float** | Rate premiums modifiers in wink currency | [optional] 
**user_specified_currency_premium_modifier** | **float** | Rate premiums modifiers in user specified currency | [optional] 
**source_channel_modifier** | **float** | Channel / Membership modifier in hotel currency | [optional] 
**internal_channel_modifier** | **float** | Channel / Membership modifier in wink currency | [optional] 
**user_specified_currency_channel_modifier** | **float** | Channel / Membership modifier in user specified currency | [optional] 
**quantity** | **int** | Quantity | [optional] 
**min_occupancy** | **int** | Minimum occupancy | [optional] 
**max_occupancy** | **int** | Maximum occupancy | [optional] 
**rate_source** | **str** | Source | [optional] 
**promotional_discount_percent** | **float** | Promotional discount percent | [optional] 
**channel_discount_percent** | **float** | Chanel discount percent | [optional] 
**premium_percent** | **float** | Premium percent | [optional] 
**available** | **bool** | Available | [optional] 
**source_to_user_currency_quote** | [**QuoteLightweightNonAuthenticatedEntity**](QuoteLightweightNonAuthenticatedEntity.md) | Hotel to user currency exchange rate. | [optional] 
**source_to_internal_currency_quote** | [**QuoteLightweightNonAuthenticatedEntity**](QuoteLightweightNonAuthenticatedEntity.md) | Hotel to wink currency exchange rate. | [optional] 
**offer_details** | [**List[LocalizedDescriptionNonAuthenticatedEntity]**](LocalizedDescriptionNonAuthenticatedEntity.md) |  | [optional] 
**promotional_codes** | **List[str]** |  | [optional] 
**user_specified_currency_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | User-defined currency final price. | [optional] 
**source_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Source currency final price. | [optional] 
**internal_total** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) | Internal currency final price. | [optional] 
**user_specified_currency_average_price_per_night** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**internal_average_price_per_night** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**source_average_price_per_night** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 
**total_discount_percent** | **float** |  | [optional] 

## Example

```python
from wink_sdk_lookup.models.stay_rate_non_authenticated_entity import StayRateNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of StayRateNonAuthenticatedEntity from a JSON string
stay_rate_non_authenticated_entity_instance = StayRateNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(StayRateNonAuthenticatedEntity.to_json())

# convert the object into a dict
stay_rate_non_authenticated_entity_dict = stay_rate_non_authenticated_entity_instance.to_dict()
# create an instance of StayRateNonAuthenticatedEntity from a dict
stay_rate_non_authenticated_entity_from_dict = StayRateNonAuthenticatedEntity.from_dict(stay_rate_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


