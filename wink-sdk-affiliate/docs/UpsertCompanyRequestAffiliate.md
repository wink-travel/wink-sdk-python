# UpsertCompanyRequestAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of company | 
**legal_name** | **str** | Legal name of entity if other than name | [optional] 
**company_type** | **str** | Type of company | 
**type** | **str** | Type of company | 
**description** | **str** | Account description. | [optional] 
**annual_travel_spend_in_dollars** | **int** | How much user or company spends on travel per year. | [optional] 

## Example

```python
from wink_sdk_affiliate.models.upsert_company_request_affiliate import UpsertCompanyRequestAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertCompanyRequestAffiliate from a JSON string
upsert_company_request_affiliate_instance = UpsertCompanyRequestAffiliate.from_json(json)
# print the JSON string representation of the object
print(UpsertCompanyRequestAffiliate.to_json())

# convert the object into a dict
upsert_company_request_affiliate_dict = upsert_company_request_affiliate_instance.to_dict()
# create an instance of UpsertCompanyRequestAffiliate from a dict
upsert_company_request_affiliate_from_dict = UpsertCompanyRequestAffiliate.from_dict(upsert_company_request_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


