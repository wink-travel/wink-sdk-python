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
**description** | **str** | A personal message from the company. | [optional] 
**address** | [**AddressAgent**](AddressAgent.md) |  | 
**managers** | [**List[CompanyUserAgent]**](CompanyUserAgent.md) |  | [optional] 
**logo** | [**SimpleMultimediaAgent**](SimpleMultimediaAgent.md) |  | [optional] 
**travel_agent** | [**TravelAgentAgent**](TravelAgentAgent.md) |  | [optional] 
**managed_by** | [**ManagedByEntityAgent**](ManagedByEntityAgent.md) |  | [optional] 
**online_presence** | [**List[OnlinePresenceAgent]**](OnlinePresenceAgent.md) |  | [optional] 
**annual_travel_spend_in_dollars** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 

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


