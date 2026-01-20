# RoomConfigurationPriceRatePlanNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **UUID** | Rate plan identifier | 
**name** | **str** | Provides the name of the rate plan. | 
**breakfast** | **bool** | When true, indicates breakfast is included. | [default to False]
**brunch** | **bool** | When true, indicates brunch is included. | [default to False]
**lunch** | **bool** | When true, indicates lunch is included. | [default to False]
**dinner** | **bool** | When true, indicates dinner is included. | [default to False]
**all_inclusive** | **bool** | Everything included except alcohol | [default to False]
**all_inclusive_plus_alcohol** | **bool** | Everything included with alcohol | [default to False]
**early_check_in_charge** | **object** |  | [optional] 
**late_check_out_charge** | **object** |  | [optional] 
**cancellation_policy** | [**CancellationPolicyLightweightNonAuthenticatedEntity**](CancellationPolicyLightweightNonAuthenticatedEntity.md) | The cancellation policy for this rate plan. | [optional] 
**cancellation_policy_exceptions** | [**CancellationPolicyExceptionsNonAuthenticatedEntity**](CancellationPolicyExceptionsNonAuthenticatedEntity.md) | Allows a property to dynamically use another cancellation policy for a specific date range | [optional] 

## Example

```python
from wink_sdk_inventory.models.room_configuration_price_rate_plan_non_authenticated_entity import RoomConfigurationPriceRatePlanNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of RoomConfigurationPriceRatePlanNonAuthenticatedEntity from a JSON string
room_configuration_price_rate_plan_non_authenticated_entity_instance = RoomConfigurationPriceRatePlanNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(RoomConfigurationPriceRatePlanNonAuthenticatedEntity.to_json())

# convert the object into a dict
room_configuration_price_rate_plan_non_authenticated_entity_dict = room_configuration_price_rate_plan_non_authenticated_entity_instance.to_dict()
# create an instance of RoomConfigurationPriceRatePlanNonAuthenticatedEntity from a dict
room_configuration_price_rate_plan_non_authenticated_entity_from_dict = RoomConfigurationPriceRatePlanNonAuthenticatedEntity.from_dict(room_configuration_price_rate_plan_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


