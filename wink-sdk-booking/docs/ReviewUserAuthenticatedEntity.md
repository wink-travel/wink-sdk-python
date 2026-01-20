# ReviewUserAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_identifier** | **UUID** | User identifier | [optional] 
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last name | [optional] 
**email** | **str** | Email | [optional] 
**telephone** | **str** | Telephone | [optional] 
**full_name** | **str** | Full name | [optional] 

## Example

```python
from wink_sdk_booking.models.review_user_authenticated_entity import ReviewUserAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewUserAuthenticatedEntity from a JSON string
review_user_authenticated_entity_instance = ReviewUserAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ReviewUserAuthenticatedEntity.to_json())

# convert the object into a dict
review_user_authenticated_entity_dict = review_user_authenticated_entity_instance.to_dict()
# create an instance of ReviewUserAuthenticatedEntity from a dict
review_user_authenticated_entity_from_dict = ReviewUserAuthenticatedEntity.from_dict(review_user_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


