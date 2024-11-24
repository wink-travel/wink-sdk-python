# PageReviewViewSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[ReviewViewSupplier]**](ReviewViewSupplier.md) |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**List[SortObject]**](SortObject.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**PageableObjectSupplier**](PageableObjectSupplier.md) |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.page_review_view_supplier import PageReviewViewSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of PageReviewViewSupplier from a JSON string
page_review_view_supplier_instance = PageReviewViewSupplier.from_json(json)
# print the JSON string representation of the object
print(PageReviewViewSupplier.to_json())

# convert the object into a dict
page_review_view_supplier_dict = page_review_view_supplier_instance.to_dict()
# create an instance of PageReviewViewSupplier from a dict
page_review_view_supplier_from_dict = PageReviewViewSupplier.from_dict(page_review_view_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


