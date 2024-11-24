# PageCompanyViewSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[CompanyViewSupplier]**](CompanyViewSupplier.md) |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**List[SortObject]**](SortObject.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**PageableObjectSupplier**](PageableObjectSupplier.md) |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.page_company_view_supplier import PageCompanyViewSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of PageCompanyViewSupplier from a JSON string
page_company_view_supplier_instance = PageCompanyViewSupplier.from_json(json)
# print the JSON string representation of the object
print(PageCompanyViewSupplier.to_json())

# convert the object into a dict
page_company_view_supplier_dict = page_company_view_supplier_instance.to_dict()
# create an instance of PageCompanyViewSupplier from a dict
page_company_view_supplier_from_dict = PageCompanyViewSupplier.from_dict(page_company_view_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


