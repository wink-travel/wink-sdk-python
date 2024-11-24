# GeoJsonPointBooker

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
from wink_sdk_booking.models.geo_json_point_booker import GeoJsonPointBooker

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJsonPointBooker from a JSON string
geo_json_point_booker_instance = GeoJsonPointBooker.from_json(json)
# print the JSON string representation of the object
print(GeoJsonPointBooker.to_json())

# convert the object into a dict
geo_json_point_booker_dict = geo_json_point_booker_instance.to_dict()
# create an instance of GeoJsonPointBooker from a dict
geo_json_point_booker_from_dict = GeoJsonPointBooker.from_dict(geo_json_point_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


