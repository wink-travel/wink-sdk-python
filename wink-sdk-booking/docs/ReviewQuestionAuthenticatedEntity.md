# ReviewQuestionAuthenticatedEntity

Questions to be answered by booker

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**sort** | **int** |  | [optional] 
**options** | [**List[ReviewAnswerOptionAuthenticatedEntity]**](ReviewAnswerOptionAuthenticatedEntity.md) |  | [optional] 

## Example

```python
from wink_sdk_booking.models.review_question_authenticated_entity import ReviewQuestionAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewQuestionAuthenticatedEntity from a JSON string
review_question_authenticated_entity_instance = ReviewQuestionAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ReviewQuestionAuthenticatedEntity.to_json())

# convert the object into a dict
review_question_authenticated_entity_dict = review_question_authenticated_entity_instance.to_dict()
# create an instance of ReviewQuestionAuthenticatedEntity from a dict
review_question_authenticated_entity_from_dict = ReviewQuestionAuthenticatedEntity.from_dict(review_question_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


