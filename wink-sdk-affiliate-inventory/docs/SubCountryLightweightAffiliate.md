# SubCountryLightweightAffiliate

Country subdivision such as a state or province

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Sub-country name | [optional] 
**ascii_name** | **str** | Sub-country ascii name | [optional] 
**geo_name_id** | **str** | Sub-country GeoNames identifier | [optional] 

## Example

```python
from wink_sdk_affiliate_inventory.models.sub_country_lightweight_affiliate import SubCountryLightweightAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SubCountryLightweightAffiliate from a JSON string
sub_country_lightweight_affiliate_instance = SubCountryLightweightAffiliate.from_json(json)
# print the JSON string representation of the object
print(SubCountryLightweightAffiliate.to_json())

# convert the object into a dict
sub_country_lightweight_affiliate_dict = sub_country_lightweight_affiliate_instance.to_dict()
# create an instance of SubCountryLightweightAffiliate from a dict
sub_country_lightweight_affiliate_from_dict = SubCountryLightweightAffiliate.from_dict(sub_country_lightweight_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


