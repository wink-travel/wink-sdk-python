# AuthenticatedUserSupplierDetails

The authenticated user ID that made the request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_identifier** | **str** | User identifier | [optional] 
**first_name** | **str** | First name | 
**last_name** | **str** | Last name | 
**email** | **str** | Email | 
**full_name** | **str** | Full name | [optional] [readonly] 

## Example

```python
from wink_sdk_extranet_distribution.models.authenticated_user_supplier_details import AuthenticatedUserSupplierDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatedUserSupplierDetails from a JSON string
authenticated_user_supplier_details_instance = AuthenticatedUserSupplierDetails.from_json(json)
# print the JSON string representation of the object
print(AuthenticatedUserSupplierDetails.to_json())

# convert the object into a dict
authenticated_user_supplier_details_dict = authenticated_user_supplier_details_instance.to_dict()
# create an instance of AuthenticatedUserSupplierDetails from a dict
authenticated_user_supplier_details_from_dict = AuthenticatedUserSupplierDetails.from_dict(authenticated_user_supplier_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


