# UpsertCompanyOnlinePresenceRequestAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**online_presence** | [**List[OnlinePresenceAgent]**](OnlinePresenceAgent.md) |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.upsert_company_online_presence_request_affiliate import UpsertCompanyOnlinePresenceRequestAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertCompanyOnlinePresenceRequestAffiliate from a JSON string
upsert_company_online_presence_request_affiliate_instance = UpsertCompanyOnlinePresenceRequestAffiliate.from_json(json)
# print the JSON string representation of the object
print(UpsertCompanyOnlinePresenceRequestAffiliate.to_json())

# convert the object into a dict
upsert_company_online_presence_request_affiliate_dict = upsert_company_online_presence_request_affiliate_instance.to_dict()
# create an instance of UpsertCompanyOnlinePresenceRequestAffiliate from a dict
upsert_company_online_presence_request_affiliate_from_dict = UpsertCompanyOnlinePresenceRequestAffiliate.from_dict(upsert_company_online_presence_request_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


