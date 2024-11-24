# ContactAuthenticatedEntity

Associate a contact person for this blocking (if applicable).

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
from wink_sdk_booking.models.contact_authenticated_entity import ContactAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ContactAuthenticatedEntity from a JSON string
contact_authenticated_entity_instance = ContactAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ContactAuthenticatedEntity.to_json())

# convert the object into a dict
contact_authenticated_entity_dict = contact_authenticated_entity_instance.to_dict()
# create an instance of ContactAuthenticatedEntity from a dict
contact_authenticated_entity_from_dict = ContactAuthenticatedEntity.from_dict(contact_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


