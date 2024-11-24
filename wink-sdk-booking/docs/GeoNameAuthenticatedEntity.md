# GeoNameAuthenticatedEntity

GeoNames have been created at [https://geonames.org](https://geonames.org) and contain geographical destinations we use as geoname data to associate travel inventory with a location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geo_name_id** | **str** | GeoName identifier | [optional] 
**type** | **str** | GeoName type | [optional] 
**name** | **str** | Name of city | [optional] 
**url_name** | **str** | Url name | [optional] 
**ascii_name** | **str** | Ascii name of city | [optional] 
**location** | [**GeoJsonPointAuthenticatedEntity**](GeoJsonPointAuthenticatedEntity.md) |  | [optional] 
**feature_code** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**timezone** | **str** | Timezone | [optional] 
**country** | [**CountryAuthenticatedEntity**](CountryAuthenticatedEntity.md) |  | [optional] 
**sub_country** | [**SubCountryAuthenticatedEntity**](SubCountryAuthenticatedEntity.md) |  | [optional] 
**sub_sub_country** | [**SubSubCountryAuthenticatedEntity**](SubSubCountryAuthenticatedEntity.md) |  | [optional] 

## Example

```python
from wink_sdk_booking.models.geo_name_authenticated_entity import GeoNameAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of GeoNameAuthenticatedEntity from a JSON string
geo_name_authenticated_entity_instance = GeoNameAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(GeoNameAuthenticatedEntity.to_json())

# convert the object into a dict
geo_name_authenticated_entity_dict = geo_name_authenticated_entity_instance.to_dict()
# create an instance of GeoNameAuthenticatedEntity from a dict
geo_name_authenticated_entity_from_dict = GeoNameAuthenticatedEntity.from_dict(geo_name_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


