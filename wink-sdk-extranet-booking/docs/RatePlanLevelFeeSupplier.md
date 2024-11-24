# RatePlanLevelFeeSupplier

What the guest is paying extra for

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descriptions** | [**List[LocalizedDescriptionSupplier]**](LocalizedDescriptionSupplier.md) | List of localized descriptions for this fee. | 
**fixed_amount** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | 
**type** | **str** | Rate plan fee type | 

## Example

```python
from wink_sdk_extranet_booking.models.rate_plan_level_fee_supplier import RatePlanLevelFeeSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlanLevelFeeSupplier from a JSON string
rate_plan_level_fee_supplier_instance = RatePlanLevelFeeSupplier.from_json(json)
# print the JSON string representation of the object
print(RatePlanLevelFeeSupplier.to_json())

# convert the object into a dict
rate_plan_level_fee_supplier_dict = rate_plan_level_fee_supplier_instance.to_dict()
# create an instance of RatePlanLevelFeeSupplier from a dict
rate_plan_level_fee_supplier_from_dict = RatePlanLevelFeeSupplier.from_dict(rate_plan_level_fee_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


