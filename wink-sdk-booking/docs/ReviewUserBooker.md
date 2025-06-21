# ReviewUserBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_identifier** | **str** | User identifier | [optional] 
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last name | [optional] 
**email** | **str** | Email | [optional] 
**telephone** | **str** | Telephone | [optional] 
**full_name** | **str** | Full name | [optional] 

## Example

```python
from wink_sdk_booking.models.review_user_booker import ReviewUserBooker

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewUserBooker from a JSON string
review_user_booker_instance = ReviewUserBooker.from_json(json)
# print the JSON string representation of the object
print(ReviewUserBooker.to_json())

# convert the object into a dict
review_user_booker_dict = review_user_booker_instance.to_dict()
# create an instance of ReviewUserBooker from a dict
review_user_booker_from_dict = ReviewUserBooker.from_dict(review_user_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


