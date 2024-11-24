# SubSubCountryAuthenticatedEntity

Country sub sub division

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**ascii_name** | **str** |  | [optional] 
**geo_name_id** | **str** |  | [optional] 

## Example

```python
from wink_sdk_user_settings.models.sub_sub_country_authenticated_entity import SubSubCountryAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SubSubCountryAuthenticatedEntity from a JSON string
sub_sub_country_authenticated_entity_instance = SubSubCountryAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SubSubCountryAuthenticatedEntity.to_json())

# convert the object into a dict
sub_sub_country_authenticated_entity_dict = sub_sub_country_authenticated_entity_instance.to_dict()
# create an instance of SubSubCountryAuthenticatedEntity from a dict
sub_sub_country_authenticated_entity_from_dict = SubSubCountryAuthenticatedEntity.from_dict(sub_sub_country_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


