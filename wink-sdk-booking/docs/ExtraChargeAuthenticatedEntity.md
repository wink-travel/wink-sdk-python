# ExtraChargeAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_plan_level_fee** | [**RatePlanLevelFeeAuthenticatedEntity**](RatePlanLevelFeeAuthenticatedEntity.md) | What the guest is paying extra for | [optional] 
**unit_price** | [**LocalizedPriceAuthenticatedEntity**](LocalizedPriceAuthenticatedEntity.md) | The localized unit price of the extra charge | [optional] 
**price** | [**LocalizedPriceAuthenticatedEntity**](LocalizedPriceAuthenticatedEntity.md) | The localized price of the extra charge | [optional] 

## Example

```python
from wink_sdk_booking.models.extra_charge_authenticated_entity import ExtraChargeAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ExtraChargeAuthenticatedEntity from a JSON string
extra_charge_authenticated_entity_instance = ExtraChargeAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ExtraChargeAuthenticatedEntity.to_json())

# convert the object into a dict
extra_charge_authenticated_entity_dict = extra_charge_authenticated_entity_instance.to_dict()
# create an instance of ExtraChargeAuthenticatedEntity from a dict
extra_charge_authenticated_entity_from_dict = ExtraChargeAuthenticatedEntity.from_dict(extra_charge_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


