# ReviewTemplateAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**booking_identifier** | **str** | Booking ID to review | 
**hotel_identifier** | **str** | Hotel ID to review | 
**hotel_name** | **str** | Hotel name to review | 
**user_identifier** | **str** | User ID doing the reviewing | 
**questions** | [**List[ReviewQuestionAuthenticatedEntity]**](ReviewQuestionAuthenticatedEntity.md) |  | 

## Example

```python
from wink_sdk_booking.models.review_template_authenticated_entity import ReviewTemplateAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewTemplateAuthenticatedEntity from a JSON string
review_template_authenticated_entity_instance = ReviewTemplateAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ReviewTemplateAuthenticatedEntity.to_json())

# convert the object into a dict
review_template_authenticated_entity_dict = review_template_authenticated_entity_instance.to_dict()
# create an instance of ReviewTemplateAuthenticatedEntity from a dict
review_template_authenticated_entity_from_dict = ReviewTemplateAuthenticatedEntity.from_dict(review_template_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


