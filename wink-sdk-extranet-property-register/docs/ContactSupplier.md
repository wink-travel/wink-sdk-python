# ContactSupplier


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
from wink_sdk_extranet_property_register.models.contact_supplier import ContactSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ContactSupplier from a JSON string
contact_supplier_instance = ContactSupplier.from_json(json)
# print the JSON string representation of the object
print(ContactSupplier.to_json())

# convert the object into a dict
contact_supplier_dict = contact_supplier_instance.to_dict()
# create an instance of ContactSupplier from a dict
contact_supplier_from_dict = ContactSupplier.from_dict(contact_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


