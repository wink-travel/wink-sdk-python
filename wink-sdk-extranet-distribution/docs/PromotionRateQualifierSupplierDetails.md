# PromotionRateQualifierSupplierDetails

Restrict promotion by requiring users to enter a promo code.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**promotion** | **str** | promotion code | 

## Example

```python
from wink_sdk_extranet_distribution.models.promotion_rate_qualifier_supplier_details import PromotionRateQualifierSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PromotionRateQualifierSupplierDetails from a JSON string
promotion_rate_qualifier_supplier_details_instance = PromotionRateQualifierSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(PromotionRateQualifierSupplierDetails.to_json())

# convert the object into a dict
promotion_rate_qualifier_supplier_details_dict = promotion_rate_qualifier_supplier_details_instance.to_dict()
# create an instance of PromotionRateQualifierSupplierDetails from a dict
promotion_rate_qualifier_supplier_details_from_dict = PromotionRateQualifierSupplierDetails.from_dict(promotion_rate_qualifier_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


