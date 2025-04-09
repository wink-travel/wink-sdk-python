# PageHotelViewSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[HotelViewSupplier]**](HotelViewSupplier.md) |  | [optional] 
**number** | **int** |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**sort** | [**SortObjectSupplier**](SortObjectSupplier.md) |  | [optional] 
**pageable** | [**PageableObjectSupplier**](PageableObjectSupplier.md) |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_extranet_property.models.page_hotel_view_supplier import PageHotelViewSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of PageHotelViewSupplier from a JSON string
page_hotel_view_supplier_instance = PageHotelViewSupplier.from_json(json)
# print the JSON string representation of the object
print(PageHotelViewSupplier.to_json())

# convert the object into a dict
page_hotel_view_supplier_dict = page_hotel_view_supplier_instance.to_dict()
# create an instance of PageHotelViewSupplier from a dict
page_hotel_view_supplier_from_dict = PageHotelViewSupplier.from_dict(page_hotel_view_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


