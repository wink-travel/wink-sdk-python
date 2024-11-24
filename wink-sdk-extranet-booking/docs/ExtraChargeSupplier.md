# ExtraChargeSupplier

List of extra charges that applies to the rate plan.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_plan_level_fee** | [**RatePlanLevelFeeSupplier**](RatePlanLevelFeeSupplier.md) |  | [optional] 
**unit_price** | [**LocalizedPriceSupplier**](LocalizedPriceSupplier.md) |  | [optional] 
**price** | [**LocalizedPriceSupplier**](LocalizedPriceSupplier.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.extra_charge_supplier import ExtraChargeSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ExtraChargeSupplier from a JSON string
extra_charge_supplier_instance = ExtraChargeSupplier.from_json(json)
# print the JSON string representation of the object
print(ExtraChargeSupplier.to_json())

# convert the object into a dict
extra_charge_supplier_dict = extra_charge_supplier_instance.to_dict()
# create an instance of ExtraChargeSupplier from a dict
extra_charge_supplier_from_dict = ExtraChargeSupplier.from_dict(extra_charge_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


