# SpecialRateBundleLightweightAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique record identifier | 
**hotel_identifier** | **str** | Hotel identifier. | 
**name** | **str** | Internal name of promotion ancillary. | 
**enabled** | **bool** | Whether this promotion ancillary is enabled or not. | [default to True]
**items** | **List[object]** |  | 
**modifier_override** | **object** |  | [optional] 
**type** | **str** | Required if manual override modifier is not null | [optional] 
**pricing_type** | **str** | Determines whether this discount should be applied per night, per stay or per person - per night; Required if amount override is not null | [optional] 
**is_valid** | **bool** |  | [optional] 
**has_fixed_discount_modifier** | **bool** |  | [optional] 
**has_percent_discount_modifier** | **bool** |  | [optional] 
**description** | [**List[LocalizedDescriptionAffiliate]**](LocalizedDescriptionAffiliate.md) |  | [optional] 

## Example

```python
from wink_sdk_affiliate_browse.models.special_rate_bundle_lightweight_affiliate import SpecialRateBundleLightweightAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialRateBundleLightweightAffiliate from a JSON string
special_rate_bundle_lightweight_affiliate_instance = SpecialRateBundleLightweightAffiliate.from_json(json)
# print the JSON string representation of the object
print(SpecialRateBundleLightweightAffiliate.to_json())

# convert the object into a dict
special_rate_bundle_lightweight_affiliate_dict = special_rate_bundle_lightweight_affiliate_instance.to_dict()
# create an instance of SpecialRateBundleLightweightAffiliate from a dict
special_rate_bundle_lightweight_affiliate_from_dict = SpecialRateBundleLightweightAffiliate.from_dict(special_rate_bundle_lightweight_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


