# SimpleDescriptionAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Use as title or short text description | 
**description** | **str** | Longer text description | 
**language** | **str** | Indicate which language this description is written in. | [default to 'en']
**creator** | **str** | Whether it was user or system generated. | [optional] [default to 'USER']
**md5_content_hash** | **str** | The md5 hash of the name, description and language. | [optional] 
**hash_mismatch** | **bool** |  | [optional] [readonly] 

## Example

```python
from wink_sdk_affiliate.models.simple_description_agent import SimpleDescriptionAgent

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleDescriptionAgent from a JSON string
simple_description_agent_instance = SimpleDescriptionAgent.from_json(json)
# print the JSON string representation of the object
print(SimpleDescriptionAgent.to_json())

# convert the object into a dict
simple_description_agent_dict = simple_description_agent_instance.to_dict()
# create an instance of SimpleDescriptionAgent from a dict
simple_description_agent_from_dict = SimpleDescriptionAgent.from_dict(simple_description_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


