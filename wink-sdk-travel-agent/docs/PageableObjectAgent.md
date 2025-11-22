# PageableObjectAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | [optional] 
**paged** | **bool** |  | [optional] 
**page_number** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**sort** | [**SortObjectAgent**](SortObjectAgent.md) |  | [optional] 
**unpaged** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_travel_agent.models.pageable_object_agent import PageableObjectAgent

# TODO update the JSON string below
json = "{}"
# create an instance of PageableObjectAgent from a JSON string
pageable_object_agent_instance = PageableObjectAgent.from_json(json)
# print the JSON string representation of the object
print(PageableObjectAgent.to_json())

# convert the object into a dict
pageable_object_agent_dict = pageable_object_agent_instance.to_dict()
# create an instance of PageableObjectAgent from a dict
pageable_object_agent_from_dict = PageableObjectAgent.from_dict(pageable_object_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


