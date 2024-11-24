# AuthenticatedUserSupplier

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
from wink_sdk_extranet_booking.models.authenticated_user_supplier import AuthenticatedUserSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatedUserSupplier from a JSON string
authenticated_user_supplier_instance = AuthenticatedUserSupplier.from_json(json)
# print the JSON string representation of the object
print(AuthenticatedUserSupplier.to_json())

# convert the object into a dict
authenticated_user_supplier_dict = authenticated_user_supplier_instance.to_dict()
# create an instance of AuthenticatedUserSupplier from a dict
authenticated_user_supplier_from_dict = AuthenticatedUserSupplier.from_dict(authenticated_user_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


