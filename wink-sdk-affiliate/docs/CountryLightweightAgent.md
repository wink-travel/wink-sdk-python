# CountryLightweightAgent

Country

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso** | **str** | ISO code | [optional] 
**name** | **str** | Country name | [optional] 
**capital** | **str** | Country capital | [optional] 
**continent** | **str** | Continent code | [optional] 
**currency_code** | **str** | Currency code | [optional] 
**currency_name** | **str** | Currency name | [optional] 
**geo_name_id** | **str** | Country GeoNames identifier | [optional] 

## Example

```python
from wink_sdk_affiliate.models.country_lightweight_agent import CountryLightweightAgent

# TODO update the JSON string below
json = "{}"
# create an instance of CountryLightweightAgent from a JSON string
country_lightweight_agent_instance = CountryLightweightAgent.from_json(json)
# print the JSON string representation of the object
print(CountryLightweightAgent.to_json())

# convert the object into a dict
country_lightweight_agent_dict = country_lightweight_agent_instance.to_dict()
# create an instance of CountryLightweightAgent from a dict
country_lightweight_agent_from_dict = CountryLightweightAgent.from_dict(country_lightweight_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


