# SubmitReviewRequestAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answers** | [**List[SubmitReviewAnswerAuthenticatedEntity]**](SubmitReviewAnswerAuthenticatedEntity.md) |  | 
**message_from_guest** | **str** | Private message from guest to the hotel. Is not displayed on property profile. | [optional] 
**image_identifier** | **str** | Reviewer can upload her best picture from the property. Cloudinary image identifier. | [optional] 
**text** | **str** | Free text record created by traveler | [optional] 
**room_number** | **str** | Guest&#39;s room number during their stay. | [optional] 
**room_rating** | **int** | Guest&#39;s room rating | [optional] 

## Example

```python
from wink_sdk_booking.models.submit_review_request_authenticated_entity import SubmitReviewRequestAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitReviewRequestAuthenticatedEntity from a JSON string
submit_review_request_authenticated_entity_instance = SubmitReviewRequestAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(SubmitReviewRequestAuthenticatedEntity.to_json())

# convert the object into a dict
submit_review_request_authenticated_entity_dict = submit_review_request_authenticated_entity_instance.to_dict()
# create an instance of SubmitReviewRequestAuthenticatedEntity from a dict
submit_review_request_authenticated_entity_from_dict = SubmitReviewRequestAuthenticatedEntity.from_dict(submit_review_request_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


