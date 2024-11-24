# LookupCachedNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique lookup identifier | [optional] 
**type** | **str** | Type of lookup | [optional] 
**type_identifier** | **str** | Unique lookup type identifier | [optional] 
**name** | **str** | Name of lookup | [optional] 
**url_name** | **str** | Url-friendly slug that uniquely identifies this lookup | [optional] 
**owner_identifier** | **str** | Lookup that is supplier blocking includes the supplier identifier | [optional] 
**owner_name** | **str** | Lookup that is supplier blocking includes the supplier name | [optional] 
**city_name** | **str** | Closest city where lookup entry is located | [optional] 
**country_name** | **str** | Country where lookup entry is located | [optional] 
**sub_country_name** | **str** | State where lookup entry is located | [optional] 
**sub_sub_country_name** | **str** | County where lookup entry is located | [optional] 
**country_code** | **str** | Country code | [optional] 
**owner_type** | **str** | The type of owner that created this lookup | [optional] 
**language_code** | **str** | The language the lookup code was written in | [optional] 
**sort** | **int** | Platform-specific sort | [optional] 
**origin** | **bool** | If this lookup is the origin lookup. | [optional] 
**lowercase_name** | **str** | Name in lower case | [optional] 
**location_x** | **float** | Longitude | [optional] 
**location_y** | **float** | Latitude | [optional] 
**location** | [**GeoJsonPointNonAuthenticatedEntity**](GeoJsonPointNonAuthenticatedEntity.md) |  | [optional] 

## Example

```python
from wink_sdk_lookup.models.lookup_cached_non_authenticated_entity import LookupCachedNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of LookupCachedNonAuthenticatedEntity from a JSON string
lookup_cached_non_authenticated_entity_instance = LookupCachedNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(LookupCachedNonAuthenticatedEntity.to_json())

# convert the object into a dict
lookup_cached_non_authenticated_entity_dict = lookup_cached_non_authenticated_entity_instance.to_dict()
# create an instance of LookupCachedNonAuthenticatedEntity from a dict
lookup_cached_non_authenticated_entity_from_dict = LookupCachedNonAuthenticatedEntity.from_dict(lookup_cached_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


