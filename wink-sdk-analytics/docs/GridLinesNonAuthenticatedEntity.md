# GridLinesNonAuthenticatedEntity

The configuration of the minor grid lines. These are the lines that are an extension of the minor ticks through the body of the Chart.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**dash_type** | **str** |  | [optional] 
**skip** | **float** |  | [optional] 
**step** | **float** |  | [optional] 
**visible** | **bool** |  | [optional] 
**width** | **float** |  | [optional] 

## Example

```python
from wink_sdk_analytics.models.grid_lines_non_authenticated_entity import GridLinesNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of GridLinesNonAuthenticatedEntity from a JSON string
grid_lines_non_authenticated_entity_instance = GridLinesNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(GridLinesNonAuthenticatedEntity.to_json())

# convert the object into a dict
grid_lines_non_authenticated_entity_dict = grid_lines_non_authenticated_entity_instance.to_dict()
# create an instance of GridLinesNonAuthenticatedEntity from a dict
grid_lines_non_authenticated_entity_from_dict = GridLinesNonAuthenticatedEntity.from_dict(grid_lines_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


