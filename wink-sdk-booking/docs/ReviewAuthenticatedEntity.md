# ReviewAuthenticatedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Document UUID | [optional] 
**created_date** | **datetime** | Datetime this record was first created | [optional] 
**last_update** | **datetime** | Datetime this record was last updated | [optional] 
**version** | **int** | Version property that shows how many times this document has been persisted. Document will not persist if the version property is less than current version property in the system. Result in an optimistic locking exception. | [optional] 
**booking_identifier** | **UUID** | Booking identifier identifier booking this review is associated with. | [optional] 
**hotel_identifier** | **UUID** | Hotel identifier this booking is associated with. | [optional] 
**user** | [**ReviewUserAuthenticatedEntity**](ReviewUserAuthenticatedEntity.md) | User details of creator of booking. | [optional] 
**review_date** | **datetime** | Date of review. | [optional] 
**average_score** | **float** | Total points divided by number of questions. | [optional] 
**answers** | [**List[ReviewAnswerAuthenticatedEntity]**](ReviewAnswerAuthenticatedEntity.md) | List of user review answers. | [optional] 
**message_from_guest** | **str** | Private message from guest to the hotel. Is not displayed on property profile. | [optional] 
**response_from_hotel** | **str** | Property can response to traveler review. Response goes on public review profile and can be seen by others. | [optional] 
**image_identifier** | **str** | Reviewer can upload her best picture from the property. Cloudinary image identifier. | [optional] 
**text** | **str** | Free text record created by traveler | [optional] 
**approved_text** | **bool** | Hotel allows the review text to be displayed as part of their profile. | [optional] 
**approved_image** | **bool** | Hotel allows the user-generated image to be displayed as part of their profile. | [optional] 
**likes** | **List[str]** | List of member identifiers who liked the textual review | [optional] 
**room_number** | **str** | Guest&#39;s room number during their stay. | [optional] 
**room_rating** | **int** | Guest&#39;s room rating | [optional] 
**responded** | **bool** | Returns true if property has responded to the review given by the guest. | [optional] [default to False]

## Example

```python
from wink_sdk_booking.models.review_authenticated_entity import ReviewAuthenticatedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewAuthenticatedEntity from a JSON string
review_authenticated_entity_instance = ReviewAuthenticatedEntity.from_json(json)
# print the JSON string representation of the object
print(ReviewAuthenticatedEntity.to_json())

# convert the object into a dict
review_authenticated_entity_dict = review_authenticated_entity_instance.to_dict()
# create an instance of ReviewAuthenticatedEntity from a dict
review_authenticated_entity_from_dict = ReviewAuthenticatedEntity.from_dict(review_authenticated_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


