# SpecialRateBundleLightweightSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **UUID** | Unique record identifier | 
**hotel_identifier** | **UUID** | Hotel identifier. | 
**name** | **str** | Internal name of promotion ancillary. | 
**enabled** | **bool** | Whether this promotion ancillary is enabled or not. | [default to True]
**items** | [**List[SpecialRateLightweightSupplier]**](SpecialRateLightweightSupplier.md) |  | 
**modifier_override** | [**VariableChargeSupplier**](VariableChargeSupplier.md) |  | [optional] 
**type** | **str** | Required if manual override modifier is not null | [optional] 
**pricing_type** | **str** | Determines whether this discount should be applied per night, per stay or per person - per night; Required if amount override is not null | [optional] 
**is_valid** | **bool** |  | [optional] 
**has_fixed_discount_modifier** | **bool** |  | [optional] 
**has_percent_discount_modifier** | **bool** |  | [optional] 
**description** | [**List[LocalizedDescriptionSupplier]**](LocalizedDescriptionSupplier.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_distribution.models.special_rate_bundle_lightweight_supplier import SpecialRateBundleLightweightSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialRateBundleLightweightSupplier from a JSON string
special_rate_bundle_lightweight_supplier_instance = SpecialRateBundleLightweightSupplier.from_json(json)
# print the JSON string representation of the object
print(SpecialRateBundleLightweightSupplier.to_json())

# convert the object into a dict
special_rate_bundle_lightweight_supplier_dict = special_rate_bundle_lightweight_supplier_instance.to_dict()
# create an instance of SpecialRateBundleLightweightSupplier from a dict
special_rate_bundle_lightweight_supplier_from_dict = SpecialRateBundleLightweightSupplier.from_dict(special_rate_bundle_lightweight_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


