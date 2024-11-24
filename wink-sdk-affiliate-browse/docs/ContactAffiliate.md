# ContactAffiliate

Contact details for reservations desk

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
from wink_sdk_affiliate_browse.models.contact_affiliate import ContactAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of ContactAffiliate from a JSON string
contact_affiliate_instance = ContactAffiliate.from_json(json)
# print the JSON string representation of the object
print(ContactAffiliate.to_json())

# convert the object into a dict
contact_affiliate_dict = contact_affiliate_instance.to_dict()
# create an instance of ContactAffiliate from a dict
contact_affiliate_from_dict = ContactAffiliate.from_dict(contact_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


