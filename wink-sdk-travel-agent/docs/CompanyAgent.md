# CompanyAgent

A Company is our definition of a sales channel / affiliate. A property also has a company record.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique identifier | 
**user_identifier** | **str** | User or Registered client owner identifier that created this record | 
**owner** | [**CompanyUserAgent**](CompanyUserAgent.md) |  | 
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
**address** | [**AddressAgent**](AddressAgent.md) |  | 
**managers** | [**List[CompanyUserAgent]**](CompanyUserAgent.md) |  | [optional] 
**urls** | **List[str]** | List of all active accounts that could be used for selling or seeing a company&#39;s reach. | [optional] 
**logo** | [**SimpleMultimediaAgent**](SimpleMultimediaAgent.md) |  | [optional] 
**travel_agent** | [**TravelAgentAgent**](TravelAgentAgent.md) |  | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.company_agent import CompanyAgent

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyAgent from a JSON string
company_agent_instance = CompanyAgent.from_json(json)
# print the JSON string representation of the object
print(CompanyAgent.to_json())

# convert the object into a dict
company_agent_dict = company_agent_instance.to_dict()
# create an instance of CompanyAgent from a dict
company_agent_from_dict = CompanyAgent.from_dict(company_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


