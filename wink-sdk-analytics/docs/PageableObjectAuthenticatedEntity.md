# PageableObjectAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**sort** | [**SortObjectAuthenticatedEntity**](SortObjectAuthenticatedEntity.md) |  | [optional] 
**unpaged** | **bool** |  | [optional] 
**paged** | **bool** |  | [optional] 
**page_number** | **int** |  | [optional] 

## Example

```python
from wink_sdk_analytics.models.pageable_object_authenticated_entity import PageableObjectAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PageableObjectAuthenticatedEntity from a JSON string
pageable_object_authenticated_entity_instance = PageableObjectAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(PageableObjectAuthenticatedEntity.to_json())

# convert the object into a dict
pageable_object_authenticated_entity_dict = pageable_object_authenticated_entity_instance.to_dict()
# create an instance of PageableObjectAuthenticatedEntity from a dict
pageable_object_authenticated_entity_from_dict = PageableObjectAuthenticatedEntity.from_dict(pageable_object_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


