# UpsertCompanyLogoRequestAffiliate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logo** | [**SimpleMultimediaAffiliate**](SimpleMultimediaAffiliate.md) |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.upsert_company_logo_request_affiliate import UpsertCompanyLogoRequestAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertCompanyLogoRequestAffiliate from a JSON string
upsert_company_logo_request_affiliate_instance = UpsertCompanyLogoRequestAffiliate.from_json(json)
# print the JSON string representation of the object
print(UpsertCompanyLogoRequestAffiliate.to_json())

# convert the object into a dict
upsert_company_logo_request_affiliate_dict = upsert_company_logo_request_affiliate_instance.to_dict()
# create an instance of UpsertCompanyLogoRequestAffiliate from a dict
upsert_company_logo_request_affiliate_from_dict = UpsertCompanyLogoRequestAffiliate.from_dict(upsert_company_logo_request_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


