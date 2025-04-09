# SocialAffiliate

Social network

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of social network. | [optional] 
**location** | **str** | URL or social network identifier to social network profile | [optional] 

## Example

```python
from wink_sdk_affiliate_sales_channel.models.social_affiliate import SocialAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of SocialAffiliate from a JSON string
social_affiliate_instance = SocialAffiliate.from_json(json)
# print the JSON string representation of the object
print(SocialAffiliate.to_json())

# convert the object into a dict
social_affiliate_dict = social_affiliate_instance.to_dict()
# create an instance of SocialAffiliate from a dict
social_affiliate_from_dict = SocialAffiliate.from_dict(social_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


