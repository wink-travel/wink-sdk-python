# ManagingEntityManagerAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | User email | 
**status** | **str** | Contact phone number | [optional] 
**user_identifier** | **UUID** | User identifier | [optional] 
**first_name** | **str** | Contact first name | [optional] 
**last_name** | **str** | Contact last name | [optional] 
**secondary_email** | **str** | Contact secondary Email | [optional] 
**phone_number** | **str** | Contact phone number | [optional] 
**profile_picture** | [**SimpleMultimediaAffiliate**](SimpleMultimediaAffiliate.md) | Profile picture is available | [optional] 
**owner** | **bool** | Account owner | [optional] 
**roles** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.managing_entity_manager_agent import ManagingEntityManagerAgent

# TODO update the JSON string below
json = "{}"
# create an instance of ManagingEntityManagerAgent from a JSON string
managing_entity_manager_agent_instance = ManagingEntityManagerAgent.from_json(json)
# print the JSON string representation of the object
print(ManagingEntityManagerAgent.to_json())

# convert the object into a dict
managing_entity_manager_agent_dict = managing_entity_manager_agent_instance.to_dict()
# create an instance of ManagingEntityManagerAgent from a dict
managing_entity_manager_agent_from_dict = ManagingEntityManagerAgent.from_dict(managing_entity_manager_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


