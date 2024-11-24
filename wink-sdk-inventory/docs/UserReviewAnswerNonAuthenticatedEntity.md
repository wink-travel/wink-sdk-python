# UserReviewAnswerNonAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Question category | 
**sort** | **int** | Sort key | 
**value** | **int** | Value | 

## Example

```python
from wink_sdk_inventory.models.user_review_answer_non_authenticated_entity import UserReviewAnswerNonAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of UserReviewAnswerNonAuthenticatedEntity from a JSON string
user_review_answer_non_authenticated_entity_instance = UserReviewAnswerNonAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(UserReviewAnswerNonAuthenticatedEntity.to_json())

# convert the object into a dict
user_review_answer_non_authenticated_entity_dict = user_review_answer_non_authenticated_entity_instance.to_dict()
# create an instance of UserReviewAnswerNonAuthenticatedEntity from a dict
user_review_answer_non_authenticated_entity_from_dict = UserReviewAnswerNonAuthenticatedEntity.from_dict(user_review_answer_non_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


