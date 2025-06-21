# SimpleAddressAgent

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
**country** | **str** | Country | [optional] [readonly] 
**full_address** | **str** | Address 1, Address 2, City, State, Postal / Zip code, Country | [optional] [readonly] 

## Example

```python
from wink_sdk_travel_agent.models.simple_address_agent import SimpleAddressAgent

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleAddressAgent from a JSON string
simple_address_agent_instance = SimpleAddressAgent.from_json(json)
# print the JSON string representation of the object
print(SimpleAddressAgent.to_json())

# convert the object into a dict
simple_address_agent_dict = simple_address_agent_instance.to_dict()
# create an instance of SimpleAddressAgent from a dict
simple_address_agent_from_dict = SimpleAddressAgent.from_dict(simple_address_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


