# LookupLightweightNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **UUID** | Unique lookup identifier | [optional] 
**type** | **str** | Type of lookup | [optional] 
**type_identifier** | **UUID** | Unique lookup type identifier | [optional] 
**name** | **str** | Name of lookup | [optional] 
**url_name** | **str** | Url-friendly slug that uniquely identifies this lookup | [optional] 
**owner_identifier** | **UUID** | Lookup that is supplier inventory includes the supplier identifier | [optional] 
**owner_name** | **str** | Lookup that is supplier inventory includes the supplier name | [optional] 
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
**location** | [**GeoJsonPointNonAuthenticatedEntity**](GeoJsonPointNonAuthenticatedEntity.md) | Geo-location | 

## Example

```python
from wink_sdk_lookup.models.lookup_lightweight_non_authenticated_entity import LookupLightweightNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of LookupLightweightNonAuthenticatedEntity from a JSON string
lookup_lightweight_non_authenticated_entity_instance = LookupLightweightNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(LookupLightweightNonAuthenticatedEntity.to_json())

# convert the object into a dict
lookup_lightweight_non_authenticated_entity_dict = lookup_lightweight_non_authenticated_entity_instance.to_dict()
# create an instance of LookupLightweightNonAuthenticatedEntity from a dict
lookup_lightweight_non_authenticated_entity_from_dict = LookupLightweightNonAuthenticatedEntity.from_dict(lookup_lightweight_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


