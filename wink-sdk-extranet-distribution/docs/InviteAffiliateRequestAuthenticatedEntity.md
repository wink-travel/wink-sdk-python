# InviteAffiliateRequestAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel_email** | **str** | The email of the property | 
**affiliate_email** | **str** | The email of the affiliate | 
**affiliate_name** | **str** | The name of the affiliate | 

## Example

```python
from wink_sdk_extranet_distribution.models.invite_affiliate_request_authenticated_entity import InviteAffiliateRequestAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of InviteAffiliateRequestAuthenticatedEntity from a JSON string
invite_affiliate_request_authenticated_entity_instance = InviteAffiliateRequestAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(InviteAffiliateRequestAuthenticatedEntity.to_json())

# convert the object into a dict
invite_affiliate_request_authenticated_entity_dict = invite_affiliate_request_authenticated_entity_instance.to_dict()
# create an instance of InviteAffiliateRequestAuthenticatedEntity from a dict
invite_affiliate_request_authenticated_entity_from_dict = InviteAffiliateRequestAuthenticatedEntity.from_dict(invite_affiliate_request_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


