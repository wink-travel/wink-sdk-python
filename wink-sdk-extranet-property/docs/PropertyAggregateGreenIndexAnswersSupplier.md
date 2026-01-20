# PropertyAggregateGreenIndexAnswersSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel_identifier** | **str** |  | 
**list** | [**List[PropertyAggregateGreenIndexAnswerSupplier]**](PropertyAggregateGreenIndexAnswerSupplier.md) |  | 
**high_score** | **int** | The highest possible score from all questions | 
**total_score** | **int** | The total score from all questions answered | 
**aggregate_score** | **float** | Total score divided by high score | 
**scores_by_category** | [**List[PropertyAggregateGreenIndexScoreByCategorySupplier]**](PropertyAggregateGreenIndexScoreByCategorySupplier.md) | Aggregate scores by Green Index category | 

## Example

```python
from wink_sdk_extranet_property.models.property_aggregate_green_index_answers_supplier import PropertyAggregateGreenIndexAnswersSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyAggregateGreenIndexAnswersSupplier from a JSON string
property_aggregate_green_index_answers_supplier_instance = PropertyAggregateGreenIndexAnswersSupplier.from_json(json)
# print the JSON string representation of the object
print(PropertyAggregateGreenIndexAnswersSupplier.to_json())

# convert the object into a dict
property_aggregate_green_index_answers_supplier_dict = property_aggregate_green_index_answers_supplier_instance.to_dict()
# create an instance of PropertyAggregateGreenIndexAnswersSupplier from a dict
property_aggregate_green_index_answers_supplier_from_dict = PropertyAggregateGreenIndexAnswersSupplier.from_dict(property_aggregate_green_index_answers_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


