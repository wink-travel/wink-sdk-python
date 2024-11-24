# CompanySupplier

A Company is our definition of a sales channel / affiliate. A property also has a company record.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique identifier | 
**user_identifier** | **str** | User or Registered client owner identifier that created this record | 
**owner** | [**CompanyUserSupplier**](CompanyUserSupplier.md) |  | 
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
**address** | [**AddressSupplier**](AddressSupplier.md) |  | 
**managers** | [**List[CompanyUserSupplier]**](CompanyUserSupplier.md) |  | [optional] 
**urls** | **List[str]** | List of all active accounts that could be used for selling or seeing a company&#39;s reach. | [optional] 
**logo** | [**SimpleMultimediaSupplier**](SimpleMultimediaSupplier.md) |  | [optional] 
**travel_agent** | [**TravelAgentSupplier**](TravelAgentSupplier.md) |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.company_supplier import CompanySupplier

# TODO update the JSON string below
json = "{}"
# create an instance of CompanySupplier from a JSON string
company_supplier_instance = CompanySupplier.from_json(json)
# print the JSON string representation of the object
print(CompanySupplier.to_json())

# convert the object into a dict
company_supplier_dict = company_supplier_instance.to_dict()
# create an instance of CompanySupplier from a dict
company_supplier_from_dict = CompanySupplier.from_dict(company_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


