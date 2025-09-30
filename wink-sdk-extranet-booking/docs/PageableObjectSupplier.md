# PageableObjectSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | [optional] 
**unpaged** | **bool** |  | [optional] 
**sort** | [**SortObjectSupplier**](SortObjectSupplier.md) |  | [optional] 
**paged** | **bool** |  | [optional] 
**page_number** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.pageable_object_supplier import PageableObjectSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of PageableObjectSupplier from a JSON string
pageable_object_supplier_instance = PageableObjectSupplier.from_json(json)
# print the JSON string representation of the object
print(PageableObjectSupplier.to_json())

# convert the object into a dict
pageable_object_supplier_dict = pageable_object_supplier_instance.to_dict()
# create an instance of PageableObjectSupplier from a dict
pageable_object_supplier_from_dict = PageableObjectSupplier.from_dict(pageable_object_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


