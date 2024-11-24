# StateSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip** | **int** | Number of records to be skipped by the pager. | [optional] [default to 0]
**take** | **int** | Number of records to take. | [optional] [default to 30]
**sort** | [**List[SortDescriptorSupplier]**](SortDescriptorSupplier.md) | Descriptors used for sorting result set. | [optional] 
**filter** | [**CompositeFilterDescriptorSupplier**](CompositeFilterDescriptorSupplier.md) |  | [optional] 
**group** | [**List[GroupDescriptorSupplier]**](GroupDescriptorSupplier.md) | Descriptors to group result sets by. | [optional] 

## Example

```python
from wink_sdk_affiliate.models.state_supplier import StateSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of StateSupplier from a JSON string
state_supplier_instance = StateSupplier.from_json(json)
# print the JSON string representation of the object
print(StateSupplier.to_json())

# convert the object into a dict
state_supplier_dict = state_supplier_instance.to_dict()
# create an instance of StateSupplier from a dict
state_supplier_from_dict = StateSupplier.from_dict(state_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


