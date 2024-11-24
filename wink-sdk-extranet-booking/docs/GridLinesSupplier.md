# GridLinesSupplier

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
from wink_sdk_extranet_booking.models.grid_lines_supplier import GridLinesSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of GridLinesSupplier from a JSON string
grid_lines_supplier_instance = GridLinesSupplier.from_json(json)
# print the JSON string representation of the object
print(GridLinesSupplier.to_json())

# convert the object into a dict
grid_lines_supplier_dict = grid_lines_supplier_instance.to_dict()
# create an instance of GridLinesSupplier from a dict
grid_lines_supplier_from_dict = GridLinesSupplier.from_dict(grid_lines_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


