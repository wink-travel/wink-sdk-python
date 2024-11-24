# BorderSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**dash_type** | **str** |  | [optional] 
**width** | **float** |  | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.border_supplier import BorderSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of BorderSupplier from a JSON string
border_supplier_instance = BorderSupplier.from_json(json)
# print the JSON string representation of the object
print(BorderSupplier.to_json())

# convert the object into a dict
border_supplier_dict = border_supplier_instance.to_dict()
# create an instance of BorderSupplier from a dict
border_supplier_from_dict = BorderSupplier.from_dict(border_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


