# RoomConfigurationPriceRatePlanSupplierDetails


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
**early_check_in_charge** | [**VariableChargeSupplierDetails**](VariableChargeSupplierDetails.md) |  | [optional] 
**late_check_out_charge** | [**VariableChargeSupplierDetails**](VariableChargeSupplierDetails.md) |  | [optional] 
**cancellation_policy** | [**CancellationPolicyLightweightSupplierDetails**](CancellationPolicyLightweightSupplierDetails.md) | The cancellation policy for this rate plan. | [optional] 
**cancellation_policy_exceptions** | [**CancellationPolicyExceptionsSupplierDetails**](CancellationPolicyExceptionsSupplierDetails.md) | Allows a property to dynamically use another cancellation policy for a specific date range | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.room_configuration_price_rate_plan_supplier_details import RoomConfigurationPriceRatePlanSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RoomConfigurationPriceRatePlanSupplierDetails from a JSON string
room_configuration_price_rate_plan_supplier_details_instance = RoomConfigurationPriceRatePlanSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(RoomConfigurationPriceRatePlanSupplierDetails.to_json())

# convert the object into a dict
room_configuration_price_rate_plan_supplier_details_dict = room_configuration_price_rate_plan_supplier_details_instance.to_dict()
# create an instance of RoomConfigurationPriceRatePlanSupplierDetails from a dict
room_configuration_price_rate_plan_supplier_details_from_dict = RoomConfigurationPriceRatePlanSupplierDetails.from_dict(room_configuration_price_rate_plan_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


