# OpenGraphMediaAffiliate

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
from wink_sdk_affiliate_inventory.models.open_graph_media_affiliate import OpenGraphMediaAffiliate

# TODO update the JSON string below
json = "{}"
# create an instance of OpenGraphMediaAffiliate from a JSON string
open_graph_media_affiliate_instance = OpenGraphMediaAffiliate.from_json(json)
# print the JSON string representation of the object
print(OpenGraphMediaAffiliate.to_json())

# convert the object into a dict
open_graph_media_affiliate_dict = open_graph_media_affiliate_instance.to_dict()
# create an instance of OpenGraphMediaAffiliate from a dict
open_graph_media_affiliate_from_dict = OpenGraphMediaAffiliate.from_dict(open_graph_media_affiliate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


