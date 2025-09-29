# PropertyAggregateGreenIndexScoreByCategoryNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Green Index category | 
**high_score** | **int** | The highest possible score from all questions within this category | 
**total_score** | **int** | The total score from all questions answered within this category | 
**aggregate_score** | **float** | Total score divided by high score within this category | 

## Example

```python
from wink_sdk_inventory.models.property_aggregate_green_index_score_by_category_non_authenticated_entity import PropertyAggregateGreenIndexScoreByCategoryNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyAggregateGreenIndexScoreByCategoryNonAuthenticatedEntity from a JSON string
property_aggregate_green_index_score_by_category_non_authenticated_entity_instance = PropertyAggregateGreenIndexScoreByCategoryNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(PropertyAggregateGreenIndexScoreByCategoryNonAuthenticatedEntity.to_json())

# convert the object into a dict
property_aggregate_green_index_score_by_category_non_authenticated_entity_dict = property_aggregate_green_index_score_by_category_non_authenticated_entity_instance.to_dict()
# create an instance of PropertyAggregateGreenIndexScoreByCategoryNonAuthenticatedEntity from a dict
property_aggregate_green_index_score_by_category_non_authenticated_entity_from_dict = PropertyAggregateGreenIndexScoreByCategoryNonAuthenticatedEntity.from_dict(property_aggregate_green_index_score_by_category_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


