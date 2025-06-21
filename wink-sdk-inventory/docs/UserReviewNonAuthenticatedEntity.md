# UserReviewNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**review_by** | **str** | User details of creator of booking. | [optional] 
**reviewed_on** | **datetime** | Date of review. | [optional] 
**average_score** | **float** | Total points divided by number of questions. | [optional] 
**answers** | [**List[UserReviewAnswerNonAuthenticatedEntity]**](UserReviewAnswerNonAuthenticatedEntity.md) |  | [optional] 
**response_from_hotel** | **str** | Property can response to traveler review. Response goes on public review profile and can be seen by others. | [optional] 
**image_identifier** | **str** | Reviewer can upload her best picture from the property. Cloudinary image identifier. | [optional] 
**review** | **str** | Free text record created by traveler | [optional] 
**likes** | **int** | List of member identifiers who liked the reviewual review | [optional] 

## Example

```python
from wink_sdk_inventory.models.user_review_non_authenticated_entity import UserReviewNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of UserReviewNonAuthenticatedEntity from a JSON string
user_review_non_authenticated_entity_instance = UserReviewNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(UserReviewNonAuthenticatedEntity.to_json())

# convert the object into a dict
user_review_non_authenticated_entity_dict = user_review_non_authenticated_entity_instance.to_dict()
# create an instance of UserReviewNonAuthenticatedEntity from a dict
user_review_non_authenticated_entity_from_dict = UserReviewNonAuthenticatedEntity.from_dict(user_review_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


