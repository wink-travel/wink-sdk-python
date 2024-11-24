# SubCountryAuthenticatedEntity

Country subdivision such as a state or province

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Sub-country name | [optional] 
**ascii_name** | **str** | Sub-country ascii name | [optional] 
**geo_name_id** | **str** | Sub-country GeoNames identifier | [optional] 

## Example

```python
from wink_sdk_user_settings.models.sub_country_authenticated_entity import SubCountryAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SubCountryAuthenticatedEntity from a JSON string
sub_country_authenticated_entity_instance = SubCountryAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SubCountryAuthenticatedEntity.to_json())

# convert the object into a dict
sub_country_authenticated_entity_dict = sub_country_authenticated_entity_instance.to_dict()
# create an instance of SubCountryAuthenticatedEntity from a dict
sub_country_authenticated_entity_from_dict = SubCountryAuthenticatedEntity.from_dict(sub_country_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


