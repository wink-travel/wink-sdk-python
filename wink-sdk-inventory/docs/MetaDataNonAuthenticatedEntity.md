# MetaDataNonAuthenticatedEntity

List of property meta data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from wink_sdk_inventory.models.meta_data_non_authenticated_entity import MetaDataNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of MetaDataNonAuthenticatedEntity from a JSON string
meta_data_non_authenticated_entity_instance = MetaDataNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(MetaDataNonAuthenticatedEntity.to_json())

# convert the object into a dict
meta_data_non_authenticated_entity_dict = meta_data_non_authenticated_entity_instance.to_dict()
# create an instance of MetaDataNonAuthenticatedEntity from a dict
meta_data_non_authenticated_entity_from_dict = MetaDataNonAuthenticatedEntity.from_dict(meta_data_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


