# CountryAffiliate

Country

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso** | **str** | ISO code | [optional] 
**name** | **str** | Country name | [optional] 
**capital** | **str** | Country capital | [optional] 
**continent** | **str** | Continent code | [optional] 
**currency_code** | **str** | Currency code | [optional] 
**currency_name** | **str** | Currency name | [optional] 
**geo_name_id** | **str** | Country GeoNames identifier | [optional] 

## Example

```python
from wink_sdk_affiliate_browse.models.country_affiliate import CountryAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of CountryAffiliate from a JSON string
country_affiliate_instance = CountryAffiliate.from_json(json)
# print the JSON string representation of the object
print(CountryAffiliate.to_json())

# convert the object into a dict
country_affiliate_dict = country_affiliate_instance.to_dict()
# create an instance of CountryAffiliate from a dict
country_affiliate_from_dict = CountryAffiliate.from_dict(country_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


