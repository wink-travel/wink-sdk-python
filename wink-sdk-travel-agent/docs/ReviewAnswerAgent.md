# ReviewAnswerAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question_identifier** | **UUID** | Question identifier | 
**category** | **str** | Question category | 
**sort** | **int** | Sort key | 
**value** | **int** | Value | 

## Example

```python
from wink_sdk_travel_agent.models.review_answer_agent import ReviewAnswerAgent

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewAnswerAgent from a JSON string
review_answer_agent_instance = ReviewAnswerAgent.from_json(json)
# print the JSON string representation of the object
print(ReviewAnswerAgent.to_json())

# convert the object into a dict
review_answer_agent_dict = review_answer_agent_instance.to_dict()
# create an instance of ReviewAnswerAgent from a dict
review_answer_agent_from_dict = ReviewAnswerAgent.from_dict(review_answer_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


