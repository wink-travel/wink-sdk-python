# SubmitReviewAnswerAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question_identifier** | **str** | Question identifier | 
**category** | **str** | Question category | 
**sort** | **int** | Sort key | 
**value** | **int** | Value | 

## Example

```python
from wink_sdk_booking.models.submit_review_answer_authenticated_entity import SubmitReviewAnswerAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitReviewAnswerAuthenticatedEntity from a JSON string
submit_review_answer_authenticated_entity_instance = SubmitReviewAnswerAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SubmitReviewAnswerAuthenticatedEntity.to_json())

# convert the object into a dict
submit_review_answer_authenticated_entity_dict = submit_review_answer_authenticated_entity_instance.to_dict()
# create an instance of SubmitReviewAnswerAuthenticatedEntity from a dict
submit_review_answer_authenticated_entity_from_dict = SubmitReviewAnswerAuthenticatedEntity.from_dict(submit_review_answer_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


