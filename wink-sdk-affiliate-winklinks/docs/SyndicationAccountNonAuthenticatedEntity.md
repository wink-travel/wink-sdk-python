# SyndicationAccountNonAuthenticatedEntity

A publishable company object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | The company ID | 
**url_name** | **str** | The company url name | 
**name** | **str** | The company name | 
**description** | **str** | The company description | 
**member_since** | **date** | When the company account was created | 
**logo** | [**SimpleMultimediaNonAuthenticatedEntity**](SimpleMultimediaNonAuthenticatedEntity.md) |  | [optional] 
**online_presence** | [**List[OnlinePresenceNonAuthenticatedEntity]**](OnlinePresenceNonAuthenticatedEntity.md) |  | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.syndication_account_non_authenticated_entity import SyndicationAccountNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SyndicationAccountNonAuthenticatedEntity from a JSON string
syndication_account_non_authenticated_entity_instance = SyndicationAccountNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SyndicationAccountNonAuthenticatedEntity.to_json())

# convert the object into a dict
syndication_account_non_authenticated_entity_dict = syndication_account_non_authenticated_entity_instance.to_dict()
# create an instance of SyndicationAccountNonAuthenticatedEntity from a dict
syndication_account_non_authenticated_entity_from_dict = SyndicationAccountNonAuthenticatedEntity.from_dict(syndication_account_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


