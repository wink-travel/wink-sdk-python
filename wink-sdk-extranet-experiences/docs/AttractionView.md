# AttractionView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**attraction** | [**Attraction**](Attraction.md) |  | 

## Example

```python
from wink_sdk_extranet_experiences.models.attraction_view import AttractionView

# TODO update the JSON string below
json = "{}"
# create an instance of AttractionView from a JSON string
attraction_view_instance = AttractionView.from_json(json)
# print the JSON string representation of the object
print(AttractionView.to_json())

# convert the object into a dict
attraction_view_dict = attraction_view_instance.to_dict()
# create an instance of AttractionView from a dict
attraction_view_from_dict = AttractionView.from_dict(attraction_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


