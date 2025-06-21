# ReviewLightweightBooker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique review identifier identifying this record. | [optional] 
**booking_identifier** | **str** | Booking identifier identifier booking this review is associated with. | [optional] 
**hotel_identifier** | **str** | Hotel identifier this booking is associated with. | [optional] 
**user** | [**ReviewUserBooker**](ReviewUserBooker.md) | User details of creator of booking. | [optional] 
**review_date** | **datetime** | Date of review. | [optional] 
**average_score** | **float** | Total points divided by number of questions. | [optional] 
**answers** | [**List[ReviewAnswerBooker]**](ReviewAnswerBooker.md) |  | [optional] 
**message_from_guest** | **str** | Private message from guest to the hotel. Is not displayed on property profile. | [optional] 
**response_from_hotel** | **str** | Property can response to traveler review. Response goes on public review profile and can be seen by others. | [optional] 
**image_identifier** | **str** | Reviewer can upload her best picture from the property. Cloudinary image identifier. | [optional] 
**text** | **str** | Free text record created by traveler | [optional] 
**approved_text** | **bool** | Hotel allows the review text to be displayed as part of their profile. | [optional] 
**approved_image** | **bool** | Hotel allows the user-generated image to be displayed as part of their profile. | [optional] 
**likes** | **List[str]** |  | [optional] 
**room_number** | **str** | Guest&#39;s room number during their stay. | [optional] 
**room_rating** | **int** | Guest&#39;s room rating | [optional] 
**responded** | **bool** | Returns true if property has responded to the review given by the guest. | [optional] [default to False]

## Example

```python
from wink_sdk_booking.models.review_lightweight_booker import ReviewLightweightBooker

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewLightweightBooker from a JSON string
review_lightweight_booker_instance = ReviewLightweightBooker.from_json(json)
# print the JSON string representation of the object
print(ReviewLightweightBooker.to_json())

# convert the object into a dict
review_lightweight_booker_dict = review_lightweight_booker_instance.to_dict()
# create an instance of ReviewLightweightBooker from a dict
review_lightweight_booker_from_dict = ReviewLightweightBooker.from_dict(review_lightweight_booker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


