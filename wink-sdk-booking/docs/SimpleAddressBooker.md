# SimpleAddressBooker

Address information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address1** | **str** | Address line 1 | 
**address2** | **str** | Address line 2 | [optional] 
**state** | **str** | State | [optional] 
**postal_code** | **str** | Postal / zip code | 
**county** | **str** | County | [optional] 
**city** | **str** | City name | 
**country_code** | **str** | Country | 
**full_address** | **str** | Address 1, Address 2, City, State, Postal / Zip code, Country | [optional] [readonly] 

## Example

```python
from wink_sdk_booking.models.simple_address_booker import SimpleAddressBooker

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleAddressBooker from a JSON string
simple_address_booker_instance = SimpleAddressBooker.from_json(json)
# print the JSON string representation of the object
print(SimpleAddressBooker.to_json())

# convert the object into a dict
simple_address_booker_dict = simple_address_booker_instance.to_dict()
# create an instance of SimpleAddressBooker from a dict
simple_address_booker_from_dict = SimpleAddressBooker.from_dict(simple_address_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


