# AddressAuthenticatedEntity

Address information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** | Address line 1 | 
**address2** | **str** | Address line 2 | [optional] 
**state** | **str** | State | [optional] 
**postal_code** | **str** | Postal / zip code | [optional] 
**county** | **str** | County | [optional] 
**city** | [**GeoNameAuthenticatedEntity**](GeoNameAuthenticatedEntity.md) |  | 
**valid** | **bool** | Whether this address is considered valid by the system or not | [optional] [readonly] 
**full_address** | **str** | Address 1, Address 2, City, State, Postal / Zip code, Country | [optional] [readonly] 

## Example

```python
from wink_sdk_user_settings.models.address_authenticated_entity import AddressAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AddressAuthenticatedEntity from a JSON string
address_authenticated_entity_instance = AddressAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(AddressAuthenticatedEntity.to_json())

# convert the object into a dict
address_authenticated_entity_dict = address_authenticated_entity_instance.to_dict()
# create an instance of AddressAuthenticatedEntity from a dict
address_authenticated_entity_from_dict = AddressAuthenticatedEntity.from_dict(address_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


