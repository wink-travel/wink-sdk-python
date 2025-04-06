# OpenGraphMediaNonAuthenticatedEntity

The media list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The image url | 
**secure_url** | **str** | The secure url | [optional] 
**type** | **str** | Image content type | [optional] 
**width** | **str** | Image width | [optional] 
**height** | **str** | Image height | [optional] 
**alt** | **str** | Alt text | [optional] 

## Example

```python
from wink_sdk_affiliate_winklinks.models.open_graph_media_non_authenticated_entity import OpenGraphMediaNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of OpenGraphMediaNonAuthenticatedEntity from a JSON string
open_graph_media_non_authenticated_entity_instance = OpenGraphMediaNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(OpenGraphMediaNonAuthenticatedEntity.to_json())

# convert the object into a dict
open_graph_media_non_authenticated_entity_dict = open_graph_media_non_authenticated_entity_instance.to_dict()
# create an instance of OpenGraphMediaNonAuthenticatedEntity from a dict
open_graph_media_non_authenticated_entity_from_dict = OpenGraphMediaNonAuthenticatedEntity.from_dict(open_graph_media_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


