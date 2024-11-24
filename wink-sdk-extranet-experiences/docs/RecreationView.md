# RecreationView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**recreation** | [**Recreation**](Recreation.md) |  | [optional] 
**featured_image_identifier** | **str** |  | [optional] 

## Example

```python
from wink_sdk_extranet_experiences.models.recreation_view import RecreationView

# TODO update the JSON string below
json = "{}"
# create an instance of RecreationView from a JSON string
recreation_view_instance = RecreationView.from_json(json)
# print the JSON string representation of the object
print(RecreationView.to_json())

# convert the object into a dict
recreation_view_dict = recreation_view_instance.to_dict()
# create an instance of RecreationView from a dict
recreation_view_from_dict = RecreationView.from_dict(recreation_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


