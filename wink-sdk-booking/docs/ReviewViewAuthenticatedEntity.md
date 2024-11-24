# ReviewViewAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**review** | [**ReviewAuthenticatedEntity**](ReviewAuthenticatedEntity.md) |  | 

## Example

```python
from wink_sdk_booking.models.review_view_authenticated_entity import ReviewViewAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewViewAuthenticatedEntity from a JSON string
review_view_authenticated_entity_instance = ReviewViewAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ReviewViewAuthenticatedEntity.to_json())

# convert the object into a dict
review_view_authenticated_entity_dict = review_view_authenticated_entity_instance.to_dict()
# create an instance of ReviewViewAuthenticatedEntity from a dict
review_view_authenticated_entity_from_dict = ReviewViewAuthenticatedEntity.from_dict(review_view_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


