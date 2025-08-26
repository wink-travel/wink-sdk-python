# CreateAffiliateAccountRequestAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of company | 
**legal_name** | **str** | Legal name of entity if other than name | [optional] 
**url_name** | **str** | Url slug of entity | [optional] 
**unique_id** | **str** | Unique short ID of entity | [optional] 
**company_type** | **str** | Type of company | 
**type** | **str** | Type of company | 
**description** | **str** | Account description. | [optional] 
**city_geo_name_id** | **str** | City geo name ID | 
**travel_agent** | **object** |  | [optional] 
**online_presence** | **List[object]** |  | [optional] 
**annual_travel_spend_in_dollars** | **int** | How much user or company spends on travel per year. | [optional] 

## Example

```python
from wink_sdk_affiliate.models.create_affiliate_account_request_affiliate import CreateAffiliateAccountRequestAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAffiliateAccountRequestAffiliate from a JSON string
create_affiliate_account_request_affiliate_instance = CreateAffiliateAccountRequestAffiliate.from_json(json)
# print the JSON string representation of the object
print(CreateAffiliateAccountRequestAffiliate.to_json())

# convert the object into a dict
create_affiliate_account_request_affiliate_dict = create_affiliate_account_request_affiliate_instance.to_dict()
# create an instance of CreateAffiliateAccountRequestAffiliate from a dict
create_affiliate_account_request_affiliate_from_dict = CreateAffiliateAccountRequestAffiliate.from_dict(create_affiliate_account_request_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


