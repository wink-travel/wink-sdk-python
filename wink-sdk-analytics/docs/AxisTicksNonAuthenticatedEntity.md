# AxisTicksNonAuthenticatedEntity

The configuration of the category axis minor ticks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**size** | **float** |  | [optional] 
**step** | **float** |  | [optional] 
**skip** | **float** |  | [optional] 
**visible** | **bool** |  | [optional] 
**width** | **float** |  | [optional] 

## Example

```python
from wink_sdk_analytics.models.axis_ticks_non_authenticated_entity import AxisTicksNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AxisTicksNonAuthenticatedEntity from a JSON string
axis_ticks_non_authenticated_entity_instance = AxisTicksNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(AxisTicksNonAuthenticatedEntity.to_json())

# convert the object into a dict
axis_ticks_non_authenticated_entity_dict = axis_ticks_non_authenticated_entity_instance.to_dict()
# create an instance of AxisTicksNonAuthenticatedEntity from a dict
axis_ticks_non_authenticated_entity_from_dict = AxisTicksNonAuthenticatedEntity.from_dict(axis_ticks_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


