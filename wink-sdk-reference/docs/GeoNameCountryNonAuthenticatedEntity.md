# GeoNameCountryNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geo_name_id** | **str** |  | [optional] 
**continent_code** | **str** |  | [optional] 
**continent_name** | **str** |  | [optional] 
**country_iso_code** | **str** |  | [optional] 
**country_name** | **str** |  | [optional] 

## Example

```python
from wink_sdk_reference.models.geo_name_country_non_authenticated_entity import GeoNameCountryNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of GeoNameCountryNonAuthenticatedEntity from a JSON string
geo_name_country_non_authenticated_entity_instance = GeoNameCountryNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(GeoNameCountryNonAuthenticatedEntity.to_json())

# convert the object into a dict
geo_name_country_non_authenticated_entity_dict = geo_name_country_non_authenticated_entity_instance.to_dict()
# create an instance of GeoNameCountryNonAuthenticatedEntity from a dict
geo_name_country_non_authenticated_entity_from_dict = GeoNameCountryNonAuthenticatedEntity.from_dict(geo_name_country_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


