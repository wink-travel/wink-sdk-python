# GlobalScoreRequestNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sort** | **str** | Choose the criteria you want the results sorted on. | 
**user_session** | [**UserSessionNonAuthenticatedEntity**](UserSessionNonAuthenticatedEntity.md) |  | 
**search_filters** | [**SearchFiltersNonAuthenticatedEntity**](SearchFiltersNonAuthenticatedEntity.md) |  | [optional] 
**page** | **int** | The page to paginate to. Note: Page uses a 0-based index. | [default to 0]
**size** | **int** | The result size to return. | [default to 6]

## Example

```python
from wink_sdk_lookup.models.global_score_request_non_authenticated_entity import GlobalScoreRequestNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalScoreRequestNonAuthenticatedEntity from a JSON string
global_score_request_non_authenticated_entity_instance = GlobalScoreRequestNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(GlobalScoreRequestNonAuthenticatedEntity.to_json())

# convert the object into a dict
global_score_request_non_authenticated_entity_dict = global_score_request_non_authenticated_entity_instance.to_dict()
# create an instance of GlobalScoreRequestNonAuthenticatedEntity from a dict
global_score_request_non_authenticated_entity_from_dict = GlobalScoreRequestNonAuthenticatedEntity.from_dict(global_score_request_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


