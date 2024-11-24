# RatePlanLevelFeeSupplierDetails

What the guest is paying extra for

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descriptions** | [**List[LocalizedDescriptionSupplierDetails]**](LocalizedDescriptionSupplierDetails.md) | List of localized descriptions for this fee. | 
**fixed_amount** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | 
**type** | **str** | Rate plan fee type | 

## Example

```python
from wink_sdk_extranet_distribution.models.rate_plan_level_fee_supplier_details import RatePlanLevelFeeSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlanLevelFeeSupplierDetails from a JSON string
rate_plan_level_fee_supplier_details_instance = RatePlanLevelFeeSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(RatePlanLevelFeeSupplierDetails.to_json())

# convert the object into a dict
rate_plan_level_fee_supplier_details_dict = rate_plan_level_fee_supplier_details_instance.to_dict()
# create an instance of RatePlanLevelFeeSupplierDetails from a dict
rate_plan_level_fee_supplier_details_from_dict = RatePlanLevelFeeSupplierDetails.from_dict(rate_plan_level_fee_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


