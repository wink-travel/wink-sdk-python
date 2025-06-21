# LookupLightweightAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique lookup identifier | [optional] 
**type** | **str** | Type of lookup | [optional] 
**type_identifier** | **str** | Unique lookup type identifier | [optional] 
**name** | **str** | Name of lookup | [optional] 
**url_name** | **str** | Url-friendly slug that uniquely identifies this lookup | [optional] 
**owner_identifier** | **str** | Lookup that is supplier inventory includes the supplier identifier | [optional] 
**owner_name** | **str** | Lookup that is supplier inventory includes the supplier name | [optional] 
**city_name** | **str** | Closest city where lookup entry is located | [optional] 
**country_name** | **str** | Country where lookup entry is located | [optional] 
**sub_country_name** | **str** | State where lookup entry is located | [optional] 
**sub_sub_country_name** | **str** | County where lookup entry is located | [optional] 
**country_code** | **str** | Country code | [optional] 
**owner_type** | **str** | The type of owner that created this lookup | [optional] 
**language_code** | **str** | The language the lookup code was written in | [optional] 
**sort** | **int** | Platform-specific sort | [optional] 
**origin** | **bool** | If this lookup is the origin lookup. | [optional] 
**lowercase_name** | **str** | Name in lower case | [optional] 
**location** | [**GeoJsonPointAffiliate**](GeoJsonPointAffiliate.md) | Geo-location | 

## Example

```python
from wink_sdk_affiliate_inventory.models.lookup_lightweight_affiliate import LookupLightweightAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of LookupLightweightAffiliate from a JSON string
lookup_lightweight_affiliate_instance = LookupLightweightAffiliate.from_json(json)
# print the JSON string representation of the object
print(LookupLightweightAffiliate.to_json())

# convert the object into a dict
lookup_lightweight_affiliate_dict = lookup_lightweight_affiliate_instance.to_dict()
# create an instance of LookupLightweightAffiliate from a dict
lookup_lightweight_affiliate_from_dict = LookupLightweightAffiliate.from_dict(lookup_lightweight_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


