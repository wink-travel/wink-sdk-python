# AggregateGreendexAnswersSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**high_score** | **int** | The highest possible score from all questions | [optional] 
**total_score** | **int** | The total score from all questions answered | [optional] 
**aggregate_score** | **float** | Total score divided by high score | [optional] 
**scores_by_category** | [**List[AggregateGreendexScoreByCategorySupplier]**](AggregateGreendexScoreByCategorySupplier.md) |  | [optional] 

## Example

```python
from wink_sdk_extranet_property.models.aggregate_greendex_answers_supplier import AggregateGreendexAnswersSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateGreendexAnswersSupplier from a JSON string
aggregate_greendex_answers_supplier_instance = AggregateGreendexAnswersSupplier.from_json(json)
# print the JSON string representation of the object
print(AggregateGreendexAnswersSupplier.to_json())

# convert the object into a dict
aggregate_greendex_answers_supplier_dict = aggregate_greendex_answers_supplier_instance.to_dict()
# create an instance of AggregateGreendexAnswersSupplier from a dict
aggregate_greendex_answers_supplier_from_dict = AggregateGreendexAnswersSupplier.from_dict(aggregate_greendex_answers_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


