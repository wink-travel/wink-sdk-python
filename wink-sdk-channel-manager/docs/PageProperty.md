# PageProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_elements** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[ModelProperty]**](ModelProperty.md) |  | [optional] 
**number** | **int** |  | [optional] 
**sort** | [**List[SortObject]**](SortObject.md) |  | [optional] 
**number_of_elements** | **int** |  | [optional] 
**pageable** | [**PageableObject**](PageableObject.md) |  | [optional] 
**first** | **bool** |  | [optional] 
**last** | **bool** |  | [optional] 
**empty** | **bool** |  | [optional] 

## Example

```python
from wink_sdk_channel_manager.models.page_property import PageProperty

# TODO update the JSON string below
json = "{}"
# create an instance of PageProperty from a JSON string
page_property_instance = PageProperty.from_json(json)
# print the JSON string representation of the object
print(PageProperty.to_json())

# convert the object into a dict
page_property_dict = page_property_instance.to_dict()
# create an instance of PageProperty from a dict
page_property_from_dict = PageProperty.from_dict(page_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


