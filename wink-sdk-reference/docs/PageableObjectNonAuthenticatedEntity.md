# PageableObjectNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | [optional] 
**sort** | [**SortObjectNonAuthenticatedEntity**](SortObjectNonAuthenticatedEntity.md) |  | [optional] 
**page_size** | **int** |  | [optional] 
**page_number** | **int** |  | [optional] 
**unpaged** | **bool** |  | [optional] 
**paged** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_reference.models.pageable_object_non_authenticated_entity import PageableObjectNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PageableObjectNonAuthenticatedEntity from a JSON string
pageable_object_non_authenticated_entity_instance = PageableObjectNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(PageableObjectNonAuthenticatedEntity.to_json())

# convert the object into a dict
pageable_object_non_authenticated_entity_dict = pageable_object_non_authenticated_entity_instance.to_dict()
# create an instance of PageableObjectNonAuthenticatedEntity from a dict
pageable_object_non_authenticated_entity_from_dict = PageableObjectNonAuthenticatedEntity.from_dict(pageable_object_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


