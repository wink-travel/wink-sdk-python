# IntelligentPropertyRegistrationRequestSupplier

The values here override, or help complete, the lead data that is already in the database. Most times, it will be the address from Google that cannot be properly mapped and will need some human intervention.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_in_english** | **str** | Unique hotel trade name. The hotel name must be unique. If there are multiple hotels with the same name, we recommend appending destination to the name. [Verify uniqueness here](#operation/isHotelNameUnique). | 
**name_in_local_language** | **str** | Local name of the hotel as it is referred to in the local language. | [optional] 
**address** | [**UpsertAddressRequestSupplier**](UpsertAddressRequestSupplier.md) | Property address. | 
**address_local** | [**SimpleAddressSupplier**](SimpleAddressSupplier.md) | Property local address. | [optional] 
**location** | [**GeoJsonPointSupplier**](GeoJsonPointSupplier.md) | Reservation desk information. | 
**multimedia_identifiers** | **List[object]** |  | [optional] 
**approve_rating** | **bool** | Whether to approve the incoming rating from Google Places | [optional] [default to False]
**website** | **str** | Website of property | [optional] 
**reservation** | [**ContactSupplier**](ContactSupplier.md) | Reservation desk information. | 
**revenue** | [**ContactSupplier**](ContactSupplier.md) | Revenue information. | 
**marketing** | [**ContactSupplier**](ContactSupplier.md) | Marketing information. | 
**agreement_accepted** | **bool** | Agreement accepted by legal signer. | [default to True]
**descriptions** | **List[object]** |  | [optional] 
**profile** | [**IntelligentProfileSupplier**](IntelligentProfileSupplier.md) | Property profile. | 
**hotel_amenity_codes** | **List[object]** |  | [optional] 
**property_accessibility_codes** | **List[object]** |  | [optional] 
**property_security_codes** | **List[object]** |  | [optional] 

## Example

```python
from wink_sdk_extranet_property_register.models.intelligent_property_registration_request_supplier import IntelligentPropertyRegistrationRequestSupplier

# TODO update the JSON string below
json = "{}"
# create an instance of IntelligentPropertyRegistrationRequestSupplier from a JSON string
intelligent_property_registration_request_supplier_instance = IntelligentPropertyRegistrationRequestSupplier.from_json(json)
# print the JSON string representation of the object
print(IntelligentPropertyRegistrationRequestSupplier.to_json())

# convert the object into a dict
intelligent_property_registration_request_supplier_dict = intelligent_property_registration_request_supplier_instance.to_dict()
# create an instance of IntelligentPropertyRegistrationRequestSupplier from a dict
intelligent_property_registration_request_supplier_from_dict = IntelligentPropertyRegistrationRequestSupplier.from_dict(intelligent_property_registration_request_supplier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


