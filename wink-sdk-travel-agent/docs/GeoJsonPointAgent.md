# GeoJsonPointAgent

Geo-location point where blocking takes place. Defaults to location of property.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **float** |  | [optional] 
**y** | **float** |  | [optional] 
**type** | **str** |  | [optional] 
**coordinates** | **List[float]** |  | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.geo_json_point_agent import GeoJsonPointAgent

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJsonPointAgent from a JSON string
geo_json_point_agent_instance = GeoJsonPointAgent.from_json(json)
# print the JSON string representation of the object
print(GeoJsonPointAgent.to_json())

# convert the object into a dict
geo_json_point_agent_dict = geo_json_point_agent_instance.to_dict()
# create an instance of GeoJsonPointAgent from a dict
geo_json_point_agent_from_dict = GeoJsonPointAgent.from_dict(geo_json_point_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


