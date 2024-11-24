# GeoJsonLineStringNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**coordinates** | [**List[PointNonAuthenticatedEntity]**](PointNonAuthenticatedEntity.md) |  | [optional] 

## Example

```python
from wink_sdk_inventory.models.geo_json_line_string_non_authenticated_entity import GeoJsonLineStringNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJsonLineStringNonAuthenticatedEntity from a JSON string
geo_json_line_string_non_authenticated_entity_instance = GeoJsonLineStringNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(GeoJsonLineStringNonAuthenticatedEntity.to_json())

# convert the object into a dict
geo_json_line_string_non_authenticated_entity_dict = geo_json_line_string_non_authenticated_entity_instance.to_dict()
# create an instance of GeoJsonLineStringNonAuthenticatedEntity from a dict
geo_json_line_string_non_authenticated_entity_from_dict = GeoJsonLineStringNonAuthenticatedEntity.from_dict(geo_json_line_string_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


