# OnlinePresenceNonAuthenticatedEntity

Online presence of account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | List of all active accounts that could be used for selling or seeing a company&#39;s reach. | 
**identifier** | **str** | The url, account name or phone number that identifies this user with the specified network. | 
**audiences** | **List[str]** | The url, account name or phone number that identifies this user with the specified network. | [optional] 
**audience_size** | **int** | The url, account name or phone number that identifies this user with the specified network. | 

## Example

```python
from wink_sdk_affiliate_winklinks.models.online_presence_non_authenticated_entity import OnlinePresenceNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of OnlinePresenceNonAuthenticatedEntity from a JSON string
online_presence_non_authenticated_entity_instance = OnlinePresenceNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(OnlinePresenceNonAuthenticatedEntity.to_json())

# convert the object into a dict
online_presence_non_authenticated_entity_dict = online_presence_non_authenticated_entity_instance.to_dict()
# create an instance of OnlinePresenceNonAuthenticatedEntity from a dict
online_presence_non_authenticated_entity_from_dict = OnlinePresenceNonAuthenticatedEntity.from_dict(online_presence_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


