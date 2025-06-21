# LocalizedDescriptionAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Longer text description | 
**language** | **str** | Indicate which language this description is written in. | [default to 'en']
**creator** | **str** | Whether it was user or system generated. | [optional] [default to 'USER']
**md5_content_hash** | **str** | The md5 hash of the name, description and language. | [optional] 
**hash_mismatch** | **bool** |  | [optional] [readonly] 

## Example

```python
from wink_sdk_travel_agent.models.localized_description_agent import LocalizedDescriptionAgent

# TODO update the JSON string below
json = "{}"
# create an instance of LocalizedDescriptionAgent from a JSON string
localized_description_agent_instance = LocalizedDescriptionAgent.from_json(json)
# print the JSON string representation of the object
print(LocalizedDescriptionAgent.to_json())

# convert the object into a dict
localized_description_agent_dict = localized_description_agent_instance.to_dict()
# create an instance of LocalizedDescriptionAgent from a dict
localized_description_agent_from_dict = LocalizedDescriptionAgent.from_dict(localized_description_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


