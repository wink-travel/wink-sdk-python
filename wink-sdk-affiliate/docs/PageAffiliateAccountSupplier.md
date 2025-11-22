# PageAffiliateAccountSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[AffiliateAccountSupplier]**](AffiliateAccountSupplier.md) |  | [optional] 
**number** | **int** |  | [optional] 
**pageable** | [**PageableObjectSupplier**](PageableObjectSupplier.md) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**sort** | [**SortObjectSupplier**](SortObjectSupplier.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.page_affiliate_account_supplier import PageAffiliateAccountSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of PageAffiliateAccountSupplier from a JSON string
page_affiliate_account_supplier_instance = PageAffiliateAccountSupplier.from_json(json)
# print the JSON string representation of the object
print(PageAffiliateAccountSupplier.to_json())

# convert the object into a dict
page_affiliate_account_supplier_dict = page_affiliate_account_supplier_instance.to_dict()
# create an instance of PageAffiliateAccountSupplier from a dict
page_affiliate_account_supplier_from_dict = PageAffiliateAccountSupplier.from_dict(page_affiliate_account_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


