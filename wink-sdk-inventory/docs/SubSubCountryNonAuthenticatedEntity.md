# SubSubCountryNonAuthenticatedEntity

Country sub sub division

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**ascii_name** | **str** |  | [optional] 
**geo_name_id** | **str** |  | [optional] 

## Example

```python
from wink_sdk_inventory.models.sub_sub_country_non_authenticated_entity import SubSubCountryNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SubSubCountryNonAuthenticatedEntity from a JSON string
sub_sub_country_non_authenticated_entity_instance = SubSubCountryNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SubSubCountryNonAuthenticatedEntity.to_json())

# convert the object into a dict
sub_sub_country_non_authenticated_entity_dict = sub_sub_country_non_authenticated_entity_instance.to_dict()
# create an instance of SubSubCountryNonAuthenticatedEntity from a dict
sub_sub_country_non_authenticated_entity_from_dict = SubSubCountryNonAuthenticatedEntity.from_dict(sub_sub_country_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


