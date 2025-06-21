# GeoJsonPointAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **float** |  | [optional] 
**y** | **float** |  | [optional] 
**type** | **str** |  | [optional] 
**coordinates** | **List[float]** |  | [optional] 

## Example

```python
from wink_sdk_booking.models.geo_json_point_authenticated_entity import GeoJsonPointAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJsonPointAuthenticatedEntity from a JSON string
geo_json_point_authenticated_entity_instance = GeoJsonPointAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(GeoJsonPointAuthenticatedEntity.to_json())

# convert the object into a dict
geo_json_point_authenticated_entity_dict = geo_json_point_authenticated_entity_instance.to_dict()
# create an instance of GeoJsonPointAuthenticatedEntity from a dict
geo_json_point_authenticated_entity_from_dict = GeoJsonPointAuthenticatedEntity.from_dict(geo_json_point_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


