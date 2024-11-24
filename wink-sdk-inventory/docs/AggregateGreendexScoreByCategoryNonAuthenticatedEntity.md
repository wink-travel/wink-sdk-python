# AggregateGreendexScoreByCategoryNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Green Index category | [optional] 
**high_score** | **int** | The highest possible score from all questions within this category | [optional] 
**total_score** | **int** | The total score from all questions answered within this category | [optional] 
**aggregate_score** | **float** | Total score divided by high score within this category | [optional] 

## Example

```python
from wink_sdk_inventory.models.aggregate_greendex_score_by_category_non_authenticated_entity import AggregateGreendexScoreByCategoryNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateGreendexScoreByCategoryNonAuthenticatedEntity from a JSON string
aggregate_greendex_score_by_category_non_authenticated_entity_instance = AggregateGreendexScoreByCategoryNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(AggregateGreendexScoreByCategoryNonAuthenticatedEntity.to_json())

# convert the object into a dict
aggregate_greendex_score_by_category_non_authenticated_entity_dict = aggregate_greendex_score_by_category_non_authenticated_entity_instance.to_dict()
# create an instance of AggregateGreendexScoreByCategoryNonAuthenticatedEntity from a dict
aggregate_greendex_score_by_category_non_authenticated_entity_from_dict = AggregateGreendexScoreByCategoryNonAuthenticatedEntity.from_dict(aggregate_greendex_score_by_category_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


