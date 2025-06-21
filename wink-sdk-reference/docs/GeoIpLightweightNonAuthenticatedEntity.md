# GeoIpLightweightNonAuthenticatedEntity

Uses MaxMind's city lite db to persist GeoIpLightweight objects in our own db.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geo_name_id** | **str** | GeoNameLightweight identifiers taken from [https://geonames.org](https://geonames.org). | 
**locale_code** | **str** | Locale code | 
**continent_code** | **str** | Continent code | 
**continent_name** | **str** | Continent name | 
**country_iso_code** | **str** | Country ISO code | 
**country_name** | **str** | Country name | 
**city_name** | **str** | City name | 
**timezone** | **str** | Timezone | 
**sub_division1_code** | **str** | Sub-division 1 code | [optional] 
**sub_division1_name** | **str** | Sub-division 1 name | [optional] 
**sub_division2_code** | **str** | Sub-division 2 code | [optional] 
**sub_division2_name** | **str** | Sub-division 2 name | [optional] 

## Example

```python
from wink_sdk_reference.models.geo_ip_lightweight_non_authenticated_entity import GeoIpLightweightNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of GeoIpLightweightNonAuthenticatedEntity from a JSON string
geo_ip_lightweight_non_authenticated_entity_instance = GeoIpLightweightNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(GeoIpLightweightNonAuthenticatedEntity.to_json())

# convert the object into a dict
geo_ip_lightweight_non_authenticated_entity_dict = geo_ip_lightweight_non_authenticated_entity_instance.to_dict()
# create an instance of GeoIpLightweightNonAuthenticatedEntity from a dict
geo_ip_lightweight_non_authenticated_entity_from_dict = GeoIpLightweightNonAuthenticatedEntity.from_dict(geo_ip_lightweight_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


