# CountryLightweightNonAuthenticatedEntity

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
from wink_sdk_reference.models.country_lightweight_non_authenticated_entity import CountryLightweightNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CountryLightweightNonAuthenticatedEntity from a JSON string
country_lightweight_non_authenticated_entity_instance = CountryLightweightNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(CountryLightweightNonAuthenticatedEntity.to_json())

# convert the object into a dict
country_lightweight_non_authenticated_entity_dict = country_lightweight_non_authenticated_entity_instance.to_dict()
# create an instance of CountryLightweightNonAuthenticatedEntity from a dict
country_lightweight_non_authenticated_entity_from_dict = CountryLightweightNonAuthenticatedEntity.from_dict(country_lightweight_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


