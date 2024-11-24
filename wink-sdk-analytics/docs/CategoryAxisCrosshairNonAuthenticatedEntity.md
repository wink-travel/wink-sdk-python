# CategoryAxisCrosshairNonAuthenticatedEntity

The configuration options of the crosshair. The crosshair is displayed when the `categoryAxis.crosshair.visible` option is set to `true`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**dash_type** | **str** |  | [optional] 
**opacity** | **float** |  | [optional] 
**visible** | **bool** |  | [optional] 
**width** | **float** |  | [optional] 
**tooltip** | [**CategoryAxisCrosshairTooltipNonAuthenticatedEntity**](CategoryAxisCrosshairTooltipNonAuthenticatedEntity.md) |  | [optional] 

## Example

```python
from wink_sdk_analytics.models.category_axis_crosshair_non_authenticated_entity import CategoryAxisCrosshairNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryAxisCrosshairNonAuthenticatedEntity from a JSON string
category_axis_crosshair_non_authenticated_entity_instance = CategoryAxisCrosshairNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(CategoryAxisCrosshairNonAuthenticatedEntity.to_json())

# convert the object into a dict
category_axis_crosshair_non_authenticated_entity_dict = category_axis_crosshair_non_authenticated_entity_instance.to_dict()
# create an instance of CategoryAxisCrosshairNonAuthenticatedEntity from a dict
category_axis_crosshair_non_authenticated_entity_from_dict = CategoryAxisCrosshairNonAuthenticatedEntity.from_dict(category_axis_crosshair_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


