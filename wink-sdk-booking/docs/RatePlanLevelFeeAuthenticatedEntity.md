# RatePlanLevelFeeAuthenticatedEntity

What the guest is paying extra for

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descriptions** | [**List[LocalizedDescriptionAuthenticatedEntity]**](LocalizedDescriptionAuthenticatedEntity.md) | List of localized descriptions for this fee. | 
**fixed_amount** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | 
**type** | **str** | Rate plan fee type | 

## Example

```python
from wink_sdk_booking.models.rate_plan_level_fee_authenticated_entity import RatePlanLevelFeeAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlanLevelFeeAuthenticatedEntity from a JSON string
rate_plan_level_fee_authenticated_entity_instance = RatePlanLevelFeeAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(RatePlanLevelFeeAuthenticatedEntity.to_json())

# convert the object into a dict
rate_plan_level_fee_authenticated_entity_dict = rate_plan_level_fee_authenticated_entity_instance.to_dict()
# create an instance of RatePlanLevelFeeAuthenticatedEntity from a dict
rate_plan_level_fee_authenticated_entity_from_dict = RatePlanLevelFeeAuthenticatedEntity.from_dict(rate_plan_level_fee_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


