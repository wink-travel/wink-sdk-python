# ExtraChargeSupplierDetails

List of extra charges that applies to the rate plan.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_plan_level_fee** | [**RatePlanLevelFeeSupplierDetails**](RatePlanLevelFeeSupplierDetails.md) |  | [optional] 
**unit_price** | [**LocalizedPriceSupplierDetails**](LocalizedPriceSupplierDetails.md) |  | [optional] 
**price** | [**LocalizedPriceSupplierDetails**](LocalizedPriceSupplierDetails.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.extra_charge_supplier_details import ExtraChargeSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ExtraChargeSupplierDetails from a JSON string
extra_charge_supplier_details_instance = ExtraChargeSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(ExtraChargeSupplierDetails.to_json())

# convert the object into a dict
extra_charge_supplier_details_dict = extra_charge_supplier_details_instance.to_dict()
# create an instance of ExtraChargeSupplierDetails from a dict
extra_charge_supplier_details_from_dict = ExtraChargeSupplierDetails.from_dict(extra_charge_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


