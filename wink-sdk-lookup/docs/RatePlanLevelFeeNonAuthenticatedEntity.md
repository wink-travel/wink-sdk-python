# RatePlanLevelFeeNonAuthenticatedEntity

What the guest is paying extra for

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descriptions** | [**List[LocalizedDescriptionNonAuthenticatedEntity]**](LocalizedDescriptionNonAuthenticatedEntity.md) | List of localized descriptions for this fee. | 
**fixed_amount** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | 
**type** | **str** | Rate plan fee type | 

## Example

```python
from wink_sdk_lookup.models.rate_plan_level_fee_non_authenticated_entity import RatePlanLevelFeeNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlanLevelFeeNonAuthenticatedEntity from a JSON string
rate_plan_level_fee_non_authenticated_entity_instance = RatePlanLevelFeeNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(RatePlanLevelFeeNonAuthenticatedEntity.to_json())

# convert the object into a dict
rate_plan_level_fee_non_authenticated_entity_dict = rate_plan_level_fee_non_authenticated_entity_instance.to_dict()
# create an instance of RatePlanLevelFeeNonAuthenticatedEntity from a dict
rate_plan_level_fee_non_authenticated_entity_from_dict = RatePlanLevelFeeNonAuthenticatedEntity.from_dict(rate_plan_level_fee_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


