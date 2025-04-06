# InviteAffiliateRequestSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel_email** | **str** | The email of the property | 
**affiliate_email** | **str** | The email of the affiliate | 
**affiliate_name** | **str** | The name of the affiliate | 

## Example

```python
from wink_sdk_extranet_distribution.models.invite_affiliate_request_supplier import InviteAffiliateRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of InviteAffiliateRequestSupplier from a JSON string
invite_affiliate_request_supplier_instance = InviteAffiliateRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(InviteAffiliateRequestSupplier.to_json())

# convert the object into a dict
invite_affiliate_request_supplier_dict = invite_affiliate_request_supplier_instance.to_dict()
# create an instance of InviteAffiliateRequestSupplier from a dict
invite_affiliate_request_supplier_from_dict = InviteAffiliateRequestSupplier.from_dict(invite_affiliate_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


