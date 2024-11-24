# ReviewViewSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**review** | [**ReviewSupplier**](ReviewSupplier.md) |  | 

## Example

```python
from wink_sdk_extranet_booking.models.review_view_supplier import ReviewViewSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewViewSupplier from a JSON string
review_view_supplier_instance = ReviewViewSupplier.from_json(json)
# print the JSON string representation of the object
print(ReviewViewSupplier.to_json())

# convert the object into a dict
review_view_supplier_dict = review_view_supplier_instance.to_dict()
# create an instance of ReviewViewSupplier from a dict
review_view_supplier_from_dict = ReviewViewSupplier.from_dict(review_view_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


