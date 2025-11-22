# PageChannelManagerProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[ChannelManagerProperty]**](ChannelManagerProperty.md) |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**SortObject**](SortObject.md) |  | [optional] 
**pageable** | [**PageableObject**](PageableObject.md) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_channel_manager.models.page_channel_manager_property import PageChannelManagerProperty

# TODO update the JSON string below
json = "{}"
# create an instance of PageChannelManagerProperty from a JSON string
page_channel_manager_property_instance = PageChannelManagerProperty.from_json(json)
# print the JSON string representation of the object
print(PageChannelManagerProperty.to_json())

# convert the object into a dict
page_channel_manager_property_dict = page_channel_manager_property_instance.to_dict()
# create an instance of PageChannelManagerProperty from a dict
page_channel_manager_property_from_dict = PageChannelManagerProperty.from_dict(page_channel_manager_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


