# ReviewAnswerBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question_identifier** | **str** | Question identifier | 
**category** | **str** | Question category | 
**sort** | **int** | Sort key | 
**value** | **int** | Value | 

## Example

```python
from wink_sdk_booking.models.review_answer_booker import ReviewAnswerBooker

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewAnswerBooker from a JSON string
review_answer_booker_instance = ReviewAnswerBooker.from_json(json)
# print the JSON string representation of the object
print(ReviewAnswerBooker.to_json())

# convert the object into a dict
review_answer_booker_dict = review_answer_booker_instance.to_dict()
# create an instance of ReviewAnswerBooker from a dict
review_answer_booker_from_dict = ReviewAnswerBooker.from_dict(review_answer_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


