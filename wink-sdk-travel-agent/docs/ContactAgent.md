# ContactAgent

Array of emergency contact information for the customer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | Contact first name | [optional] 
**last_name** | **str** | Contact last name | [optional] 
**email** | **str** | Contact E-mail | [optional] 
**secondary_email** | **str** | Contact secondary Email | [optional] 
**phone_number** | **str** | Contact phone number | [optional] 
**full_name** | **str** | First and last name | [optional] [readonly] 
**summary** | **str** | Summary | [optional] [readonly] 

## Example

```python
from wink_sdk_travel_agent.models.contact_agent import ContactAgent

# TODO update the JSON string below
json = "{}"
# create an instance of ContactAgent from a JSON string
contact_agent_instance = ContactAgent.from_json(json)
# print the JSON string representation of the object
print(ContactAgent.to_json())

# convert the object into a dict
contact_agent_dict = contact_agent_instance.to_dict()
# create an instance of ContactAgent from a dict
contact_agent_from_dict = ContactAgent.from_dict(contact_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


