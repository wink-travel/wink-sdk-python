# ManualPropertyRegistrationRequestSupplier

Manual property registration request body

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique hotel trade name. The hotel name must be unique. If there are multiple hotels with the same name, we recommend appending destination to the name. [Verify uniqueness here](#operation/isHotelNameUnique). | 
**local_name** | **str** | Local name of the hotel as it is referred to in the local language. | 
**address** | [**UpsertAddressRequestSupplier**](UpsertAddressRequestSupplier.md) | Property address. | 
**reservation** | [**ContactSupplier**](ContactSupplier.md) | Reservation desk information. | 
**revenue** | [**ContactSupplier**](ContactSupplier.md) | Revenue information. | 
**marketing** | [**ContactSupplier**](ContactSupplier.md) | Marketing information. | 
**agreement_accepted** | **bool** | Agreement accepted by legal signer. | [default to True]

## Example

```python
from wink_sdk_extranet_property_register.models.manual_property_registration_request_supplier import ManualPropertyRegistrationRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of ManualPropertyRegistrationRequestSupplier from a JSON string
manual_property_registration_request_supplier_instance = ManualPropertyRegistrationRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(ManualPropertyRegistrationRequestSupplier.to_json())

# convert the object into a dict
manual_property_registration_request_supplier_dict = manual_property_registration_request_supplier_instance.to_dict()
# create an instance of ManualPropertyRegistrationRequestSupplier from a dict
manual_property_registration_request_supplier_from_dict = ManualPropertyRegistrationRequestSupplier.from_dict(manual_property_registration_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


