# PageBookingSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[BookingSupplier]**](BookingSupplier.md) |  | [optional] 
**number** | **int** |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**sort** | [**SortObjectSupplier**](SortObjectSupplier.md) |  | [optional] 
**pageable** | [**PageableObjectSupplier**](PageableObjectSupplier.md) |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.page_booking_supplier import PageBookingSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of PageBookingSupplier from a JSON string
page_booking_supplier_instance = PageBookingSupplier.from_json(json)
# print the JSON string representation of the object
print(PageBookingSupplier.to_json())

# convert the object into a dict
page_booking_supplier_dict = page_booking_supplier_instance.to_dict()
# create an instance of PageBookingSupplier from a dict
page_booking_supplier_from_dict = PageBookingSupplier.from_dict(page_booking_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


