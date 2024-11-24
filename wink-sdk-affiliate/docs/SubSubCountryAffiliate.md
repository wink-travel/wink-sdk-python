# SubSubCountryAffiliate

Country sub sub division

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**ascii_name** | **str** |  | [optional] 
**geo_name_id** | **str** |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.sub_sub_country_affiliate import SubSubCountryAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SubSubCountryAffiliate from a JSON string
sub_sub_country_affiliate_instance = SubSubCountryAffiliate.from_json(json)
# print the JSON string representation of the object
print(SubSubCountryAffiliate.to_json())

# convert the object into a dict
sub_sub_country_affiliate_dict = sub_sub_country_affiliate_instance.to_dict()
# create an instance of SubSubCountryAffiliate from a dict
sub_sub_country_affiliate_from_dict = SubSubCountryAffiliate.from_dict(sub_sub_country_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


