# OnlinePresenceAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | List of all active accounts that could be used for selling or seeing a company&#39;s reach. | 
**identifier** | **str** | The url, account name or phone number that identifies this user with the specified network. | 
**audiences** | **List[str]** | The type of audience you have on this network. | [optional] 
**audience_size** | **int** | The size of your audience. | [optional] 
**sort** | **int** | How you would like to order your accounts. | [optional] 
**disabled** | **bool** | The url, account name or phone number that identifies this user with the specified network. | 

## Example

```python
from wink_sdk_affiliate.models.online_presence_agent import OnlinePresenceAgent

# TODO update the JSON string below
json = "{}"
# create an instance of OnlinePresenceAgent from a JSON string
online_presence_agent_instance = OnlinePresenceAgent.from_json(json)
# print the JSON string representation of the object
print(OnlinePresenceAgent.to_json())

# convert the object into a dict
online_presence_agent_dict = online_presence_agent_instance.to_dict()
# create an instance of OnlinePresenceAgent from a dict
online_presence_agent_from_dict = OnlinePresenceAgent.from_dict(online_presence_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


