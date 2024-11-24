# SubSubCountryAgent

Country sub sub division

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**ascii_name** | **str** |  | [optional] 
**geo_name_id** | **str** |  | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.sub_sub_country_agent import SubSubCountryAgent

# TODO update the JSON string below
json = "{}"
# create an instance of SubSubCountryAgent from a JSON string
sub_sub_country_agent_instance = SubSubCountryAgent.from_json(json)
# print the JSON string representation of the object
print(SubSubCountryAgent.to_json())

# convert the object into a dict
sub_sub_country_agent_dict = sub_sub_country_agent_instance.to_dict()
# create an instance of SubSubCountryAgent from a dict
sub_sub_country_agent_from_dict = SubSubCountryAgent.from_dict(sub_sub_country_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


