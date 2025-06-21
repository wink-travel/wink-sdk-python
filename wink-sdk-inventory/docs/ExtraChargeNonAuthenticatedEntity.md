# ExtraChargeNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_plan_level_fee** | [**RatePlanLevelFeeNonAuthenticatedEntity**](RatePlanLevelFeeNonAuthenticatedEntity.md) | What the guest is paying extra for | [optional] 
**unit_price** | [**LocalizedPriceNonAuthenticatedEntity**](LocalizedPriceNonAuthenticatedEntity.md) | The localized unit price of the extra charge | [optional] 
**price** | [**LocalizedPriceNonAuthenticatedEntity**](LocalizedPriceNonAuthenticatedEntity.md) | The localized price of the extra charge | [optional] 

## Example

```python
from wink_sdk_inventory.models.extra_charge_non_authenticated_entity import ExtraChargeNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ExtraChargeNonAuthenticatedEntity from a JSON string
extra_charge_non_authenticated_entity_instance = ExtraChargeNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ExtraChargeNonAuthenticatedEntity.to_json())

# convert the object into a dict
extra_charge_non_authenticated_entity_dict = extra_charge_non_authenticated_entity_instance.to_dict()
# create an instance of ExtraChargeNonAuthenticatedEntity from a dict
extra_charge_non_authenticated_entity_from_dict = ExtraChargeNonAuthenticatedEntity.from_dict(extra_charge_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


