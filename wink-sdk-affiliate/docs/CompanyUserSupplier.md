# CompanyUserSupplier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | User email | 
**status** | **str** | Contact phone number | [optional] 
**user_identifier** | **str** | User identifier | [optional] 
**first_name** | **str** | Contact first name | [optional] 
**last_name** | **str** | Contact last name | [optional] 
**secondary_email** | **str** | Contact secondary Email | [optional] 
**phone_number** | **str** | Contact phone number | [optional] 
**profile_picture_url** | **str** | Profile picture is available | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from wink_sdk_affiliate.models.company_user_supplier import CompanyUserSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyUserSupplier from a JSON string
company_user_supplier_instance = CompanyUserSupplier.from_json(json)
# print the JSON string representation of the object
print(CompanyUserSupplier.to_json())

# convert the object into a dict
company_user_supplier_dict = company_user_supplier_instance.to_dict()
# create an instance of CompanyUserSupplier from a dict
company_user_supplier_from_dict = CompanyUserSupplier.from_dict(company_user_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


