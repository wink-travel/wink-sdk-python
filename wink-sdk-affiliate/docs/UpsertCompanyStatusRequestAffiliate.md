# UpsertCompanyStatusRequestAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | New company status | 

## Example

```python
from wink_sdk_affiliate.models.upsert_company_status_request_affiliate import UpsertCompanyStatusRequestAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertCompanyStatusRequestAffiliate from a JSON string
upsert_company_status_request_affiliate_instance = UpsertCompanyStatusRequestAffiliate.from_json(json)
# print the JSON string representation of the object
print(UpsertCompanyStatusRequestAffiliate.to_json())

# convert the object into a dict
upsert_company_status_request_affiliate_dict = upsert_company_status_request_affiliate_instance.to_dict()
# create an instance of UpsertCompanyStatusRequestAffiliate from a dict
upsert_company_status_request_affiliate_from_dict = UpsertCompanyStatusRequestAffiliate.from_dict(upsert_company_status_request_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


