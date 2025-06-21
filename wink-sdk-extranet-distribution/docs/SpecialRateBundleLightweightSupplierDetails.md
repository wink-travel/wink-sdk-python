# SpecialRateBundleLightweightSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique record identifier | 
**hotel_identifier** | **str** | Hotel identifier. | 
**name** | **str** | Internal name of promotion ancillary. | 
**enabled** | **bool** | Whether this promotion ancillary is enabled or not. | [default to True]
**items** | **List[object]** |  | 
**modifier_override** | [**VariableChargeSupplierDetails**](VariableChargeSupplierDetails.md) |  | [optional] 
**type** | **str** | Required if manual override modifier is not null | [optional] 
**pricing_type** | **str** | Determines whether this discount should be applied per night, per stay or per person - per night; Required if amount override is not null | [optional] 
**is_valid** | **bool** |  | [optional] 
**description** | [**List[LocalizedDescriptionSupplierDetails]**](LocalizedDescriptionSupplierDetails.md) |  | [optional] 
**has_fixed_discount_modifier** | **bool** |  | [optional] 
**has_percent_discount_modifier** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.special_rate_bundle_lightweight_supplier_details import SpecialRateBundleLightweightSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialRateBundleLightweightSupplierDetails from a JSON string
special_rate_bundle_lightweight_supplier_details_instance = SpecialRateBundleLightweightSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(SpecialRateBundleLightweightSupplierDetails.to_json())

# convert the object into a dict
special_rate_bundle_lightweight_supplier_details_dict = special_rate_bundle_lightweight_supplier_details_instance.to_dict()
# create an instance of SpecialRateBundleLightweightSupplierDetails from a dict
special_rate_bundle_lightweight_supplier_details_from_dict = SpecialRateBundleLightweightSupplierDetails.from_dict(special_rate_bundle_lightweight_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


