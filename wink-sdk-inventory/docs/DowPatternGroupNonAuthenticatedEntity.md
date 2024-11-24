# DowPatternGroupNonAuthenticatedEntity

Indicate which days this blocking is open.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mon** | **bool** | Set to &#x60;true&#x60; to enable Monday. | [optional] 
**tue** | **bool** | Set to &#x60;true&#x60; to enable Tuesday. | [optional] 
**wed** | **bool** | Set to &#x60;true&#x60; to enable Wednesday. | [optional] 
**thu** | **bool** | Set to &#x60;true&#x60; to enable Thursday. | [optional] 
**fri** | **bool** | Set to &#x60;true&#x60; to enable Friday. | [optional] 
**sat** | **bool** | Set to &#x60;true&#x60; to enable Saturday. | [optional] 
**sun** | **bool** | Set to &#x60;true&#x60; to enable Sunday. | [optional] 
**disabled** | **bool** | Convenience property to quickly determine if this existing object has any active days enabled. | [optional] 

## Example

```python
from wink_sdk_inventory.models.dow_pattern_group_non_authenticated_entity import DowPatternGroupNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of DowPatternGroupNonAuthenticatedEntity from a JSON string
dow_pattern_group_non_authenticated_entity_instance = DowPatternGroupNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(DowPatternGroupNonAuthenticatedEntity.to_json())

# convert the object into a dict
dow_pattern_group_non_authenticated_entity_dict = dow_pattern_group_non_authenticated_entity_instance.to_dict()
# create an instance of DowPatternGroupNonAuthenticatedEntity from a dict
dow_pattern_group_non_authenticated_entity_from_dict = DowPatternGroupNonAuthenticatedEntity.from_dict(dow_pattern_group_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


