# CreateCompanyRequestAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of company | 
**legal_name** | **str** | Legal name of entity if other than name | [optional] 
**company_type** | **str** | Type of company | 
**type** | **str** | Type of company | 
**description** | **str** | A personal message from the company. | [optional] 
**city_geo_name_id** | **str** | City geo name ID | 
**travel_agent** | **object** | If the company type is travel agent, this object will be filled out too. | [optional] 
**online_presence** | [**List[OnlinePresenceAffiliate]**](OnlinePresenceAffiliate.md) |  | [optional] 
**annual_travel_spend_in_dollars** | [**CustomMonetaryAmount**](CustomMonetaryAmount.md) |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.create_company_request_affiliate import CreateCompanyRequestAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCompanyRequestAffiliate from a JSON string
create_company_request_affiliate_instance = CreateCompanyRequestAffiliate.from_json(json)
# print the JSON string representation of the object
print(CreateCompanyRequestAffiliate.to_json())

# convert the object into a dict
create_company_request_affiliate_dict = create_company_request_affiliate_instance.to_dict()
# create an instance of CreateCompanyRequestAffiliate from a dict
create_company_request_affiliate_from_dict = CreateCompanyRequestAffiliate.from_dict(create_company_request_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


