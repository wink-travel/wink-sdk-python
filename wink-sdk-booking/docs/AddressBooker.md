# AddressBooker

Address information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** | Address line 1 | 
**address2** | **str** | Address line 2 | [optional] 
**state** | **str** | State | [optional] 
**postal_code** | **str** | Postal / zip code | [optional] 
**county** | **str** | County | [optional] 
**city** | [**GeoNameBooker**](GeoNameBooker.md) |  | 
**valid** | **bool** | Whether this address is considered valid by the system or not | [optional] [readonly] 
**full_address** | **str** | Address 1, Address 2, City, State, Postal / Zip code, Country | [optional] [readonly] 

## Example

```python
from wink_sdk_booking.models.address_booker import AddressBooker

# TODO update the JSON string below
json = "{}"
# create an instance of AddressBooker from a JSON string
address_booker_instance = AddressBooker.from_json(json)
# print the JSON string representation of the object
print(AddressBooker.to_json())

# convert the object into a dict
address_booker_dict = address_booker_instance.to_dict()
# create an instance of AddressBooker from a dict
address_booker_from_dict = AddressBooker.from_dict(address_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


