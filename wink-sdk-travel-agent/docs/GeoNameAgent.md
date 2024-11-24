# GeoNameAgent

GeoNames have been created at [https://geonames.org](https://geonames.org) and contain geographical destinations we use as geoname data to associate travel inventory with a location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geo_name_id** | **str** | GeoName identifier | [optional] 
**type** | **str** | GeoName type | [optional] 
**name** | **str** | Name of city | [optional] 
**url_name** | **str** | Url name | [optional] 
**ascii_name** | **str** | Ascii name of city | [optional] 
**location** | [**GeoJsonPointAgent**](GeoJsonPointAgent.md) |  | [optional] 
**feature_code** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**timezone** | **str** | Timezone | [optional] 
**country** | [**CountryAgent**](CountryAgent.md) |  | [optional] 
**sub_country** | [**SubCountryAgent**](SubCountryAgent.md) |  | [optional] 
**sub_sub_country** | [**SubSubCountryAgent**](SubSubCountryAgent.md) |  | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.geo_name_agent import GeoNameAgent

# TODO update the JSON string below
json = "{}"
# create an instance of GeoNameAgent from a JSON string
geo_name_agent_instance = GeoNameAgent.from_json(json)
# print the JSON string representation of the object
print(GeoNameAgent.to_json())

# convert the object into a dict
geo_name_agent_dict = geo_name_agent_instance.to_dict()
# create an instance of GeoNameAgent from a dict
geo_name_agent_from_dict = GeoNameAgent.from_dict(geo_name_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


