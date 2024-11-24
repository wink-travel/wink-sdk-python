# BookingViewSupplierDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**booking** | [**BookingSupplierDetails**](BookingSupplierDetails.md) |  | 

## Example

```python
from wink_sdk_extranet_booking.models.booking_view_supplier_details import BookingViewSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BookingViewSupplierDetails from a JSON string
booking_view_supplier_details_instance = BookingViewSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(BookingViewSupplierDetails.to_json())

# convert the object into a dict
booking_view_supplier_details_dict = booking_view_supplier_details_instance.to_dict()
# create an instance of BookingViewSupplierDetails from a dict
booking_view_supplier_details_from_dict = BookingViewSupplierDetails.from_dict(booking_view_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


