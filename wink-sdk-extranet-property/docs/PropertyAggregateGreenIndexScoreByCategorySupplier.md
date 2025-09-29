# PropertyAggregateGreenIndexScoreByCategorySupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Green Index category | 
**high_score** | **int** | The highest possible score from all questions within this category | 
**total_score** | **int** | The total score from all questions answered within this category | 
**aggregate_score** | **float** | Total score divided by high score within this category | 

## Example

```python
from wink_sdk_extranet_property.models.property_aggregate_green_index_score_by_category_supplier import PropertyAggregateGreenIndexScoreByCategorySupplier

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyAggregateGreenIndexScoreByCategorySupplier from a JSON string
property_aggregate_green_index_score_by_category_supplier_instance = PropertyAggregateGreenIndexScoreByCategorySupplier.from_json(json)
# print the JSON string representation of the object
print(PropertyAggregateGreenIndexScoreByCategorySupplier.to_json())

# convert the object into a dict
property_aggregate_green_index_score_by_category_supplier_dict = property_aggregate_green_index_score_by_category_supplier_instance.to_dict()
# create an instance of PropertyAggregateGreenIndexScoreByCategorySupplier from a dict
property_aggregate_green_index_score_by_category_supplier_from_dict = PropertyAggregateGreenIndexScoreByCategorySupplier.from_dict(property_aggregate_green_index_score_by_category_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


