# SearchByGeoLocation400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**error** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from wink_sdk_lookup.models.search_by_geo_location400_response import SearchByGeoLocation400Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchByGeoLocation400Response from a JSON string
search_by_geo_location400_response_instance = SearchByGeoLocation400Response.from_json(json)
# print the JSON string representation of the object
print(SearchByGeoLocation400Response.to_json())

# convert the object into a dict
search_by_geo_location400_response_dict = search_by_geo_location400_response_instance.to_dict()
# create an instance of SearchByGeoLocation400Response from a dict
search_by_geo_location400_response_from_dict = SearchByGeoLocation400Response.from_dict(search_by_geo_location400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


