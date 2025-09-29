# MediaAuthorAttributionAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL to contributor | [optional] 
**name** | **str** | Name of contributor | 

## Example

```python
from wink_sdk_affiliate.models.media_author_attribution_agent import MediaAuthorAttributionAgent

# TODO update the JSON string below
json = "{}"
# create an instance of MediaAuthorAttributionAgent from a JSON string
media_author_attribution_agent_instance = MediaAuthorAttributionAgent.from_json(json)
# print the JSON string representation of the object
print(MediaAuthorAttributionAgent.to_json())

# convert the object into a dict
media_author_attribution_agent_dict = media_author_attribution_agent_instance.to_dict()
# create an instance of MediaAuthorAttributionAgent from a dict
media_author_attribution_agent_from_dict = MediaAuthorAttributionAgent.from_dict(media_author_attribution_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


