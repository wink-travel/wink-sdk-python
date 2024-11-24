# PlotBandSupplier

The plot bands of the category axis.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**var_from** | **str** |  | [optional] 
**opacity** | **float** |  | [optional] 
**to** | **str** |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.plot_band_supplier import PlotBandSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of PlotBandSupplier from a JSON string
plot_band_supplier_instance = PlotBandSupplier.from_json(json)
# print the JSON string representation of the object
print(PlotBandSupplier.to_json())

# convert the object into a dict
plot_band_supplier_dict = plot_band_supplier_instance.to_dict()
# create an instance of PlotBandSupplier from a dict
plot_band_supplier_from_dict = PlotBandSupplier.from_dict(plot_band_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


