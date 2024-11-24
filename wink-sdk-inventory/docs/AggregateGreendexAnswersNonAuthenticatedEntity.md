# AggregateGreendexAnswersNonAuthenticatedEntity

Detailed Green Index scores on hoe the property scores by category

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**high_score** | **int** | The highest possible score from all questions | [optional] 
**total_score** | **int** | The total score from all questions answered | [optional] 
**aggregate_score** | **float** | Total score divided by high score | [optional] 
**scores_by_category** | [**List[AggregateGreendexScoreByCategoryNonAuthenticatedEntity]**](AggregateGreendexScoreByCategoryNonAuthenticatedEntity.md) | Aggregate scores by Green Index category | [optional] 

## Example

```python
from wink_sdk_inventory.models.aggregate_greendex_answers_non_authenticated_entity import AggregateGreendexAnswersNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateGreendexAnswersNonAuthenticatedEntity from a JSON string
aggregate_greendex_answers_non_authenticated_entity_instance = AggregateGreendexAnswersNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(AggregateGreendexAnswersNonAuthenticatedEntity.to_json())

# convert the object into a dict
aggregate_greendex_answers_non_authenticated_entity_dict = aggregate_greendex_answers_non_authenticated_entity_instance.to_dict()
# create an instance of AggregateGreendexAnswersNonAuthenticatedEntity from a dict
aggregate_greendex_answers_non_authenticated_entity_from_dict = AggregateGreendexAnswersNonAuthenticatedEntity.from_dict(aggregate_greendex_answers_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


