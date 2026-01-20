# PropertyAggregateGreenIndexAnswersNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel_identifier** | **str** |  | 
**list** | [**List[PropertyAggregateGreenIndexAnswerNonAuthenticatedEntity]**](PropertyAggregateGreenIndexAnswerNonAuthenticatedEntity.md) |  | 
**high_score** | **int** | The highest possible score from all questions | 
**total_score** | **int** | The total score from all questions answered | 
**aggregate_score** | **float** | Total score divided by high score | 
**scores_by_category** | [**List[PropertyAggregateGreenIndexScoreByCategoryNonAuthenticatedEntity]**](PropertyAggregateGreenIndexScoreByCategoryNonAuthenticatedEntity.md) | Aggregate scores by Green Index category | 

## Example

```python
from wink_sdk_inventory.models.property_aggregate_green_index_answers_non_authenticated_entity import PropertyAggregateGreenIndexAnswersNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyAggregateGreenIndexAnswersNonAuthenticatedEntity from a JSON string
property_aggregate_green_index_answers_non_authenticated_entity_instance = PropertyAggregateGreenIndexAnswersNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(PropertyAggregateGreenIndexAnswersNonAuthenticatedEntity.to_json())

# convert the object into a dict
property_aggregate_green_index_answers_non_authenticated_entity_dict = property_aggregate_green_index_answers_non_authenticated_entity_instance.to_dict()
# create an instance of PropertyAggregateGreenIndexAnswersNonAuthenticatedEntity from a dict
property_aggregate_green_index_answers_non_authenticated_entity_from_dict = PropertyAggregateGreenIndexAnswersNonAuthenticatedEntity.from_dict(property_aggregate_green_index_answers_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


