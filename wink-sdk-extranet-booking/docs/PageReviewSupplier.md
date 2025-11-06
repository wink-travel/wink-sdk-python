# PageReviewSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_pages** | **int** |  | [optional] 
**total_elements** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[ReviewSupplier]**](ReviewSupplier.md) |  | [optional] 
**number** | **int** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**sort** | [**SortObjectSupplier**](SortObjectSupplier.md) |  | [optional] 
**pageable** | [**PageableObjectSupplier**](PageableObjectSupplier.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_extranet_booking.models.page_review_supplier import PageReviewSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of PageReviewSupplier from a JSON string
page_review_supplier_instance = PageReviewSupplier.from_json(json)
# print the JSON string representation of the object
print(PageReviewSupplier.to_json())

# convert the object into a dict
page_review_supplier_dict = page_review_supplier_instance.to_dict()
# create an instance of PageReviewSupplier from a dict
page_review_supplier_from_dict = PageReviewSupplier.from_dict(page_review_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


