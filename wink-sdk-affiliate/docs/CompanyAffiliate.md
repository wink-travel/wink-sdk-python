# CompanyAffiliate

A Company is our definition of a sales channel / affiliate. A property also has a company record.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique identifier | 
**user_identifier** | **str** | User or Registered client owner identifier that created this record | 
**owner** | [**CompanyUserAffiliate**](CompanyUserAffiliate.md) |  | 
**name** | **str** | Name of company | 
**url_name** | **str** | Url slug of company name | 
**legal_name** | **str** | Legal name of entity if other than name | [optional] 
**enabled** | **bool** | Whether this company is enabled by reactive. | 
**approved** | **bool** | Whether this company has been approved by KYC. | [default to False]
**company_type** | **str** | Type of company | 
**type** | **str** | Type of sales channel | 
**vat_id** | **str** | An optional VAT ID | 
**description** | **str** | A personal message from the company. | [optional] 
**url** | **str** | Company&#39;s main website | 
**address** | [**AddressAffiliate**](AddressAffiliate.md) |  | 
**managers** | [**List[CompanyUserAffiliate]**](CompanyUserAffiliate.md) |  | [optional] 
**urls** | **List[str]** | List of all active accounts that could be used for selling or seeing a company&#39;s reach. | [optional] 
**logo** | [**SimpleMultimediaAffiliate**](SimpleMultimediaAffiliate.md) |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.company_affiliate import CompanyAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyAffiliate from a JSON string
company_affiliate_instance = CompanyAffiliate.from_json(json)
# print the JSON string representation of the object
print(CompanyAffiliate.to_json())

# convert the object into a dict
company_affiliate_dict = company_affiliate_instance.to_dict()
# create an instance of CompanyAffiliate from a dict
company_affiliate_from_dict = CompanyAffiliate.from_dict(company_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


