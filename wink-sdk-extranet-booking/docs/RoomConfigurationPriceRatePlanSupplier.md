# RoomConfigurationPriceRatePlanSupplier

Rate plan used for this stay

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Rate plan identifier | 
**name** | **str** | Provides the name of the rate plan. | 
**breakfast** | **bool** | When true, indicates breakfast is included. | [default to False]
**brunch** | **bool** | When true, indicates brunch is included. | [default to False]
**lunch** | **bool** | When true, indicates lunch is included. | [default to False]
**dinner** | **bool** | When true, indicates dinner is included. | [default to False]
**all_inclusive** | **bool** | Everything included except alcohol | [default to False]
**all_inclusive_plus_alcohol** | **bool** | Everything included with alcohol | [default to False]
**early_check_in_charge** | [**VariableChargeSupplier**](VariableChargeSupplier.md) |  | [optional] 
**late_check_out_charge** | [**VariableChargeSupplier**](VariableChargeSupplier.md) |  | [optional] 
**cancellation_policy** | [**CancellationPolicySupplier**](CancellationPolicySupplier.md) |  | [optional] 
**cancellation_policy_exceptions** | [**CancellationPolicyExceptionsSupplier**](CancellationPolicyExceptionsSupplier.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.room_configuration_price_rate_plan_supplier import RoomConfigurationPriceRatePlanSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of RoomConfigurationPriceRatePlanSupplier from a JSON string
room_configuration_price_rate_plan_supplier_instance = RoomConfigurationPriceRatePlanSupplier.from_json(json)
# print the JSON string representation of the object
print(RoomConfigurationPriceRatePlanSupplier.to_json())

# convert the object into a dict
room_configuration_price_rate_plan_supplier_dict = room_configuration_price_rate_plan_supplier_instance.to_dict()
# create an instance of RoomConfigurationPriceRatePlanSupplier from a dict
room_configuration_price_rate_plan_supplier_from_dict = RoomConfigurationPriceRatePlanSupplier.from_dict(room_configuration_price_rate_plan_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


