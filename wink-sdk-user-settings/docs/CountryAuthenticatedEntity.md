# CountryAuthenticatedEntity

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
from wink_sdk_user_settings.models.country_authenticated_entity import CountryAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CountryAuthenticatedEntity from a JSON string
country_authenticated_entity_instance = CountryAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(CountryAuthenticatedEntity.to_json())

# convert the object into a dict
country_authenticated_entity_dict = country_authenticated_entity_instance.to_dict()
# create an instance of CountryAuthenticatedEntity from a dict
country_authenticated_entity_from_dict = CountryAuthenticatedEntity.from_dict(country_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


