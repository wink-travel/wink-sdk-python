# PagePropertySupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[PropertySupplier]**](PropertySupplier.md) |  | [optional] 
**number** | **int** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**sort** | [**SortObjectSupplier**](SortObjectSupplier.md) |  | [optional] 
**pageable** | [**PageableObjectSupplier**](PageableObjectSupplier.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_extranet_property.models.page_property_supplier import PagePropertySupplier

# TODO update the JSON string below
json = "{}"
# create an instance of PagePropertySupplier from a JSON string
page_property_supplier_instance = PagePropertySupplier.from_json(json)
# print the JSON string representation of the object
print(PagePropertySupplier.to_json())

# convert the object into a dict
page_property_supplier_dict = page_property_supplier_instance.to_dict()
# create an instance of PagePropertySupplier from a dict
page_property_supplier_from_dict = PagePropertySupplier.from_dict(page_property_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


